'''
Program written by Alex Brown in Python 2.7.13, with the purpose of creating
a method for determining someone's future job, housing, projected income,
and number of kids.
'''


def start(name = "",age = 0,currentIncome = 0.0, kids =0):
    #get user's information
    name,age,currentIncome,kids = info(name,age,currentIncome,kids)
    #start by finding the user's future job
    career = job(name)
    print("\nWe just determined your future career!")
    #moves to finding a house
    home = house(name)
    print("\nLet's determine your income now")
    #finds future income for user
    futureIncome = income(name,age,currentIncome)
    #find user's numebr of kids
    print("\nNow we've reached everyone's favorite part. Predicting your future number of kids!")
    futureKids = children(name,kids)
    #prints out final results and ask to play again
    end(name,career,home,futureIncome,futureKids,age,currentIncome,kids)





def info(name,age,currentIncome,kids):
    name = raw_input("\nWhat is your name? ")
    print("\nOk {}, I am going to ask you a few questions.".format(name))
    stop = True
    while stop:
        try:
            age = int(raw_input("\nHow old are you? "))
            stop = False
        except:
            print("\nYou typed your age incorrectly, please try again.")
            
        
    stop = True
    while stop:
        try:
            currentIncome = float(raw_input("\nIf you don't mind me asking, what is your salary? (ex.1500.23): "))
            stop = False
        except:
            print("\nSalary format is incorrect, try again and look at the example.")
    kids = int(raw_input("\nHow many kids do you have? (0 = none) "))
    print("\nThank you for your answers")
    
    return name,age,currentIncome,kids

def job(name):
    career = ['Doctor', 'Cop', 'Engineer', 'Journalist', 'Musician']
    #list the user's potential careers
    print("\nLet's see your possible career options: ")
    for i in career:
        print i
    stop = True
    while stop:
        try:
            prefCareer = raw_input("\nChoose a career: ").title()
            index = (4 - career.index(prefCareer))
            stop = False
        except:
            print("\n{} was not a career option, please try again.".format(prefCareer))
    print("\nThank you for your choice {}!".format(name))
    #use the indvidual's chosen career to determine their future career
    futureJob = career[index]
    return futureJob
        
            
def house(name):
    print("\nNow let's figure out where you will live:")
    options = (1,4,6,8)
    stop = True
    empty = []
    #have the use pick numbers, which will be compared againt the tuple options
    i = 0
    while i < 5:
        try:
            choice = int(raw_input("\nPick a number 1-8, we'll do this five times total:"))
            if choice < 0 or choice > 8:
                print("\n You did not pick number between 1 and 8, please try again.")
                continue 
            elif choice not in empty:
                empty.append(choice)
                i += 1
            else:
                print("\nYou already picked that number, try again")
                continue
        except:
            print("\n You did not pick an INTEGER, please try again.")

    store = []
    #if any of the chosen numbers are in the tuple it is added to the list store
    for i in options:
        if i in empty:
            store.append(i)
        else:
            store.append(0)
    
    total = sum(store)
    if total < 5:
        home = "trailer"
    elif total > 5 and total < 10:
        home = "apartment"
    elif total > 10 and total < 13:
        home = "house"
    else:
        home = "mansion"
    print("\nWe just found your future home {}!").format(name)
    return home
        
        
        
        
def income(name,age,currentIncome):
        stop = True
        while stop:
            try:
                desiredIncome = float(raw_input("\nWhat do you think your future salary will be? (ex.1500.23): "))
                stop = False
            except:
                print("\nSalary format is incorrect, try again and look at the example.")
                
        #Take's what the user want's their future income to be and uses it to determine
        #their predicted future income
        modulo = currentIncome/desiredIncome
        step1 = age * modulo
        step2 = step1 + 1
        futureIncome = currentIncome*step2
        print("\nOk {}, we have your predicted future income!".format(name))
        return futureIncome

def children(name,kids):
          options = (0,1,2,3,4,5)
          print("\nLet's see the possibilities for future number of kids: ")
          for i in options:
              print i
          stop = True
          #uses tuple of options to mathematically find the number of kids the user will have
          while stop:
              try:
                choice = int(raw_input("\nPlease choose a number between 0 and 5: "))
                if choice < 0 or choice > 5:
                  print("\nYou did not choose a number between 0 and 5, please try again")
                  continue
                else:
                    stop = False
              except:
                  print("\nYou did not choose an integer, please try again")
          offSpring = (kids-choice) + 6
          print("\nCool, we have an idea on the number of kids you will have!".format(name))
          return offSpring
          
          
def end(name,career,home,futureIncome,futureKids,age,currentIncome,kids):
    #presents all of the user's results as a string
    job = career.lower()
    salary = math.ceil(futureIncome)
    print("\nAlright {}, here are your results: You will be a {} and will live in (a/an) {}.".format(name,job,home))
    print("\nYou will have a salary of ${} and will have {} kids, congrats!".format(salary,futureKids))
    stop = True
    while stop:
        choice = raw_input("\nUnhappy with your results? Try again (y/n) ")
        if choice == 'y':
            again(name,age,currentIncome,kids)
        elif choice == 'n':
            print("\nBye {}, thanks for using Success Predictor!".format(name))
            stop = False
        else:
            print("\nYou did not select y for 'yes' or n for 'no', please try again.")
            continue
         



def again(name,age,currentIncome,kids):
    print("\nAlright {}, I know you were not happy with your previous results, so let's try again.".format(name))
    #start by finding the user's future job
    career = job(name)
    print("\nWe just determined your future career!")
    #moves to finding a house
    home = house(name)
    print("\nLet's determine your income now")
    #finds future income for user
    futureIncome = income(name,age,currentIncome)
    #find user's numebr of kids
    print("\nNow we've reached everyone's favorite part! Predicting future number of kids!")
    futureKids = children(name,kids)
    #prints out final results and ask to play again
    end(name,career,home,futureIncome,futureKids,age,currentIncome,kids)





if __name__ == "__main__":
    import math
    start()
