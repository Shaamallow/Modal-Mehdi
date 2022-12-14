import time
import pygame
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# ENABLE DEBUGGING

debug = True

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Modal Mehdi')
clock = pygame.time.Clock()

# CHANGE TIME VARIABLE HERE
time_between_letters = 1000
time_letter_visible = 500


def text_objects(text, font, color=black):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

##### HELP MENU STARTS HERE #####

# opens up a new page with the help menu
# Help is written on top of the screen and there is a back button on the bottom of the screen to go back to the intro page
# the button is a rectangle with black text in it and a black border
# the button is on the bottom of the screen


def help_menu():

    help = True

    while help:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if escape key is pressed, quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("HELP", largeText)
        # help text is written on top of the screen
        TextRect.center = ((display_width/2), (100))
        gameDisplay.blit(TextSurf, TextRect)

        # create a back button on the bottom of the screen
        # the button will be a rectangle with black text in it and a black border
        # the button will be on the bottom of the screen

        # create a back button
        back_button = pygame.Rect(300, 500, 200, 50)
        pygame.draw.rect(gameDisplay, black, back_button, 2)
        back_button_text = pygame.font.Font('freesansbold.ttf', 30)
        back_button_text_surf, back_button_text_rect = text_objects(
            "BACK", back_button_text)
        back_button_text_rect.center = (
            (back_button.left + 100), (back_button.top + 25))
        gameDisplay.blit(back_button_text_surf, back_button_text_rect)

        # check if the mouse is over the back button
        if back_button.collidepoint(pygame.mouse.get_pos()):
            # mousseDOWN event
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is over the back button and the mouse is clicked, go back to the intro page
                help = False

        # rules are "You have to remember the order of the letters and press them in the correct order afterwards"
        # "a random amount of letters will appear on the screen"
        # "if you press the wrong letter, you lose"
        # "the a number of black dots will appear with a specific timing in between them"
        # "you need to remember the timing of the dots and press the space bar at the right time when a interrogative mark appears"
        # the rules are written on the screen
        # the rules are written in the middle of the screen
        # the rules are written in a font size of 15
        # the rules are written in black
        # rules are written on 2 lines to look better

        # create a rules text
        rules_text = pygame.font.Font('freesansbold.ttf', 15)
        rules_text_surf, rules_text_rect = text_objects(
            "A random amount of letters will appear on the screen", rules_text)
        rules_text_rect.center = ((display_width/2), (display_height/2 - 100))
        gameDisplay.blit(rules_text_surf, rules_text_rect)

        rules_text2_surf, rules_text2_rect = text_objects(
            "You have to remember letters and their order", rules_text)
        rules_text2_rect.center = ((display_width/2), (display_height/2 - 50))
        gameDisplay.blit(rules_text2_surf, rules_text2_rect)

        rules_text3_surf, rules_text3_rect = text_objects(
            "Then dots will appear on the screen at same letter's frequency", rules_text)
        rules_text3_rect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(rules_text3_surf, rules_text3_rect)

        rules_text4_surf, rules_text4_rect = text_objects(
            "one of the dots will be a question mark", rules_text)
        rules_text4_rect.center = ((display_width/2), (display_height/2 + 50))
        gameDisplay.blit(rules_text4_surf, rules_text4_rect)

        rules_text5_surf, rules_text5_rect = text_objects(
            "each dot represent a letter in the said order", rules_text)
        rules_text5_rect.center = ((display_width/2), (display_height/2 + 100))
        gameDisplay.blit(rules_text5_surf, rules_text5_rect)

        rules_text6_surf, rules_text6_rect = text_objects(
            "you need to input the letter corresponding to the question mark ", rules_text)
        rules_text6_rect.center = ((display_width/2), (display_height/2 + 150))
        gameDisplay.blit(rules_text6_surf, rules_text6_rect)

        pygame.display.update()
        clock.tick(15)

##### HELP MENU ENDS HERE #####


