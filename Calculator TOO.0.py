HISTORY=[]
last_answers=HISTORY
EXPRESSIONS=[] #The expression of the last calculation will be stored as a string for later presentation when scrolling History.
global last_answer
global gapped #Formatting. Helps print the calculation in consecutive lines.
global mode

def menu():
    print("\nCALCULATOR TOO.0\n" + "─" * 16)
    mode="Main Menu"
    print(mode + "\n" + '―' * len(mode))  # U+2015, Horizontal Bar
    print("1. Calculator\n\n2. History\n\n3. Memory\n")

    while True: #Scans for option 1.
        mode_select=input("Enter mode: ") #Try to accept alphabetic or numerical answers.
        mode_select=mode_select.lower()
        if mode_select in ["1", "c", "calculator"]:
            calculator()
        elif mode_select in ["q", "quit", "exit"]:
            calculator()
        else:
            break

    while True: #scans for option 2.
        mode_select=input("Enter mode: ")
        mode_select=mode_select.lower()
        if mode_select in ["2", or "h", or "history"]:
            history()
        elif mode_select in ["q", "quit", "exit"]:
            calculator()
        else:
            break
    
    while True: #Scans for option 3.
        mode_select=input("Enter mode: ")
        mode_select=mode_select.lower()
        if mode_select in ["3", "m", "memory"]:
            memory()
        elif mode_select in ["q", "quit", "exit"]:
            calculator()
        else:
            break


def calculator():
    looper=True
    gapped=False
    while(looper==True):
        #print("CALCULATOR TOO.0\n\n\nHistory\n-------\n" + str(last_answers) + "\n")
        print("\nCALCULATOR TOO.0\n" + "─" * 16)
        mode="Calculator Mode"
        print(mode + "\n" + '―' * len(mode))  # U+2015, Horizontal Bar
        history_subtitle()
        arg1=float(input("Enter quantity: ")) #Later version might not even prompt user for 'quantity,' but instead ask for the entire expression (more streamlined).
        cc1=len(str(arg1)) #Character count 1
        
        while True:
            op1=input(str("\n+  -  *  /\nEnter operator: ")) #Add option to return or exit later.
            if op1 in ["+", "-", "*", "/"]:
                show_work(gapped, op1, cc1, arg1)
                break
            else:
                print("Please enter a valid operator.\n")
                gapped=True

#def history():


def memory():

def history_subtitle():
    string='History'
    emptystring=''

    for i in range(0, len(string)):
        if string[i]==' ':
            emptystring=emptystring + string[i]
        else:
            emptystring=emptystring + string[i] + str('\u0332') #Underlines 'History.'
    
    print(emptystring)
    print(*HISTORY, sep=", ") #Prints history of answers without square brackets, each item separated by a comma and whitespace.

def show_work(gapped, op1, cc1, arg1):
    if(gapped==False):
        arg2=float(input(op1 + " "))
        cc2=len(str(arg2)) #Character count 2
    else:
        arg2=float(input(str(arg1) + "\n" + op1 + " "))
        cc2=len(str(arg2))
        #cc_space=abs(cc1-cc2) #Formatting
        gapped=False #Reset

    if(cc1>=cc2):
        print("─" * cc1) #Line of equivalence
    elif(cc2>=cc1):
        print("─" * cc2) #Line of equivalence

    #print("\n" + "   " + str(arg1) + "\n" + op1 + "  " + str(arg2))
        
    if(op1=="+"):
        answer=arg1+arg2
        HISTORY.append(answer)
        print(answer)
        #last_answers=HISTORY[]

    elif(op1=="-"):
        answer=arg1-arg2
        HISTORY.append(answer)
        print(answer)

    elif(op1=="*"):
        answer=arg1*arg2
        HISTORY.append(answer)
        print(answer)

    elif(op1=="/"):
        answer=arg1/arg2
        HISTORY.append(answer)
        print(answer)

calculator() #A true, dedicated calculator should launch ready to calculate before offering other services.

menu()