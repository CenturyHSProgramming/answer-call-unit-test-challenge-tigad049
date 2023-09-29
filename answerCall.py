# answerCall.py
# by David Tigas

def answerCall(caller_code: str, same_area_code: bool, cur_time: str):
    should_answer_call = True

    cur_time_int = int(cur_time.replace(':', ''))
    if cur_time_int < 700 or cur_time_int > 2200:
        should_answer_call = False

    if same_area_code == False:
        if caller_code == "U":
            should_answer_call = False
    
    if caller_code == "T":
        should_answer_call = False
    
    return should_answer_call

if __name__ == '__main__':
    pass