def menu():

    # Variable to keep the game running and make it possible to implement a debug mode
    # Otherwise could be replaced by a while True loop

    intro = True

    while intro:

        # EVENT HANDLING

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if escape key is pressed, quit the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # GAME DISPLAY

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("Memory Test", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        # create a starting button and a help button on the bottom of the screen
        # both button will be rectangles with text in them
        # both button will be the same size with a black border and black text
        # the starting button will be a little on the left and the help button will be a little on the right

        # create a starting button
        start_button = pygame.Rect(100, 500, 200, 50)
        pygame.draw.rect(gameDisplay, black, start_button, 2)
        start_button_text = pygame.font.Font('freesansbold.ttf', 30)
        start_button_text_surf, start_button_text_rect = text_objects(
            "START", start_button_text)
        start_button_text_rect.center = (
            (start_button.left + 100), (start_button.top + 25))
        gameDisplay.blit(start_button_text_surf, start_button_text_rect)

        # create a help button
        help_button = pygame.Rect(500, 500, 200, 50)
        pygame.draw.rect(gameDisplay, black, help_button, 2)
        help_button_text = pygame.font.Font('freesansbold.ttf', 30)
        help_button_text_surf, help_button_text_rect = text_objects(
            "HELP", help_button_text)
        help_button_text_rect.center = (
            (help_button.left + 100), (help_button.top + 25))
        gameDisplay.blit(help_button_text_surf, help_button_text_rect)

        # create a Results button to display the results of the game (csv file) on top of the screen (top right)
        # the results button will be a rectangle with text in it
        # the results button will be the same size with a black border and black text
        # the results button will be on the top right of the screen

        # create a results button
        results_button = pygame.Rect(550, 50, 200, 50)
        pygame.draw.rect(gameDisplay, black, results_button, 2)
        results_button_text = pygame.font.Font('freesansbold.ttf', 30)
        results_button_text_surf, results_button_text_rect = text_objects(
            "RESULTS", results_button_text)
        results_button_text_rect.center = (
            (results_button.left + 100), (results_button.top + 25))
        gameDisplay.blit(results_button_text_surf, results_button_text_rect)

        # check if the mouse is over the starting button or click on letter A on the keyboard
        # if so, start the game
        if start_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN or pygame.key.get_pressed()[pygame.K_a]:
                # if the mouse is over the starting button, the game starts
                # possible to go back to menu by pressing escape
                game()
        # check if the mouse is over the help button
        if help_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is over the help button, the help menu is displayed
                # possible to go back to menu by clicking on the back button or pressing escape
                help_menu()
        # check if the mouse is over the results button
        if results_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is over the results button, the results menu is displayed
                # possible to go back to menu by clicking on the back button or pressing escape
                results_screen()

        # update screen
        pygame.display.update()
        clock.tick(15)


def game():

    # get user ID by reading the csv file

    userID = get_userID()

    # repeat the game automatically for 10 minutes

    start_time = time.time()
    end_time = start_time + 600

    # number of try in the same session
    ID_try = 1

    while time.time() < end_time:

        # Timeline of the game

        random_letters, number_of_dots, gameExit = letter_flash()

        # Verify if no interrupt of the game process
        if gameExit:
            return None

        gameExit = dot_flash(number_of_dots)

        if gameExit:
            return None

        # get user input used for statistics
        user_input, gameExit, time_input = letter_input()

        if gameExit:
            return None

        # check if the user input is correct
        # position isn't an accurate naming, it's the distance between the letter input
        # and the letter that should have been input (algebraic distance based on the position inside the list)
        position = letter_comparison(
            random_letters, user_input, number_of_dots)

        if position != None:
            # if the user input is incorrect, do not save results
            logs(userID, random_letters, user_input,
                 position, time_input, number_of_dots, ID_try)
            write_results(position)

        ID_try += 1


def letter_flash():

    # generate a random integer between 6 and 10
    # this will be the number of letters that will appear on the screen
    # the number of letters will be the same as the number of letters that will be pressed afterwards
    number_of_letters = random.randint(6, 10)

    # create a list of letters
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
               "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # chose without duplicates random letters 
    # from the list of letters
    # chose exactly number_of_letters letters

    random_letters = random.sample(letters, number_of_letters)

    # generate a random integer lower than the number of letters
    # this will be the number of black dots that will appear on the screen
    number_of_dots = random.randint(0, number_of_letters-1)

    # letter will stay on screen for 0.5 seconds

    letterExit = False

    current_time = pygame.time.get_ticks()
    cooldown = False

    i = 0  # current random letter

    gameDisplay.fill(white)
    pygame.display.update()

    goBackToMenu = False

    while not letterExit:

        for event in pygame.event.get():

            # forcequit window of game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                # if escape key is pressed, go back to menu
                if event.key == pygame.K_ESCAPE:
                    letterExit = True
                    goBackToMenu = True

        # display the letters
        # letters will be on display for 2 seconds
        # the letters will be displayed in the order of the list random_letters
        # the letters will be displayed one after the other
        # the letters will be displayed in the middle of the screen

        # display the letters

        now = pygame.time.get_ticks()

        if (now - current_time > time_between_letters) and (i < number_of_letters) and (not cooldown):
            gameDisplay.fill(white)
            letter_text = pygame.font.Font('freesansbold.ttf', 100)
            letter_text_surf, letter_text_rect = text_objects(
                random_letters[i], letter_text)
            letter_text_rect.center = ((display_width/2), (display_height/2))
            gameDisplay.blit(letter_text_surf, letter_text_rect)
            current_time = now
            i += 1
            cooldown = True
            pygame.display.update()
            clock.tick(60)

        if (now - current_time > time_letter_visible) and cooldown:
            gameDisplay.fill(white)
            cooldown = False
            pygame.display.update()
            clock.tick(60)

        if (i == number_of_letters) and now-current_time > time_between_letters:
            letterExit = True

    if debug:

        print(random_letters)
        print(number_of_dots)
        print(goBackToMenu)

    return (random_letters, number_of_dots, goBackToMenu)


def dot_flash(number_of_dots):

    # make number_of_dots black dots appear on the screen
    # the dots will appear in the middle of the screen at the same frequency than the letters
    # the dots will be displayed for the same time as the letters

    i = 0  # current dot

    gameDisplay.fill(white)
    pygame.display.update()

    current_time = pygame.time.get_ticks()
    cooldown = False
    dotExit = False

    goBackToMenu = False

    while not dotExit:

        for event in pygame.event.get():

            # forcequit window of game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                # if escape key is pressed, go back to menu
                if event.key == pygame.K_ESCAPE:
                    dotExit = True
                    goBackToMenu = True

        # display the dots
        # the dots will be displayed in the middle of the screen
        # the dots will be displayed one after the other
        # the dots will be displayed at the same frequency than the letters

        now = pygame.time.get_ticks()

        if (now - current_time > time_between_letters) and (i < number_of_dots) and (not cooldown):
            gameDisplay.fill(white)
            pygame.draw.circle(gameDisplay, black,
                               (display_width/2, display_height/2), 50)
            current_time = now
            i += 1
            cooldown = True
            pygame.display.update()
            clock.tick(60)

        if (now - current_time > time_letter_visible) and cooldown:
            gameDisplay.fill(white)
            cooldown = False
            pygame.display.update()
            clock.tick(60)

        if (i == number_of_dots) and (now-current_time > time_between_letters):

            # dots were displayed, now wait for user input
            dotExit = True

    return goBackToMenu


def letter_input():

    goBackToMenu = False

    hasInput = False

    input_letter = None

    # Display at first a white screen
    # Display then a interrogation mark in black in the middle of the screen
    # After the user has pressed a key, display the letter pressed in the middle of the screen instead of a question mark
    # The input letter will be in black

    # question mark in black in the middle of the screen

    gameDisplay.fill(white)

    question_mark = pygame.font.Font('freesansbold.ttf', 100)
    question_mark_surf, question_mark_rect = text_objects("?", question_mark)
    question_mark_rect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(question_mark_surf, question_mark_rect)

    # Validate input black button at the bottom of the screen
    # If the user presses the button, hasInput will be True
    # the button is a rectangle with the text "Validate" in the middle of the rectangle
    # the button has a black border

    button_width = 200
    button_height = 50
    button_x = (display_width/2) - (button_width/2)
    button_y = display_height - button_height - 10

    button = pygame.Rect(button_x, button_y, button_width, button_height)

    pygame.draw.rect(gameDisplay, black, button, 2)

    button_text = pygame.font.Font('freesansbold.ttf', 20)
    button_text_surf, button_text_rect = text_objects("Validate", button_text)
    button_text_rect.center = (
        (button_x + (button_width/2)), (button_y + (button_height/2)))
    gameDisplay.blit(button_text_surf, button_text_rect)

    pygame.display.update()

    # get time before the user presses a key
    current_time = pygame.time.get_ticks()
    while not hasInput:

        for event in pygame.event.get():

            # forcequit window of game
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if validate button is pressed, hasInput is True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos) and input_letter != None:
                    hasInput = True

                    # time between the user pressing a key and the user pressing the validate button
                    time_input = pygame.time.get_ticks() - current_time

            if event.type == pygame.KEYDOWN:

                # if escape key is pressed, go back to menu
                if event.key == pygame.K_ESCAPE:
                    hasInput = True
                    goBackToMenu = True

                # if a key is pressed, display the letter pressed in the middle of the screen
                # the letter will be in black
                else:
                    input_letter = pygame.key.name(event.key)

                    # display a white rectangle at the same place as the question mark

                    pygame.draw.rect(gameDisplay, white, question_mark_rect)

                    letter_text = pygame.font.Font('freesansbold.ttf', 100)
                    letter_text_surf, letter_text_rect = text_objects(
                        input_letter, letter_text)
                    letter_text_rect.center = (
                        (display_width/2), (display_height/2))
                    gameDisplay.blit(letter_text_surf, letter_text_rect)
                    pygame.display.update()

    return input_letter, goBackToMenu, time_input


