import pytchat
import threading
import RPi.GPIO as GPIO
import time

global filter_percentage #makes the variable filter_percentage accessable globally
global resonance_percentage #makes the variable resonance_percentage accessable globally
global pin_to_use_filter #makes the variable pin_to_use_filter accessable globally
global pin_to_use_resonance #makes the variable pin_to_use_resonance accessable globally

pin_to_use_filter = 40 #the gpio pin number to output the pwm signal on for the filter control coltage
pin_to_use_resonance = 38 #the gpio pin number to output the pwm signal on for the resonance control coltage
filter_percentage = 100 #the duty cycle of the pin connected to the filter control voltage
resonance_percentage = 0 #the duty cycle of the pin connected to the resonance control voltage
time_for_filter_change = 1 #the amount of time in seconds between filter changes
video_url = "" #the url of the video to check the chat on (put it between the apostaphies)

def pwm(time_for_filter_change): #defines the pwm function with the argument time_for_filter_change
    #this section sets up the first gpio pin for the filter cv
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(pin_to_use_filter, GPIO.OUT)
    filter_pwm = GPIO.PWM(pin_to_use_filter, 8000)
    filter_pwm.start(filter_percentage)

    #this section sets up the second gpio pin for the resonance cv
    GPIO.setup(pin_to_use_resonance, GPIO.OUT)
    resonance_pwm = GPIO.PWM(pin_to_use_resonance, 8000)
    resonance_pwm.start(resonance_percentage)

    #updates the dutycycle of the two pwm pins with the delay defines in time_for_filter_change
    while True:
        print(filter_percentage)
        filter_pwm.ChangeDutyCycle(filter_percentage)
        resonance_pwm.ChangeDutyCycle(resonance_percentage)
        time.sleep(time_for_filter_change)

#creates and starts a thread for the pwm function to ensure there are no drop outs when we read the messages
pwm_thread = threading.Thread(target=pwm, args=([time_for_filter_change]))
pwm_thread.start()

def message_retriever(video_url): #defines the message_retriever function with the argument video_url
    #ensures we are using global and not local namespace for these variables
    global filter_percentage 
    global resonance_percentage

    #this section gets the new messages from the chat
    chat = pytchat.create(video_url)
    while chat.is_alive():
        for c in chat.get().sync_items():
            message = f"{c.message}"
            print(message)

            #this section preforms a series of checks to validate the input from the chat for the filter percentage
            if len(message) > 7 and len(message) < 11:
                if message[0:7] == "filter ":
                    if message[7:len(message)].isdigit():
                        if int(message[7:len(message)]) < 101:
                            filter_percentage = int(message[7:len(message)])

            #this section preforms a series of checks to validate the input from the chat for the resonance percentage
            if len(message) > 10 and len(message) < 14:
                if message[0:10] == "resonance ":
                    if message[10:len(message)].isdigit():
                        if int(message[10:len(message)]) < 101:
                            resonance_percentage = int(message[10:len(message)])
            
message_retriever(video_url) #calls the message_retriever function with the argument video_url
