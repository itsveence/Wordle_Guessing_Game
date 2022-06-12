def wordle():
    import random

    print("Welcome to my Wordle Guessing Game!")
    word_list = ["clock", "box", "rain", "temple"]
    secret_word = (random.choice(word_list))
    guess = ""
    trials = 0
    print("Your hint is:", "_" * len(secret_word))

    def hint_func():
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] in secret_word:
                if guess[i] == secret_word[i]:
                    hint += guess[i].upper()
                else:
                    hint += guess[i]
            else:
                hint += "_"
        print(f"Your hint is: {hint}")

    while guess != secret_word:
        guess = input("What is your guess?").lower()
        if len(guess) != len(secret_word):
            print(f"Please enter a {len(secret_word)} letter word")
            continue
        trials += 1
        if guess != secret_word:
            print("Your guess was not correct.")
            hint_func()
        else:
            print("Congratulations! You guessed it!")
            if trials == 1:
                print(f"It took you {trials} attempt")
            else:
                print(f"It took you {trials} attempts")


wordle()
