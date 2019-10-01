from datetime import date
import traceback as trace
import re
import random as rand

class srs:
    def __init__(self, fname):
        try:
            if str(fname).endswith(".txt"):
                self.fname = fname
            else:
                raise NameError()
            self.deck = {
                "name": "",
                "topic": "",
                "date of creation": 0 
            }
        except NameError:
            print("ERROR: Missing .txt extension")
            print("ERROR: The file name passed as argument is not valid")
            print("ERROR...The program execution has been stopped")
        except:
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")
        
    def insert(self, name, topic):
        try:
            flag = True
            check = re.compile(r"NAME: " + name + r"\n")
            with open(self.fname, "r") as f:
                for line in f.readlines():
                    if re.match(check, line) != None:
                        flag = False
                        break

            if flag == True:
                self.deck.clear()
                self.deck.update({"name" : str(name)})
                self.deck.update({"topic" : str(topic)})
                self.deck.update({"date of creation" : date.today().isoformat()})
                self.__update()
            else:
                print("The deck you are attempting to create already exists")
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")

    def __update(self): #write well the data on the file
        try:
            name = ""
            topic = ""
            date_of_creation = 0


            with open(self.fname, "a") as f:
                f.write("CARDS: ")
                for key, value in zip(self.deck.keys(), self.deck.values()): 
                    if key == "name":
                        name = value
                    elif key == "topic":
                        topic = value
                    elif key == "date of creation":
                        date_of_creation = value
                    else:
                        f.write(key + " -> " + value + ", ")
                
                f.write("\n")
                f.write("NAME: " + name + "\n")
                f.write("TOPIC: " + topic + "\n")
                f.write("DATE OF CREATION: " + str(date_of_creation) + "\n")
                f.write("------------------- END DECK ---------------------")
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")

    def add(self, deck, front, back): #add the deck parameter and set it
        try:
            check_name = re.compile(r"NAME: " + deck + r"\n")
            check_card = re.compile(front + r" -> \w+")
            flag = False
            lines = []
            cards = []
            count = 0

            if isinstance(deck, str) == False or isinstance(front, str) == False or isinstance(back, str) == False:
                raise ValueError()        

            with open(self.fname, "r") as f:
                lines = f.readlines()

            for index in range(0, len(lines)):
                if re.match(check_name, lines[index]) != None:
                    flag = True
                    cards = lines[index - 1].replace("CARDS: ", "").replace("\n", "").split(", ")
                    break
            
            if flag == True:
                for card in cards:
                    if re.match(check_card, card) != None:
                        flag = False
                        break
                
                if flag == True:
                    if cards[0] != "":
                        cards.append(front + " -> " + back)
                    else:
                        cards[0] = front + " -> " + back

                    for index in range(0, len(lines)):
                        if re.match(check_name, lines[index]) != None:
                            lines[index - 1] = ", ".join(cards)
                            lines[index - 1] = "CARDS: " + lines[index - 1] + "\n"
                            print(lines[index - 1])
                            break

                    with open(self.fname, "w") as f:    
                        f.writelines(lines)
                else:
                    print("The card you are attempting to add already exists")
            else:
                print("The deck you selected has not been found in the collection")
        except ValueError:
            print("ERROR: The data type of your arguments is not valid")
            print("ERROR...The program execution has been stopped")           
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")
        
    def remove(self, deck, front): #add the deck parameter and set it, also remove from file
        try:
            check_name = re.compile(r"NAME: " + deck + r"\n")
            check_card = re.compile(front + r" -> \w+")
            flag = False
            lines = []
            cards = []

            with open(self.fname, "r") as f:
                lines = f.readlines()

            for index in range(0, len(lines)):
                if re.match(check_name, lines[index]) != None:
                    flag = True
                    cards = lines[index - 1].replace("CARDS: ", "").replace("\n", "").split(", ")
                    break
            
            if flag == True:
                flag = False
                for index in range(0, len(cards)):
                    if re.match(check_card, cards[index]) != None:
                        flag = True
                        cards.pop(index)
                        break
                
                if flag == True:
                    for index in range(0, len(lines)):
                        if re.match(check_name, lines[index]) != None:
                            lines[index - 1] = ", ".join(cards)
                            lines[index - 1] = "CARDS: " + lines[index - 1] + "\n"
                            print(lines[index - 1])
                            break
                
                    with open(self.fname, "w") as f:
                        f.writelines(lines)
                else:
                    print("The card you wanted to remove has not been found")
            else:
                print("The deck you selected has not been found in the collection")
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")

    def delete(self, deck): #remove from file
        try:
            check_name = re.compile(r"NAME: " + deck + r"\n")
            flag = False
            lines = []
            point1 = 0
            point2 = 0

            with open(self.fname, "r") as f:
                lines = f.readlines()

            for index in range(0, len(lines)):
                if re.match(check_name, lines[index]) != None:
                    flag = True
                    point1 = index - 1
                    point2 = index + 3
                    break

            if flag == True:
                while point2 >= point1:
                    lines.pop(point2)
                    point2 -= 1

                with open(self.fname, "w") as f:
                    f.writelines(lines)
            else:
                print("The deck you selected has not been found in the collection")
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")
    
    def get(self, deck): #get from file
        try:
            check_name = re.compile(r"NAME: " + deck + r"\n")
            flag = False
            lines = []
            get = []
            point1 = 0
            point2 = 0

            with open(self.fname, "r") as f:
                lines = f.readlines()
            
            for index in range(0, len(lines)):
                if re.match(check_name, lines[index]) != None:
                    flag = True
                    point1 = index - 1
                    point2 = index + 3
                    break
            
            if flag == True:   
                while point1 <= point2:
                    get.append(lines[point1])
                    point1 += 1
                return get
            else:
                print("The deck you selected has not been found in the collection")
                return None
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")
        
    def start(self, topic):
        try:
            check_topic = re.compile(r"TOPIC: " + topic + r"\n")
            flag = False
            lines = []
            cards = []
            random = 0
            response = ""

            with open(self.fname, "r") as f:
                lines = f.readlines()
            
            for index in range(0, len(lines)):
                if re.match(check_topic, lines[index]):
                    flag = True
                    cards = lines[index - 2].replace("CARDS: ", "").split(", ")
                    break
            
            if flag == True:
                for index in range(0, len(cards)):
                    cards[index] = cards[index].split(" -> ")

                for index in range(len(cards)):
                    random = rand.randint(0, len(cards) - 1)
                    print(cards[random][0] + ": ", end = '')
                    response = input()
                    print("\n", end = '')

                    print(cards[random][1].replace("\n", ""))
                    if response.lower() == cards[random][1].lower().replace("\n", ""):
                        print("GOOD, YOU REMEMBER WELL, GO ON!")
                        print("================================")
                    else:
                        print("...I THINK YOU SHOULD STUDY MORE")
                        print("================================")
            else:
                print("The topic you selected has not been found in the collection")
        except:
            trace.print_exc()
            print("ERROR...An unexpected error has occured during the program execution")
            print("ERROR...The program execution has been stopped")