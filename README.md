# youtube-controled-pwm
A program to controll a pwm pin on a raspberry pi based on a youtube livestream's comments

# Installation instructions:
Simply enter the following commands into the terminal:

pip3 install pytchat

cd /home/pi/Desktop

wget https://raw.githubusercontent.com/kittycat959/youtube-controled-pwm/main/program.py

# Running the program:
Before running the program there are a few lines that must be configured to tell the program about your setup, these lines are on line number 11 through to line number 16, the program will have been saved to the desktop so you can simply double click on the file to open it or you can type "nano /home/pi/Desktop/program.py" without the quotes to open it in the terminal, if you descide to do this press control, then y then enter twice in order to save the changes you have made.

## The lines that may need chaning are below allong with what they are used for:

pin_to_use_filter tells the program what pin to use to output its control voltage for the filter

pin_to_use_resonance tells the program what pin to use to ouptut its control voltage for the resonance

filter_percentage is the percentage dutycycle to start the filter control voltage on

resonance_percentage is the percentage dutycycle to start the resonance control voltage on

time_for_filter_change is the interval in seconds between cv updates

video_url is the video url of the live stream and it must be but between the apostrophes

After all these lines have been updated and saved you can run the program by typing python3 /home/pi/Desktop/program.py
