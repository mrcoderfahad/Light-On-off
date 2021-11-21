check = ""
light_on = False
while (check != 'sleep'):
    check = input(">>> ").lower()

    if check == 'on':
        if light_on == 'on':
            print("Light Is Already On Mode")
        else:
            light_on = True
            print("Light Turned On Mode")
    elif check == 'off':
        if not light_on:
            print("Light Is Already In off Mode")
        else:
            light_on = False
            print("Light Turned Off Mode")
    elif check == 'sleep':
        print("This Programme Going To Sleep Mode")
        break
    elif check == 'help':
        print("""1. On - Light ON
2. Off - Light Off
3. Sleep - exit programme
        """)
    else:
        print("I Don't Understand Your Command!!!")

    