def letter_comparison(random_letters, input_letter, number_of_dots):

    # compare the input letter with the random letters
    # if the input letter is in the random letters, the input letter will be displayed in green
    # if the input letter is not in the random letters, the input letter will be displayed in red

    # display a white rectangle at the same place as the question mark

    # gives the position of the input letter in the random letters wich is considered as a "ERROR"
    # if the input letter is not in the random letters, the position will be NONE
    # if the input letter is in the random letters, the position will be the distance between the input letter and the correct letter of the random letters

    position = None

    if input_letter in random_letters:

        if input_letter == random_letters[number_of_dots]:
            position = 0
        else:

            # position result is a little hazardous if the input letter appears multiple times in the random letters
            # the position will be the distance between the correct letter (random_letter[number_of_dots]) and the first occurence of the input letter in the random letters
            # this can be changed with a manual check and getting the position in the array of the input letter closest to the correct letter
            # IF SHIFT IN THE RESULTS : add a loop to do the above correction checking the position of correct +- 1 then +- 2 then +- 3 etc

            position = random_letters.index(input_letter) - number_of_dots

    gameDisplay.fill(white)

    if position == 0:
        letter_text = pygame.font.Font('freesansbold.ttf', 100)
        letter_text_surf, letter_text_rect = text_objects(
            input_letter, letter_text, green)
        letter_text_rect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(letter_text_surf, letter_text_rect)
        pygame.display.update()
        pygame.time.wait(1000)

    else:
        letter_text = pygame.font.Font('freesansbold.ttf', 100)
        letter_text_surf, letter_text_rect = text_objects(
            input_letter, letter_text, red)
        letter_text_rect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(letter_text_surf, letter_text_rect)
        pygame.display.update()
        pygame.time.wait(1000)

    return position


