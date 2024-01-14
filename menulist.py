def App():
    
    #print("Data structure operation in python")
    mylist = []
    mytuple = ()
    myset = {}
    #mylist=input("Enter the my list value")
    #mytuple=input("Enter the my tuple value")
    #myset=input("Enter the my set value")
    while (True):
        print("Welcome to my Application")
        print("Press 1 for list operation")
        print("Press 2 for tuple operation")
        print("Press 3 for set operation")
        print("Press 4 for Exit operation")
        num=int(input("please enter number"))
        if num == 1 :
            listops(mylist)
        
        #elif num == 2: 
            #tupleops(mytuple)
        #elif num == 3:
            #setops(myset)

        #elif num == 4:
            print("Exiting the Application")
            break

def listops(xyz):
            while (True):
                print("Welcome to my List operation")
                print("Press 1 for adding to List")
                print("Press 2 for removing from List")
                print("Press 3 for display a List")
                print("Press 4 for back to main Menu")
                num=int(input("please enter number"))
                if num == 1:
                    element=input("enter the elment to be added to list")
                    xyz.append(element)
                elif num == 2:
                    element=input("enter the elment to be removed")
                    if element in xyz:
                        xyz.remove(element)
                    else:
                         print("The entered removal value not present in the list")
                elif num == 3:
                    print(xyz)
                elif num ==4:
                    break
App()

          