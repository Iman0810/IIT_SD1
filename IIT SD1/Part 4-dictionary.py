creditRange = [0, 20, 40, 60, 80, 100, 120]
progress_count, trailer_count, retriever_count, exclude_count = 0, 0, 0, 0          # variables
progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []
myDictionary = {}

# Multiple inpiuts
while True:

    # To loop until a valid input is given
    UOWnumber = input("Enter your UOW number: ")
    
    while True:
        try:
            pass_credit = int(input("Enter Credit at pass: "))
            if not pass_credit in creditRange:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    while True:
        try:
            defer_credit = int(input("Enter Credit at defer: "))
            if not defer_credit in creditRange:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    while True:
        try:
            fail_credit = int(input("Enter Credit at fail: "))
            if not fail_credit in creditRange:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    # Total Checking
    Total = pass_credit + defer_credit + fail_credit
    if Total != 120:
        print("Total incorrect")
    else:    
        # Checking the outputs
        if pass_credit == 120:
            print("Progress")
            progress_count += 1
            progress_list.append([pass_credit, defer_credit, fail_credit])
            
            myDictionary[UOWnumber] = f"Progress - {pass_credit}, {defer_credit}, {fail_credit}"
            
        elif pass_credit == 100:
            print("Progress (module trailer)")
            trailer_list.append([pass_credit, defer_credit, fail_credit])
            trailer_count += 1
            
            myDictionary[UOWnumber] = f"Trailer - {pass_credit}, {defer_credit}, {fail_credit}"
            
        elif fail_credit >= 80:
            print("Exclude")
            exclude_list.append([pass_credit, defer_credit, fail_credit])
            exclude_count += 1
            
            myDictionary[UOWnumber] = f"Exclude - {pass_credit}, {defer_credit}, {fail_credit}"
            
        else:
            print("module retriever")
            retriever_list.append([pass_credit, defer_credit, fail_credit])
            retriever_count += 1
             
            myDictionary[UOWnumber] = f"Retriever - {pass_credit}, {defer_credit}, {fail_credit}"
             
    
    
    Order = input("Enter 'q' to exit the program \nElse enter 'y' to continue: ")
    if Order.lower() == "q":
        print("Exiting program")
        break
    

# key : value
for i,j in myDictionary.items():
    print(f"{i} : {j}", end=" ")
    
print()