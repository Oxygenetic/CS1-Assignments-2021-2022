'''
Created on 20 Oct 2021
@author: FHentsch-Cowles24
Description:
    A game of rock-paper-scissors. Rock beats scissors, scissors beat paper, paper beats rock. At the start a menu is provided with the options to play, quit,
or check score. The user can choose between single-player against the computer or two-player against another user. Users choose their weapon (Rock, Paper,
or Scissors). If single-player, computer chooses at random. The winner is then declared and scores/total-games count is updated. The menu reappears with
options to play again, quit, or check score. Enjoy!
Log:
10/20/2021 Version 1.0 - Created program
10/21/2021 Version 2.0 - Sophisticated menu, added 2-player option
10/26/2021 Version 2.1 - Added emoji decorations, fixed tie not adding to games_played bug, reformatted comments, added .lower comforts for user
10/28/2021 Version 2.2 - Added emoji1/emoji2 variables in choice announcements
11/02/2021 Version 2.3 - Added sound to weapon selection using playsound()
11/02/2021 Version 2.4 - Added winsound.SND_ASYNC to allow sound to play in background so that it does not interrupt/delay the program
Bugs:
Features:
    - Two-player optional
    - Score and games played are counted
    - Quit option
    - User can switch between 1 and 2 player without having to restart the program, score will not be messed up
    - Emojis for visual effect
    - Not picky about capitalization in inputs
    - Plays sound prompting user to choose weapon
Last edited on 11/02/2021
'''

import random
import winsound

score1 = 0                                                                                                              #Tracks score of Player1
score2 = 0                                                                                                              #Tracks score of Player2
games_played = 0                                                                                                        #Tracks total games played since run
    
def game():
    
    global score1
    global score2
    global games_played
        
    menu = "Unanswered"                                                                                                 #Status- decides if the program will run rock-paper-scissors, quit, or show score
    valid_decisions = ["rps","quit","score"]                                                                            #Creating a list of recognisable menu options
    
    #Prompts user to use the menu
    while menu != valid_decisions:
        menu = input("🎲 Menu 🎲\n'RPS' - Play Rock-Paper-Scissors 🗿🧻✂️\n'Quit' - Quit program ❌\n'Score' - Check current score 🏆\n")
        menu = menu.lower()
        if menu == "rps":                                                                                               #Enter the game
            break
        elif menu == "quit":                                                                                            #Quit the program
            break
        elif menu == "score":                                                                                           #Check current score
            print("🏆 The Scoreboard 🏆\nPlayer1 score: " + str(score1) + "\nPlayer2 score: " + str(score2) +  "\nTotal games played: " + str(games_played) + "\n")
        else:                                                                                                           #Loops back if an unrecognisable input was given
            print("Case-sensitive.")
        
    #While the user decides to play rock-paper-scissors
    while menu == "rps":
        choices = ["rock", "paper", "scissors"]                                                                         #Creates a list of acceptable weapon choices
        modes = ["1","2"]                                                                                               #Creates a list of game modes (1 or 2 users)
        rock_emoji = "🗿"
        paper_emoji = "🧻"
        scissors_emoji = "✂️"
        
        #Prompts user to select game_mode
        mode = "Unchosen"
        while mode != modes:
            mode = input("How many users are playing? Enter '1' or '2'.\n")
            if mode == "1":
                break
            elif mode == "2":
                break
            else:
                print("Case-sensitive. Please choose.")                                                                 #Prompts user to enter a valid game_mode (from modes)
        
        #Assigns the opponent as Computer if mode 1 is chosen. (Player1 vs. Computer)
        while mode == "1":
            computer = random.choice(choices)                                                                           #Computer makes random choice
            opponent_name = "Computer"
            opponent = computer
            break
        
        #Adds sound telling user to choose their weapons and fight!
        winsound.PlaySound("C:\\Users\\fhentsch-cowles24\Downloads\WeaponSelection.wav", winsound.SND_ASYNC)            #winsound.SND_ASYNC lets audio play without halting following code
        
        #2 Player option
        player2 = "Unchosen"
        while mode == "2" and player2 != choices:                                                                       #Since 2-player mode is chosen, prompts Player2 to select weapon
            player2 = input("Player2: Rock, Paper, or Scissors?\n")
            player2 = player2.lower()
            if player2 == "rock":
                break
            elif player2 == "paper":
                break
            elif player2 == "scissors":
                break
            else:                                                                                                       #If user does not enter in an acceptable choice, loops back to prompt
                print("Your selection is case-sensitive. Please enter 'Rock', 'Paper', or 'Scissors'.")
        if mode == "2":                                                                                                 #Assigns opponent variables to Player2
            opponent_name = "Player2"
            opponent = player2
        
        
        
        #Prompts Player1 to select weapon
        player1 = "Unchosen"
        while player1 != choices: 
            player1 = input("Player1: Rock, Paper, or Scissors?\n")
            player1 = player1.lower()
            if player1 == "rock":
                break
            elif player1 == "paper":
                break
            elif player1 == "scissors":
                break
            else:                                                                                                       #If user does not enter in an acceptable choice, loops back to prompt
                print("Your selection is case-sensitive. Please enter 'Rock', 'Paper', or 'Scissors'.")
        
        #Setting announce emojis for each player's choice
        if player1 == "rock":
            emoji1 = rock_emoji
        if player1 == "paper":
            emoji1 = paper_emoji
        if player1 == "scissors":
            emoji1 = scissors_emoji
        if opponent == "rock":
            emoji2 = rock_emoji
        if opponent == "paper":
            emoji2 = paper_emoji
        if opponent == "scissors":
            emoji2 = scissors_emoji
        #Choice announcements
        print("Player1 chose " + player1 + emoji1)                                                                               #Announces PLayer1's chosen weapon
        print(opponent_name + " chose " + opponent + emoji2)                                                                     #Announces Opponent's chosen weapon
        
        #Player win scenarios - Sets winner to player1 and loser to opponent (computer or player2)
        if (player1 == "rock" and opponent == "scissors") or (player1 == "scissors" and opponent == "paper") or (player1 == "paper" and opponent == "rock"):
            winner = "Player1"
            loser = opponent_name
            winning_choice = player1
            losing_choice = opponent
            score1 = score1 + 1                                                                                         #Adds to Player1's score of games won
        
        #Computer win scenarios - Sets winner to opponent (computer or player2) and loser to player1
        elif (opponent == "rock" and player1 == "scissors") or (opponent == "scissors" and player1 == "paper") or (opponent == "paper" and player1 == "rock"):
            winner = opponent_name
            loser = "Player1"
            winning_choice = opponent
            losing_choice = player1
            if mode == "2":                                                                                             #Adds to Player2's score if game mode is 2 (two-player)
                score2 = score2 + 1 
        
        #If both the player and computer have the same choice
        else:
            print("Player1 and " + opponent_name + " both chose " + player1 + "! The game is a tie.\n")
            games_played = games_played + 1
            game()                                                                                                      #Loops back to the menu prompts, asks user if they would like to play (again)
        
        #Announces results of the game
        print(winner + " beat " + loser + ". " + winning_choice + " beats " + losing_choice + ".\n")
        games_played = games_played + 1                                                                                 #Adds to count of games played
        game()                                                                                                          #Loops back to the menu prompts, asks user if they would like to play (again)
    
    #When the user decides to not play; terminate the program
    while menu == "quit": 
        print("❌ You chose not to play. Ending program. ❌")
        quit()

if __name__ == '__main__':
    game()