list1=[]
def insert():
    empno=(int)(input("Enter the employee number:"))
    list1.append(empno)
    a=input("Enter the name:")
    list1.append(a)
    age=(int)(input("Enter Age:"))
    list1.append(age)
    designation=input("Enter Designation:")
    list1.append(designation)
    salary=(int)(input("Enter Salary:"))
    list1.append(salary)
def delete_item():
    try:
        del1=(int)(input("Enter the employee number to delete"))
        index2=list1.index(del1)
    except ValueError:
        print("Employement Number Not Found")
    else:
        list1.remove(list1[index2])
        print("Element Deleted")
def search_item():
    try:
        search=(int)(input("Enter the emp no to search:"))
        index1=list1.index(search)
    except ValueError:
        print("Element not Found")
    else:
        print("Element Found")
def display_item():
    try:
        num=(int)(input("Enter the emp no to Display:"))
        index1=list1.index(num)
    except ValueError:
        print("Element not found")
    else:
        print("Employee Number=",list1[index1])
        print("Employee Name=",list1[index1+1])
        print("Employee Age=",list1[index1+2])
        print("Employee Designation=",list1[index1+3])
        print("Employee Salary=",list1[index1+4])
def pf_item():
    try:
        num=(int)(input("Enter the emp no to Display:"))
        index1=list1.index(num)
    except ValueError:
        print("Element not found")
    else:
        num=list1[index1+4]
        if(num<10000):
            print("Gross Salary=",num)
            PF=num*0.05
            print("Provident Fund=",PF)
            ESI=num*0.02
            print("ESI=",ESI)
            deduction=PF+ESI
            print("Total Deduction=",deduction)
            Net_salary=num-deduction
            print("Net salary=",Net_salary)
        else:
            print("Gross Salary=",num)
            PF=num*0.08
            print("Provident Fund=",PF)
            ESI=num*0.01
            print("ESI=",ESI)
            deduction=PF+ESI
            print("Total Deduction=",deduction)
            Net_salary=num-deduction
            print("Net salary=",Net_salary)
print("Select any choice:")
print("1.Insert")
print("2.Delete")
print("3.Search")
print("4.Display")
print("5.Provident Fund Calculation")
while True:
    choice=(int)(input("Enter Your Choice:"))
    if(choice==1):
        insert()
    elif(choice==2):
        delete_item()
    elif(choice==3):
        search_item()
    elif(choice==4):
        display_item()
    elif(choice==5):
        pf_item()

    else:
        quit()
