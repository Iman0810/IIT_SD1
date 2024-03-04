creditsTOEnter = [0, 20, 40, 60, 80, 100, 120]                                               #variables
progress_count, trailer_count, retriever_count, exclude_count = 0, 0, 0, 0
progress_list, trailer_list, retriever_list, exclude_list = [], [], [], []

# Multiple inpiuts
while True:

    # To loop until a valid input is given
    while True:
        try:
            pass_credit = int(input("Enter Credit at pass: "))
            if not pass_credit in creditsTOEnter:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    while True:
        try:
            defer_credit = int(input("Enter Credit at defer: "))
            if not defer_credit in creditsTOEnter:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    while True:
        try:
            fail_credit = int(input("Enter Credit at fail: "))
            if not fail_credit in creditsTOEnter:
                print("Out of range")
            else:
                break
        except ValueError:
            print("Integer required")

    
    Total = pass_credit + defer_credit + fail_credit
    if Total != 120:                                    #checking the total
        print("Total incorrect")
    else:    
        # Checking the outputs
        if pass_credit == 120:
            print("Progress")
            progress_count += 1                        #increase related credit count
            progress_list.append([pass_credit, defer_credit, fail_credit])
        elif pass_credit == 100:
            print("Progress (module trailer)")
            trailer_list.append([pass_credit, defer_credit, fail_credit])
            trailer_count += 1                          # increase related credit count
        elif fail_credit >= 80:
            print("Exclude")
            exclude_list.append([pass_credit, defer_credit, fail_credit])
            exclude_count += 1                          # increase related credit count
        else:
            print("module retriever")
            retriever_list.append([pass_credit, defer_credit, fail_credit])
            retriever_count += 1                       # increase related credit count
    
    
    Order = input("Enter 'q' to exit the program \nElse enter 'y' to continue: ")       #asking user input to continue or quit the program
    if Order.lower() == "q": 
        print("Exiting program")
        break
        
        
                                                                                      
                                                                                     
print("Histogram")                                                     # Histogram
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
        
                                                          
print("Part 2")                                                   # Print out the list
for item in progress_list:
    print(f"Progress - {', '.join(str(i) for i in item)}")
    
for item in trailer_list:
    print(f"Trailer - {', '.join(str(i) for i in item)}")
    
for item in exclude_list:
    print(f"Exclude - {', '.join(str(i) for i in item)}")

for item in retriever_list:
    print(f"Retriever - {', '.join(str(i) for i in item)}")
    
    
    
    
# pary 3 text file
with open("output.txt", "w") as newfile: # w/ r/ a
    newfile.write("Part 3: \n")
    for item in progress_list:
        newfile.write(f"Progress - {', '.join(str(i) for i in item)}\n")
        
    for item in trailer_list:
        newfile.write(f"Trailer - {', '.join(str(i) for i in item)}\n")
        
    for item in exclude_list:
        newfile.write(f"Exclude - {', '.join(str(i) for i in item)}\n")

    for item in retriever_list:
        newfile.write(f"Retriever - {', '.join(str(i) for i in item)}\n")