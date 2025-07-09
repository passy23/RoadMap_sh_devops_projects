import random

def get_difficulty():
    """Get difficulty level from user."""
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ["1", "2", "3"]:
            return {"1": 10, "2": 5, "3": 3}[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")

def play_game():
    """Run a single round of the number guessing game."""
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    chances = get_difficulty()
    print(f"\nGreat! You have selected the {'Easy' if chances == 10 else 'Medium' if chances == 5 else 'Hard'} difficulty level.")
    print(f"You have {chances} chances to guess the correct number.\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while attempts < chances:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
                
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                return
            elif guess > secret_number:
                print("Incorrect! The number is less than", guess)
            else:
                print("Incorrect! The number is greater than", guess)
                
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    print(f"\nGame Over! The number was {secret_number}.")

def main():
    """Main function to run the game."""
    play_game()

if __name__ == "__main__":
    main()

