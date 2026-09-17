import random


def play_game():
	secret_number = random.randint(1, 100)
	attempts = 0

	print("\nI am thinking of a number from 1 to 100.")

	while True:
		answer = input("Enter your guess: ").strip()

		if not answer.isdigit():
			print("Please enter a whole number.")
			continue

		guess = int(answer)

		if guess < 1 or guess > 100:
			print("Your guess must be between 1 and 100.")
			continue

		attempts += 1

		if guess < secret_number:
			print("Too low. Try again!")
		elif guess > secret_number:
			print("Too high. Try again!")
		else:
			print(f"Correct! You guessed it in {attempts} attempts.")
			break


def main():
	print("=== Random Number Guesser ===")

	while True:
		play_game()
		play_again = input("Would you like to play again? (y/n): ").strip().lower()

		if play_again != "y":
			print("Thanks for playing!")
			break


if __name__ == "__main__":
	main()
