count = 1
while True:
    user_input = input("Type 'stop' to end or press to continue : ")
    if user_input.lower() == 'stop':
        break 
    print(count)
    count +=1

