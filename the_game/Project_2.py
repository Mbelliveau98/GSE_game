#GSE "PAPER 2"

import random
import os
money = 0




def unethic (ch, con):
    global money
    if ch == 1:
        print ('You found a loophole!')
    else:
        print ('Your practices have resulted in a net loss')
        money -= con

def ethic (ch, con):
    global money
    if ch == 1:
        print('Your environmental consciousness paid off!')
        money += con
    else:
        print ('Better luck next time!')

def neutral (ch, con):
    global money
    if ch == 1:
        print ('Balanced, as all things should be!')
        money += con
        
    elif ch == 2:
        print ('maybe you should have picked the extreme...?')
        money -= con
        
    else:
        print ('Nothing happened!') 
      
def process_ans ():
    global money
    global ethics 
    
    chance = random.randint(1,3)
    #Chances: 2/3 bad things, neutral: 1/3 all, Good:1/3 gain

    conseq = random.randint(1,3)

    ans = input ('What do you do?')
    
    
    if ans == 'A' :
        money += 4
        unethic(chance, conseq)
        
    elif ans == 'B':
        money += 3
        neutral(chance, conseq)
        
    elif ans == 'C':
        money += 2
        ethic(chance, conseq)
        
    else:
        print ('Please pick a valid option')
        return False

    ethics[ans] += 1
    
    return True
        
def end_result():
    max_ethic = ''
    max_pts = 0
    
    for e in ethics:
        if ethics[e] >= max_pts:
            max_pts = ethics[e]
            max_ethic = e

            
    if max_ethic == 'A':
        print ('Bad things happen')
    elif max_ethic == 'B':
         print ('Things happen')
    elif max_ethic == 'C':
         print ('Good things happen')

'''

////////////// Game Variables //////////

'''


ethics ={'A': 0 ,'B': 0,'C':0}

#Round: Scenario + Choices

choice = ''
choice_list = []

#questions[i] : answers[]
curr_ques = ''

one_round = []
rounds = []

quest_list = []

game = "game.txt"
file = open(game, "r")
#game.txt, watch: office space, quiet place, moon, mute



'''

////////////// The Game //////////

'''



for line in file:
    
    if line[0] == '\n':
        continue

    elif line[0] == ':':
        choice = line
        if len(choice_list) < 3:
            choice_list.append(choice)
        continue

    curr_ques = line
    quest_list.append(curr_ques)
    rounds.append(choice_list)
    
            
file.close()

for q in range(len(quest_list)):
  
    print("\n%s \n" %quest_list[q])

    for a in rounds[q]:
        print (a)
    
    while not process_ans(): #loop until valid
        process_ans()
    print('Profit: $ %d' %money)
        

print('\n')
end_result()
print('Total Profit: $ %d' %money)


