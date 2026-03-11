# (){}[]

def valid_paranthese(s: str):
    validStack = []

    for char in s:
        if char == ")" and validStack and validStack[-1] == "(" :
            validStack.pop()
        elif char == "}" and validStack and validStack[-1] == "{":
            validStack.pop()   
        elif char == "]" and validStack and validStack[-1] == "[":
            validStack.pop()     
        else:
            validStack.append(char)

    return not validStack    


s = ")"

result = valid_paranthese(s)
print("result : ", result)

#o(n) complexity
