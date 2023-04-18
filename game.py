from microbit import *
import radio

radio.on() # Turn on the bluetooth function of the card
radio.config(channel=42) # Select the channel 42 of the bluetooth module

rock = Image( # Image of the rock on the card
        '06660:'
        '69996:'
        '69996:'
        '69996:'
        '06660')
paper = Image( # Image of the paper on the card
        '09900:'
        '09990:'
        '09990:'
        '09990:'
        '09990')
scissors = Image( # Image of the scissors on the card
        '99009:'
        '99090:'
        '00900:'
        '99090:'
        '99009')
lose = Image( # Image of the defeat on the card
        '97079:'
        '79797:'
        '07970:'
        '79797:'
        '97079')
win = Image( # Image of the victory on the card
        '98889:'
        '99999:'
        '09990:'
        '00900:'
        '09990')
tie  = Image( # Image of the draw on the card
        '09990:'
        '97079:'
        '90009:'
        '97079:'
        '09990')

#######################################################
# Introduction animation at the beginning of the game #
#######################################################

display.show(Image(
        "00000:"
        "00000:"
        "00900:"
        "00000:"
        "00000"))
sleep(200)
display.show(Image(
        "00000:"
        "00700:"
        "07970:"
        "00700:"
        "00000"))
sleep(200)
display.show(Image(
        "00700:"
        "07970:"
        "79997:"
        "07970:"
        "00700"))
sleep(200)
display.show(Image(
        "07970:"
        "79997:"
        "99999:"
        "79997:"
        "07970"))
sleep(200)
display.show(Image(
        "79997:"
        "99999:"
        "99999:"
        "99999:"
        "79997"))
sleep(200)
display.show(Image(
        "99999:"
        "99999:"
        "99999:"
        "99999:"
        "99999"))
sleep(200)
display.show(Image(
        "88888:"
        "88888:"
        "88888:"
        "88888:"
        "88888"))
sleep(200)
display.show(Image(
        "77777:"
        "77777:"
        "77777:"
        "77777:"
        "77777"))
sleep(200)
display.show(Image(
        "66666:"
        "66666:"
        "66666:"
        "66666:"
        "66666"))
sleep(200)
display.show(Image(
        "55555:"
        "55555:"
        "55555:"
        "55555:"
        "55555"))
sleep(200)
display.show(Image(
        "44444:"
        "44444:"
        "44444:"
        "44444:"
        "44444"))
sleep(200)
display.show(Image(
        "33333:"
        "33333:"
        "33333:"
        "33333:"
        "33333"))
sleep(200)
display.show(Image(
        "22222:"
        "22222:"
        "22222:"
        "22222:"
        "22222"))
sleep(200)
display.show(Image(
        "11111:"
        "11111:"
        "11111:"
        "11111:"
        "11111"))
sleep(200)
display.show(Image(
        "00000:"
        "00000:"
        "00000:"
        "00000:"
        "00000"))

while True:
    # Choice: rock
    if button_a.get_presses():
        display.show(rock) # Displays the image of the rock
        radio.send("rock") # Sends the player's choice
        sleep(2500)
        display.clear()
        opponent_move = radio.receive()# Receives the opponent's choice

        if opponent_move == "scissors": # Opponent choice: scissors
            display.show(win) # Displays the image of the victory
            sleep(2500)
            display.clear()
            break
        elif opponent_move == "paper": # Opponent choice: paper
            display.show(lose) # Displays the image of the defeat
            sleep(2500)
            display.clear()
            break
        elif opponent_move == "rock": # Opponent choice: rock
            display.show(tie) # Affiche l'image de l'égalité
            sleep(2500)
            display.clear()
            break

    # Choice: paper
    elif button_b.get_presses():
        display.show(paper) # Displays the image of the paper
        radio.send("paper") # Sends the player's choice
        sleep(2500)
        display.clear()
        opponent_move = radio.receive()# Receives the opponent's choice

        if opponent_move == "rock": # Opponent choice: rock
            display.show(win) # Displays the image of the victory
            sleep(2500)
            display.clear()
            break
        elif opponent_move == "scissors": # Opponent choice: scissors
            display.show(lose) # Displays the image of the defeat
            sleep(2500)
            display.clear()
            break
        elif opponent_move == "paper": # Opponent choice: paper
            display.show(tie) # Displays the image of the draw
            sleep(2500)
            display.clear()
            break

    # Choice: scissors
    elif accelerometer.was_gesture('shake'):
        display.show(scissors) # Displays the image of the scissors
        radio.send("scissors") # Sends the player's choice
        sleep(2500)
        display.clear()
        opponent_move = radio.receive()# Receives the opponent's choice

        if opponent_move == "paper": # Opponent choice: paper
            display.show(win) # Displays the image of the victory
            sleep(2500)
            display.clear()
            break
        elif opponent_move == "rock": # Opponent choice: rock
            display.show(lose) # Displays the image of the defeat
            sleep(2500)
            display.clear()
            break
        elif opponent_move == "scissors": # Opponent choice: scissors
            display.show(tie) # Displays the image of the draw
            sleep(2500)
            display.clear()
            break