def get_userID():

    # TODO : add a method for user to input his own session ID 
    # session ID need to be a INT (otherwise need to specify how to automatically generate a random string for user ID)

    # read the user ID from the logs.csv file
    # add 1 to the user ID
    # return the new user ID

    # open logs.csv with pandas and read the last line
    logs = pd.read_csv('logs.csv')
    # if the file is empty, the user ID will be 1
    if logs.empty:
        userID = 1
    else:
        userID = logs.iloc[-1]['userID'] + 1

    return userID


def write_results(position):
    # open the results file
    # its a CSV file with 2 columns : the position, the number of user that had this position
    # if the position is not in the file, add
    # if the position is in the file, add 1 to the number of user that had this position

    # open the file with Pandas
    results = pd.read_csv("results.csv")

    # if the position is not in the file, add it
    if position not in results["position"].values:
        # use pd.concat to add a new row to the file
        results = pd.concat([results, pd.DataFrame(
            {"position": [position], "number_of_users": [1]})], ignore_index=True)

    # if the position is in the file, add 1 to the number of users
    else:
        results.loc[results["position"] == position, "number_of_users"] += 1

    # save the file
    results.to_csv("results.csv", index=False)


def logs(userID, random_letters, input_letter, error, time_spent, number_of_dots, ID_try):
    # open the logs file
    # its a CSV file with 8 columns :
    # user ID, the random letters, the input letter, the position, time, correct_letter, ID-try, cumulative-time
    # add a new row with relevate information

    # open the file with Pandas
    logs = pd.read_csv("logs.csv")

    # get correct letter according to input letter and position in the random letters
    i = random_letters.index(input_letter)
    correct_letter = random_letters[i + error]

    # use pd.concat to add a new row to the file
    logs = pd.concat([logs, pd.DataFrame({
        "userID": [userID],
        "random_letters": [random_letters],
        "input_letter": [input_letter],
        "error": [error],
        "time_input": [time_spent],
        "answer":[random_letters[number_of_dots]],
        "ID-try":[ID_try]})], ignore_index=True)

    # save the file
    logs.to_csv("logs.csv", index=False)


def results_screen():

    # display the results
    # the results are a graph with the position on the x axis and the number of users on the y axis

    # open the file with Pandas
    results = pd.read_csv("results.csv")

    # sort the results by position
    results = results.sort_values(by="position")

    # display the graph
    results.plot(x="position", y="number_of_users", kind="bar")
    plt.show()


# Call the game
menu()
pygame.quit()
quit()
