#bearish pattern 
if (open>close and 
    prevcioius_open<previous_close and
    close<previous_open and 
    open>=previous_close):
        return 1

# selling signal 

#bullish pattern
elif(open<close and
     previous_open>previouis_clsoe and
     close>previous_open and
     open<=previous_close):
        return 2

# buying signal.