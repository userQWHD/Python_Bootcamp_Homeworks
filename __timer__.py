import time
q = int(input("Enter second(s): "))


def func(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Time ended!")

func(q)



# question
# How can I add a functional input, called "stop timer" here? and this function can show both timer and input question at the same time?