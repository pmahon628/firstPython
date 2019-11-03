# While loops
i = 1
while i <= 10:
    print(i)
    i = i + 1
    # or i += 1
print("done with loop")

# basic guessing game
secret_word = "wizard"
guess = ""
guess_count = 0
guess_limt = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
  if guess_count < guess_limit
    guess = input("Enter guess: ")
    guess_count += 1
  else: 
      out_of_guesses = True

if out_of_guesses: 
    print("you lose")
else: 
    print("You win!")

# FOR loops

