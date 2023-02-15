#Variables
name = input("What is your name? ").capitalize
merit_credits_earned = 0
excellence_credits_earned = 0


#Functions
def ncea_calculator ():
    try:
        while True:

            total_ncea_credits = int(input("How many Ncea Level 1 Credits have you earned? "))

            if total_ncea_credits >= 50:
                excellence_credits_earned = int(input("How many Excellence Level 1 credits have you earned? "))
                while excellence_credits_earned > total_ncea_credits:
                    print("You cannot have more Excellence credits than total credits earned ")
                    ncea_calculator()

                if  excellence_credits_earned >= 50:
                    print("You have completed Level 1 with Excellence Endorsed! ")
                    end()
                    break
                    
                elif excellence_credits_earned <= 50:
                    merit_credits_earned = int(input("How mant Merit Level 1 credits have you earned? "))

                if excellence_credits_earned + merit_credits_earned > total_ncea_credits:
                    print("You cannot have more Excellence and Merit credits than total credits earned Please Try again ")
                    ncea_calculator()

                elif merit_credits_earned + excellence_credits_earned >= 50:
                    print("You have completed level 1 with Merit Endorsed! ")
                    end()
                    break
                    
                else:
                    print("You have passed Level 1 but you have not gained any endorsements ")
                    break

            if total_ncea_credits < 0:
                print("That is not an acceptable answer please try again ")
                ncea_calculator()
            
            if total_ncea_credits > 120:
                print("You cannot earn more than 120 credits in level 1")
                ncea_calculator()
            
            if total_ncea_credits < 50:
                print("You have not passed Level 1 and therefore am not available for an endorsement")
                break
    except NameError:
        problem()
    
    except ValueError:
        problem ()
    
def problem ():
    print("That is not an appropriate answer, try again")
    ncea_calculator ()

    

    

    

def end ():
    while True:
        print("Congratulations")
        break
    
    
ncea_calculator()


    
