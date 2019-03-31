{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please pick a marker \"X\" or \"o\"X\n",
      "Please enter a number1\n"
     ]
    }
   ],
   "source": [
    "player1 = input('Please pick a marker \"X\" or \"o\"')\n",
    "position = int(input('Please enter a number'))\n",
    "board = ['#','X','X','X','_','_','_','_','_','_']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clear_output():\n",
    "    print(\"\\n\"*100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_board(board):\n",
    "    \n",
    "    print(board[7]+'|'+board[8]+'|'+board[9])\n",
    "    print(board[4]+'|'+board[5]+'|'+board[6])\n",
    "    print(board[1]+'|'+board[2]+'|'+board[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def player_input():\n",
    "    marker = ''\n",
    "    \n",
    "    while marker != 'X'and marker != 'O':\n",
    "        marker = input('X or O you dummy...')\n",
    "    \n",
    "        \n",
    "    player1 = marker\n",
    "    \n",
    "    if player1 == 'X':\n",
    "        player2 = 'O'\n",
    "    else:\n",
    "        player2 = 'X'\n",
    "    \n",
    "    return('Player one is \"{}\", and player two is \"{}\"' .format(player1,player2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "def place_marker(board, marker, position):\n",
    "    board[position] = marker"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def win_check(board, mark):\n",
    "    \n",
    "    return (board[1] == mark and board[2] == mark and board[3] == mark or\n",
    "    board[4] == mark and board[5] == mark and board[6] == mark or\n",
    "    board[7] == mark and board[8] == mark and board[9] == mark or\n",
    "    board[1] == mark and board[5] == mark and board[9] == mark or\n",
    "    board[3] == mark and board[5] == mark and board[7] == mark or\n",
    "    board[1] == mark and board[4] == mark and board[7] == mark or\n",
    "    board[2] == mark and board[5] == mark and board[8] == mark or\n",
    "    board[3] == mark and board[6] == mark and board[9] == mark)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "def choose_first(player1,player2):\n",
    "    player1 = 0\n",
    "    player2 = 1\n",
    "    random.randint(0,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'player2' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-46-f3d43ffad647>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mchoose_first\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mplayer1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mplayer2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'player2' is not defined"
     ]
    }
   ],
   "source": [
    "choose_first(player1,player2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
