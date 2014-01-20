######################################
## 9 - 5    clock using the PiGlow  ##
##                                  ##
##  Example by @Tommybobbins        ##
######################################

from piglow import PiGlow
from time import sleep
from datetime import datetime

piglow = PiGlow()


### You can customise these settings ###

ledbrightness = 255      # Set brightness of LED - 1-255 (recommend 10-20, put 0 and you won't see it!)
ledmixbrightness = 128      # Set brightness of LED - 1-255 (recommend 10-20, put 0 and you won't see it!)
hourflash = 1           # Choose how to flash change of hour - 1= white leds, 2= all flash

#########################################


def clock_colour(hour):
#    print ("Colour = %i\n" % hour)
    if hour == 9:
        piglow.all(0) 
        sleep(0.5)
        piglow.red(ledbrightness) 
        sleep(0.5)
        piglow.red(ledbrightness) 
    elif hour == 10:
        piglow.all(0) 
        sleep(0.5)
        piglow.orange(ledbrightness) 
        sleep(0.5)
        piglow.orange(ledbrightness) 
    elif hour == 11:
        piglow.all(0) 
        sleep(0.5)
        piglow.yellow(ledmixbrightness) 
        piglow.orange(ledmixbrightness) 
        sleep(0.5)
        piglow.yellow(ledmixbrightness) 
        piglow.orange(ledmixbrightness) 
    elif hour == 12:
        piglow.all(0) 
        sleep(0.5)
        piglow.yellow(ledbrightness) 
        sleep(0.5)
        piglow.yellow(ledbrightness) 
    elif hour == 13:
        piglow.all(0) 
        sleep(0.5)
        piglow.yellow(ledmixbrightness) 
        piglow.green(ledmixbrightness) 
        sleep(0.5)
        piglow.yellow(ledmixbrightness) 
        piglow.green(ledmixbrightness) 
    elif hour == 14:
        piglow.all(0) 
        sleep(0.5)
        piglow.green(ledbrightness) 
        sleep(0.5)
        piglow.green(ledbrightness) 
    elif hour == 15:
        piglow.all(0) 
        sleep(0.5)
        piglow.green(ledmixbrightness) 
        piglow.blue(ledmixbrightness) 
        sleep(0.5)
        piglow.green(ledmixbrightness) 
        piglow.blue(ledmixbrightness) 
    elif hour == 16:
        piglow.all(0) 
        sleep(0.5)
        piglow.blue(ledbrightness) 
        sleep(0.5)
        piglow.blue(ledbrightness) 
    elif hour == 17:
        piglow.all(0) 
        sleep(0.5)
        piglow.blue(ledmixbrightness) 
        piglow.red(ledmixbrightness) 
        sleep(0.5)
        piglow.blue(ledmixbrightness) 
        piglow.red(ledmixbrightness) 
    else:
        piglow.all(0) 
        sleep(0.5)
        piglow.white(10) 
        sleep(0.5)
        piglow.white(10) 


### End of customising ###

piglow.all(0)

hourcount = 0
hourcurrent = 0
minutecurrent = 15

while True:
    time = datetime.now().time()
    hour,min,sec = str(time).split(":")
    sec,micro = str(sec).split(".")
    hour = int(hour)
    min = int (min)

    # Check if current hour is different and set ready to flash hour
    if (minutecurrent%15 == 0):
#        print "0,15,30,45 minutes past the hour" 
        minutecurrent = min 
        hourcount = hour
        hourcurrent = hour
        clock_colour(hour)
        sleep(60)
#    if hourcurrent != hour:
#        hourcount = hour
#        hourcurrent = hour
#        clock_colour(hour)
    else:
        calc= minutecurrent%15
#        print ("Sleeping because calc= %i\n"  % calc )
        sleep(10)
