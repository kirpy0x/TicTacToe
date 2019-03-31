#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


def display_board(board):
    print("\n"*10)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


def player_input():
    marker = ''
    
    while marker != 'X'and marker != 'O':
        marker = input('Pick a marker "X" or "o" ').upper()
    
        
    player1 = marker
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
    return('Player one is "{}", and player two is "{}"' .format(player1,player2))


# In[3]:


def place_marker(board, marker, position):
    board[position] = marker


# In[4]:


def win_check(board, mark):
    
    return (board[1] == mark and board[2] == mark and board[3] == mark or
    board[4] == mark and board[5] == mark and board[6] == mark or
    board[7] == mark and board[8] == mark and board[9] == mark or
    board[1] == mark and board[5] == mark and board[9] == mark or
    board[3] == mark and board[5] == mark and board[7] == mark or
    board[1] == mark and board[4] == mark and board[7] == mark or
    board[2] == mark and board[5] == mark and board[8] == mark or
    board[3] == mark and board[6] == mark and board[9] == mark)


# In[5]:


import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'player2'
    else:
        return 'player1'


# In[6]:


def space_check(board,position):
    return board[position] == '_'


# In[7]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[8]:


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Please enter a number from 1 to 9 : '))
    return position

    


# In[9]:


def replay():
    return input("Wanna play again? : ").lower().startswith('y')


# In[ ]:



print('Welcome to Tic Tac Toe')


# WHILE LOOP TO KEEP RUNNING THE GAME

while True:
    
    # play game
    
    # Set everything up: board, who's first, choose markers
    board = ['#','_','_','_','_','_','_','_','_','_']
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready? y or n ').lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    
    
    #game play
    
    while game_on:
        if turn == 'Player1':
            
            # show board
            display_board(board)
            
            #choose position
            position = player_choice(board)
            
            #place marker on position
            place_marker(board, player1_marker, position)
            
            #check win
            if win_check(board, player1_marker):
                display_board(board)
                print("Player 1 you win!")
                game_on = False
            else:
            
            #check tie
                if full_board_check(board):
                
                    display_board(board)
                    print("It's a tie!!! Losers!")
                    game_on = False
                else:
                    turn = 'Player2'
                    
            
            #next players turn
            turn = 'Player2'
    
    #player two turn
    
        else:
            turn = 'Player2'
                # show board
            display_board(board)
            
            #choose position
            position = player_choice(board)
            
            #place marker on position
            place_marker(board,player2_marker,position)
            
            #check win
            if win_check(board, player2_marker):
        
                display_board(board)
                print("Player 2 you win!")
                game_on = False
            else:
             
            
            #check tie
                if full_board_check(board):
                
                    display_board(board)
                    print("It's a tie!!! Losers!")
                    game_on = False
                else:
                    turn = 'Player1'
                    
            
            #next players turn
            turn = 'Player1'
    else:
        if replay() = True
    
    
    #player two turn
    
    
    
    
    
    
    
    
    
    
    


# 

# In[ ]:





# In[ ]:




