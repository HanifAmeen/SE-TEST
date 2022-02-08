a_list =[]
b_list =[]
c_list =[]
d_list =[]
e_list =[]

def main():
    
    range_1 = range(0, 121, 20)
    while True:
         try:
              Pass = int(input('Please enter your total PASS credits:- '))
              if Pass not in range_1 :
                  print(Pass, 'Out of range')
                  exit()
              defer = int(input('Please enter your total DEFER credits:- '))
               
              if defer not in range_1 :
                  print(defer, 'Out of range')
                  exit()
              fail = int(input('Please enter your total FAIL credits:- '))
               
              if fail not in range_1 :
                  print(fail, 'Out of range')
                  exit()
         except ValueError:
                      print("Integer invalid")
                      exit()
         break

      
    total=int(Pass)+int(defer)+int(fail)

    if (total != 120):
        print("Total Incorrect")
    else:
     
   
        if int(Pass)>119:
             print("Progress")
             a_list.append("*")
        elif int(Pass)>99:
            print("Progress (module Trailer)")
            b_list.append("*")
        elif int(Pass)>39 and int(fail)<79:
            print("Do not progress-Module retreiver")
            c_list.append("*")
        elif int (Pass)>19 and int (fail)<79:
            print("Do not progress-Module retreiver")
            c_list.append("*")
        elif int(Pass)<19 and int(fail)<79:
            print("Do not progress-Module retreiver")
            c_list.append("*")
        elif int(fail)>79:
            print("Exclude")
            d_list.append("*")

        restart=input("Would you like to enter another set of data?:- ")
        if restart == "y":
            e_list.append(2)
            main()
        else:
            if restart == "q":
                print("-------------------------------------------------------------------------------")
                print("Progress       Trailing        Retreiver         Exclude")
                
                print(a_list,b_list,c_list,d_list)

                
                
                print("-------------------------------------------------------------------------------")

main()







