import sys, random



def player():
    if ui == "q":
        sys.exit()
    
    elif ui == "r":
        print(f"You picked {ui} (Rock)!")
        
    elif ui == "p":
        print(f"You picked {ui} (Paper)!")
        
    elif ui == "s":
        print(f"You picked {ui} (Scissor)")



def comp():
    computer = random.choice(["r", "p", "s"])
    if computer == "r":
        computer = "r"
        print(f"Computer selected: {computer} (Rock)")
    
    elif computer == "p":
        computer = "p"
        print(f"computer selected: {computer} (Paper)")
    
    elif computer == "s":
        computer = "s"
        print(f"computer selected: {computer} (Scissor)")
        
    return computer

def lose():
    print("You Lose!")

def win():
    print("You Won!")
    
def ties():
    print("Tie!")




def state(ui, comp):
    global wins, losses, tie
    if ui == "r" and computer == "p" : 
        lose()
        losses += 1
    
    elif ui == computer:
        ties()
        tie +=1
    
    elif ui == "r" and computer == "s":
        wins += 1
        win()
        
    elif ui == "p" and computer == "s":
        losses += 1
        lose()
    
    elif ui == "p" and computer == "r":
        win()
        wins+=1

    elif ui == "s" and computer == "r":
        lose()
        losses+=1
    
    elif ui == "s" and computer == "p":
        win()
        wins +=1 
           
    


            
print(f"Rock Paper Scissor!")
wins = 0
losses = 0
tie = 0

while True:
    print(f"\nSelect your choices:\n r(Rock) p(Paper) s(Scissor) q(Quit)")
    ui = str(input(">"))
    final = ui.lower()

    
    player()
    print("\n")
    computer = comp()
    print("\n")
    state(ui, computer)
    print(f" wins: {wins}\n losses: {losses}\n tie: {tie}")
    
        
    