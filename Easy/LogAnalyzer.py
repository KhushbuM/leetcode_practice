#["ERROR Disk full",
#  "INFO User logged in",
#  "ERROR Timeout",
#  "WARNING CPU high"]



def log_analyzer(log : list):
    freq = {}
    levels = {"ERROR", "INFO", "WARNING"}

    
    

    for line in log:
        if not line.strip():
            continue

        words = line.split()

        for word in words:
            if word in levels:
                freq[word] = freq.get(word, 0) + 1

    return freq    


input = ["ERROR Disk full",
 "User logged in INFO",
 "WARNING CPU WARNING"]

result = log_analyzer(input)
print("result : ", result)