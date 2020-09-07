# Water Flow Measurement for YF-S201 flow meter.
import RPi.GPIO as GPIO      # Import GPIO library
import time, sys             # Import time, sys library
GPIO.setmode(GPIO.BOARD)     # GPIO pin numbering
inpt = 13                    # Set input pin
GPIO.setup(inpt,GPIO.IN)     # Set input as input pin
rate_cnt = 0                 # Revolution counts (r/min)
tot_cnt = 0                  # Total counts
time_zero = 0.0              # System start up time
time_start = 0.0             # Keep measurement begin time
time_end = 0.0               # Keep measurement end time
gpio_last = 0                # Last state 0 or 1
pulses = 0                   # 0-5 pulses from YF-S201
constant = 1.79              # Water meter calibration factor

print(‘Water Flow - Approximate’)
print(‘Control C to exit’)

# Main while loop here
time_zero = time.time()
while True:                              # Infinite loop
    rate_cnt = 0                         # Reset rate counter
    pulses = 0                           # 0-5 pulses from YF-S201
    time_start = time.time()             # Keep start time
    while pulses <= 5:                   # 6 pulses per revolution
            gpio_cur = GPIO.input(input) # Poll input
            if gpio_cur != 0 and gpio_cur != gpio_last:
                pulses += 1
            gpio_last = gpio_cur         # Keep last input state
            try:
                None
            except KeyboardInterrupt:    # For the keyboard interruption
                print(‘¥nCTRL C - Exiting.’)
                GPIO.cleanup()
                print(‘Done’)
                sys.exit()

    rate_cnt += 1              # Revolutions / time
    tot_cnt += 1               # Total revs since start
    time_end = time.time()     # End of measurement time

    # Shows measurement results on the screen
    print(‘¥nLiters / min ‘,round((rate_cnt * constant)/(time_end-time_start),2),‘approximate’)
    print(‘Total Liters’, round(tot_cnt * constant, 1))
    print(‘Time (min & clock) ‘,
        round((time.time.() - time_zero)/60,2), ‘¥t’,
        time.asctime(time.localtime(time.time())), ‘¥n’)
