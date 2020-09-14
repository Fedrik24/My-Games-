import random
import time

# Initial Steps to invite in the game
print("\n Welcome to Hangman game\n")
name = input("Enter your name : ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print ("The games is about to start!\n Let's play Hangman")
time.sleep(3)

def main():
	global count
	global display
	global word
	global already_guessed
	global length
	global play_game
	word_to_guess = ["january","border","handphone", "keyboard","mouse", "remote", "hand","arm", "tisue", "glass", "key"]

	word = random.choice(word_to_guess)
	length = len(word)
	count = 0
	display = '_' * length
	already_guessed = []
	play_game = ""

# A Loop to re-execute the games when the first roudn ends

def play_loop():
	global play_game
	play_game = input("Do you want to play again? y/n \n")
	while play_game not in ['Y','y','N','n','yes','YES','Yes','No','NO','no']:
		play_game = input("Do you want to play again?\n")
	if play_game == 'y':
		main()
	elif play_game == 'n':
		print ("Thank you for playing")
		exit()

def hangman():
	global count
	global display
	global word
	global already_guessed 
	global play_game
	limit = 5
	guess = input("This is Hangman Word" + display +"Enter your guess\n")
	guess = guess.strip()
	if len(guess.strip()) == 0 or len(guess.strip()) >=2 or guess <= "9":
		print ("Invalid Input, Try a Letter\n")
		hangman() 

	elif guess in word:
		already_guessed.extend([guess])
		index = word.find(guess)
		word = word[:index] + "_" + word[index + 1:]
		display = display[:index] + guess + display[index + 1:]
		print (display + "\n")
	elif guess in already_guessed:
		print("Try Another letter.\n")

	else:
		count +=1

		if count == 1:
			time.sleep(1)
			print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
			print("Wrong guess. " + str(limit-count) + " guesses remaining \n")
		elif count == 2:
			time.sleep(1)
			print("   _____  \n"
                  "  |     | \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
			print("Wrong guess. " + str(limit-count) + " guesses remaining \n")
	
		elif count == 3:
			time.sleep(1)
			print("   _____  \n"
                  "  |     | \n"
                  "  |     |  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
			print("Wrong guess. " + str(limit-count) + " guesses remaining \n")

		elif count == 4:

			time.sleep(1)
			print("   _____  \n"
                  "  |     | \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "__|__\n")
			print("Wrong guess. " + str(limit-count) + " guesses remaining \n")
		elif count == 5:

			time.sleep(1)
			print("   _____  \n"
                  "  |     | \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O  \n"
                  "  |    /|\  \n"
                  "  |    / \\n"
                  "__|__\n")
			print("Wrong guess. " + str(limit-count) + " guesses remaining \n")			

	if word == "_"*length:
		print ("Congrats! You guessed word correcly! ")
		play_loop()
	elif count != limit:
		hangman()
main()
hangman()