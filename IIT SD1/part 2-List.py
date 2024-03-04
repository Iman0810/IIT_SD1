creditRange = [0, 20, 40, 60, 80, 100, 120]
progress_count, trailer_count, retriever_count, exclude_count = 0, 0, 0, 0
progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []


while True:     # Multiple inpiuts

    
    while True:                   # To loop until a valid input is given
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

   
    Total = pass_credit + defer_credit + fail_credit    #checking the total
    if Total != 120:
        print("Total incorrect")                        #print the appropriate message
    else:    
        if pass_credit == 120:
            print("Progress")
            progress_count += 1                         #increase related credit count
            progress_list.append([pass_credit, defer_credit, fail_credit])
        elif pass_credit == 100:
            print("Progress (module trailer)")           
            trailer_list.append([pass_credit, defer_credit, fail_credit])
            trailer_count += 1                          #increase related credit count
        elif fail_credit >= 80:
            print("Exclude")
            exclude_list.append([pass_credit, defer_credit, fail_credit])
            exclude_count += 1                          #increase related credit count
        else:
            print("module retriever")
            retriever_list.append([pass_credit, defer_credit, fail_credit])
            retriever_count += 1                        #increase related credit count
    
    
    Order = input("Enter 'q' to exit the program \nElse press 'y' to continue: ")
    if Order.lower() == "q":
        print("Exiting program")
        break
        
        

print("Histogram")                                              # Histogram
print(f"Progress {progress_count} : ", end="")
print("*" * progress_count)
print(f"Trailer {trailer_count}  : " , end='' )
print("*" * trailer_count)
print(f"Retriever {retriever_count}: ", end='')
print("*" * retriever_count)
print(f"Exclude {exclude_count}  : ", end='')
print("*" * exclude_count)

outcome_count = progress_count + trailer_count + retriever_count  + exclude_count 
print(outcome_count, end="")
print(" outcomes in total.")
        


for item in progress_list:                                             # Print out the list
    print(f"Progress - {', '.join(str(i) for i in item)}")
    
for item in trailer_list:
    print(f"Trailer - {', '.join(str(i) for i in item)}")
    
for item in exclude_list:
    print(f"Exclude - {', '.join(str(i) for i in item)}")

for item in retriever_list:
    print(f"Retriever - {', '.join(str(i) for i in item)}")