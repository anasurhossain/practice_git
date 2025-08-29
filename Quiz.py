# Python quiz game

questions = ("How many elements in the periodic table ?",
             "Which animal lays the largest eggs?",
             "What is the most abundant gas in the Earth's atmosphere ?",
             "How many bones are in the human body ?",
             "Which planet in the solar system is the hottest?")

options = (("A. 117", "B. 118", "C. 119", "D. 120"),
           ("A. Whale", "B. Emu", "C. Ant", "D. Ostrich"),
           ("A. Nigtrogen", "B. Oxygen", "C. CO2", "D. Helium"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Neptune"))

answers = ("B", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("---------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT ")
        score += 1
    else:
        print("INCORRECT ")
        print(f"{answers[question_num]} is the correct answer.")

    question_num += 1

print("---------------------------")
print("         RESULT            ")
print("---------------------------")

print("answer", end = " ")
for answer in answers:
    print(answer, end = " ")
print()
print("guess", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score}%")
