progress_count, trailer_count, retriever_count, exclude_count= 0,0,0,0

def check_Validity(value):        #define the function
    creditRange =[0,20,40,60,80,100,120]  #define the valid credit range
    try:
        value=int(value)
        if not value in creditRange:
            print("out of range")
            return "error"
        return value
    except ValueError:
        print("Integer Required")
        return "error"
       
    
while True:


    while True:
        pass_credit = input("Please enter your credits at pass: ")     #get user input pass credit and validate
        pass_credit = check_Validity(pass_credit)
        if pass_credit != "error":
         break    

    while True:
        defer_credit = input("Please enter your credits at defer: ")  #get user input defer credit and validate
        defer_credit = check_Validity(defer_credit)
        if defer_credit != "error":
         break  

    while True:
        fail_credit = input("Please enter your credits at fail: ")   #get user input fail credit and validate
        fail_credit = check_Validity(fail_credit)
        if fail_credit != "error":
         break   

    Total = pass_credit + defer_credit + fail_credit
    if Total != 120:              #check the total of input credits
       print("Total Incorrect")   #if total incorrect, print this message   
    else:
       if pass_credit == 120:    #check pass credits equals to 120
          print("Progress")      #print the appropriate message
          progress_count += 1    #increase related credit counter
       elif pass_credit == 100:  #check pass credit equals to 100
          print("Progress(Module trailer)")   #print the appropriate message
          trailer_count += 1                  #increase related credit counter
       elif fail_credit >= 80:                #check fail credit greater than or equals to 80
          print("Exclude")                    #print the appropriate message
          exclude_count += 1                  #increase related credit counter
       else:
          print("module retriever")           #print the appropriate message
          retriever_count += 1                #increase related credit counter

    Order = input("Enter 'q' to exit the program and view results\nElse enter 'y' to continue: ")   #get user input for quit or continue the program      
    if Order.lower() == 'q':
      print("Exiting program")  

      break
      

print(f"Progress {progress_count} : ", end="")
print("*" * progress_count)
print(f"Trailer {trailer_count}  : ", end='')
print("*" * trailer_count)
print(f"Retriever {retriever_count}: ", end='')
print("*" * retriever_count)
print(f"Exclude {exclude_count}  : ", end='')
print("*" * exclude_count)

outcome_count = progress_count + trailer_count + retriever_count + exclude_count
print(outcome_count, end="")
print(" outcomes in total.")    #total outcomes