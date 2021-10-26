import random



class Game:
    def __init__(self, player_name):
        
        #the user's name
        self.player_name = player_name
        
        #list of names specified by the user later in the game
        self.my_names = None
        
        #the actual one name randomly chosen from the player's list
        self.partner_name = None
        
        #dwellings list randomly chosen by the machine
        dwellings_dict = {1: 'tent for 3 close friends',
                     2: 'Italian mansion by the frozen river',
                     3: 'nomadics tipi with 4 bedrooms',
                     4: '3 stars root cellar',
                     5: 'White House',
                     6: 'luxurious hobbit-burrow',
                     7: 'basement'}
        
        dwellings_list = list(dwellings_dict.values())
        self.dwelling = random.choice(dwellings_list)
        
        #level of craziness
        self.craziness = int
        
        #list of nums, from which one num will be chosen
        #I added additional var to make it easier to manipulate the list
        #of possible number of kids
        self.nums_kids = list(range(1, 21))
        
        #here is the final one num of how many kids
        #chosen on the base of the craziness level
        self.kid = None
        
        
    def get_name(self):
        print(f"\nWell, {self.player_name}, type in the names of your closest friends of the opposite sex\n(name name ...)")
            
            
        self.my_names = input()
        self.my_names = list(map(str, self.my_names.split()))
        self.partner_name = random.choice(self.my_names)

            
    def get_craziness(self):
        print(f"{self.player_name}, how would you describe the level of"
                " your craziness in the scale from 0 to 100? I rely on your honesty!")
        self.craziness = int(input())

                  
    def get_kids(self):
             
        mid = len(self.nums_kids) // 2
        left = self.nums_kids[:mid]
        right = self.nums_kids[mid:]
        quarter = len(left) // 2
        quarter_1 = left[:quarter]
        quarter_2 = left[quarter:]
        quarter_3 = right[:quarter]
        quarter_4 = right[quarter:]
            
        while True:
            self.get_craziness()
            
            try:
                self.craziness = int(self.craziness)
                if self.craziness not in list(range(0,101)):
                    print("Not a valid number.\nDon't be that crazy, try again!\n")
                    continue
            except ValueError:
                continue
                
            if 0 <= self.craziness < 25:
                self.kid = random.choice(quarter_1)
            elif 25 <= self.craziness < 50:
                self.kid = random.choice(quarter_2)
            elif 50 <= self.craziness < 75:
                self.kid = random.choice(quarter_3)
            else:
                self.kid = random.choice(quarter_4)
            
            return self.kid
    
    
    def play(self):
        self.get_name()
        print("\nGreat! I already know something about you.")
        self.get_kids()
        print("Let's see what's in your brightest future.\n")
        print(f"{self.player_name}, you'll marry {self.partner_name}. You'll live in a/an {self.dwelling}."
              f" You'll have {self.kid} kid(s).")
        
                    
                    
                    
def main_code():
    print("Hello! What's your name?")
    player_name = input()
    print(f"Welcome, {player_name}! The Game 'Life is Random' provides you"
          " with the real life experience and shows you how much you can"
          " predict in your life.\nNONE!\nGood luck!")
    
    while True:
        print("Ready? Type 'yes' or 'quit' if scared.")
        user_choice = input()
        
        if user_choice.lower().startswith("q"):
            print("Bye!!!")
            break
            
        try:
            user_choice = str(user_choice)
            if user_choice.lower() != "yes":
                continue
        except ValueError:
            continue
            
        if user_choice.lower() == "yes":
            
            my_game = Game(player_name)
            my_game.play()
            
        print("How about another?")
        
main_code()
