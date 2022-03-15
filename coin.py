import random 
import time


cpu_1_head_wins = 0
cpu_2_tails_wins = 0

   
    #coin position
coin_positions = ['heads','tails']
def coin_landing_position(coin_positions):
    return (random.choice(coin_positions))
        
    
    #add points to play
flipped_coin = coin_landing_position(coin_positions)

if flipped_coin == 'heads':
    cpu_1_head_wins+=1
    print(cpu_1_head_wins)

else:
    cpu_2_tails_wins+=1
    print(cpu_2_tails_wins)


print(f'The coin landed on {flipped_coin}!')  



coin_landing_position(coin_positions)  
    #while loop 

while True:
    #Counter for wins player vs cpu
    if cpu_1_head_wins != 10 and cpu_2_tails_wins != 10:
        
        
             #coin position
        coin_positions = ['heads','tails']
        def coin_landing_position(coin_positions):
            return (random.choice(coin_positions))

         #add points to play
        flipped_coin = coin_landing_position(coin_positions)

        if flipped_coin == 'heads':
            cpu_1_head_wins+=1
            

        else:
            cpu_2_tails_wins+=1
            

        print(f"cpu 1 score is {cpu_1_head_wins}")
        print(f"cpu 2 score is  {cpu_2_tails_wins}")
        print(f'The coin landed on {flipped_coin}!')  
    
    else:
        break