# answerCall.py
# by _______

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()

# Make sure it returns a value

def answerCall(caller_code: str, sameAreaCode: bool, cur_time: str):
    shouldAnswerCall = True

    while shouldAnswerCall == True:
        cur_time_int = int(cur_time.replace(':', ''))
        if cur_time_int < 700 or cur_time_int > 2200:
            shouldAnswerCall = False

        if sameAreaCode == False:
            if caller_code == "T" or caller_code == "U":
                shouldAnswerCall = False
        elif sameAreaCode == True:
            if caller_code == "T":
                shouldAnswerCall = False
        
        return shouldAnswerCall

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
