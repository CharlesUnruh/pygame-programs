import sys
import random

options = ["Drink from your Canteen.",
                "Ahead moderate speed.",
                "Ahead full speed.",
                "Stop and rest.",
                "Status Check.",
                "Quit"]
    
def printOptions():
    for i in range(len(options)-1):
        print(chr(ord('A')+i) + ". " + options[i])
    print("Q. " + options[-1])
        
def getInput():
    printOptions()
    user_input = input("Your choice? ")
    user_input = user_input.lower()
    while user_input != 'q' and user_input not in [chr(ord('a')+i) for i in range(len(options)-1)]:
        print("Please make a slection between 'a' and '"+chr(ord('a')+len(options)-1)+"' or 'q'.")
        user_input = input("Your choice? ")
        user_input = user_input.lower()
    return user_input

def drink(state):
    if state.thirst_canteen <= 0:
        print("There's no more water left in your canteen...")
    else:
        state.thirst_current -= 1
        state.thirst_canteen -= 1
        print("You take a sip from your canteen.")
    
    
def moderate_speed(state):
    travel = random.randint(5,12)
    state.distance_traveled += travel
    print("You have traveled " + str(travel) + " miles.")
    state.tiredness_current += 1
    state.thirst_current += 1
    state.distance_natives += random.randint(7,14)
    randomEvent(state)
    

def full_speed(state):
    travel = random.randint(10,20)
    state.distance_traveled += travel
    print("You have traveled " + str(travel) + " miles.")
    state.tiredness_current += random.randint(1,3)
    state.thirst_current += 1
    state.distance_natives += random.randint(7,14)
    randomEvent(state)
    

def rest(state):
    state.tiredness_current = 0
    print("Your camel appreciates the well-earned rest.")
    state.distance_natives += random.randint(7,14)
    
def quit(state):
    print("Thanks for playing!")
    

def examine(state):
    print("examine")
    print("Current distance traveled: " + str(state.distance_traveled))
    print("Drinks in Canteen: " + str(state.thirst_canteen))
    print("The natives are " + str(state.distance_natives) + " miles behind you.")


command_list = [drink, moderate_speed, full_speed, rest, examine]
command_dict = { (chr(ord('a')+i)):command_list[i] for i in range(len(command_list))}
command_dict['q'] = quit

def oasis(state):
    print("You've found an Oasis! Your canteen is full, and your camel is rested!")
    state.thirst_canteen = state.thirst_canteen_max
    state.thirst_current = 0
    state.tiredness_current = 0

event_list = [oasis]
event_probabilities = [.05]

def randomEvent(state):
    for i in range(len(event_list)):
        if random.random() < event_probabilities[i]:
            event_list[i](state)


def getCommand(user_input):
    return command_dict[user_input]

def handleState(state):
    if state.thirst_current >= state.thirst_max:
        print("You've died of thirst!")
        return True
    if state.thirst_current >= 4:
        print("You're thirsty.")
    if state.tiredness_current >= state.tiredness_max:
        print("Your camel has died of exhaustion!")
        return True
    if state.tiredness_current >= 5:
        print("Your camel is starting to feel tired.")
    if state.distance_traveled - state.distance_natives <= 0:
        print("The natives have caught you!")
        return True
    if state.distance_traveled - state.distance_natives <= 15:
        print("The natives are getting close!")
    if state.distance_traveled > state.distance_max:
        print("You've made it across the Desert! With a camel to boot!")
        return True
    return False

class State:
    distance_traveled = 0
    distance_max = 200
    thirst_current = 0
    thirst_max = 6
    tiredness_current = 0
    tiredness_max = 8
    thirst_canteen = 10
    thirst_canteen_max = 10
    distance_natives = -20

    def __init__(self,distance,thirst,tiredness,canteen,natives):
        self.distance_total = distance
        self.thirst_max = thirst
        self.tiredness_max = tiredness
        self.thirst_canteen = canteen
        self.distance_natives = -natives

def main(argv):
    state = State(200,6,8,10,20)
    done = False
    
    while not done:
        getCommand(getInput())(state)
        done = handleState(state)
    
main(sys.argv)




    