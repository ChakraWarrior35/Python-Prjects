question = [
    ["Who is M.S Dhoni?","Actor","Cricketer","Politician","Scientist",2],
    ["What is the capital of India?","Mumbai","Chennai","New Delhi","Kolkata",2],
    ["Who invented the telephone?","Albert Einstein","Alexander Graham Bell","Isaac Newton","Nikola Tesla",1],
    ["Which planet is known as the Red Planet?","Earth","Venus","Mars","Jupiter",2],
    ["Who wrote the Indian National Anthem?","Rabindranath Tagore","Bankim Chandra Chatterjee","Subhash Chandra Bose","Mahatma Gandhi",0],
    ["What is the national animal of India?","Lion","Tiger","Elephant","Leopard",1],
    ["Which gas do plants absorb from the atmosphere?","Oxygen","Nitrogen","Carbon Dioxide","Hydrogen",2], 
    ["Who is known as the Father of the Indian Constitution?","Jawaharlal Nehru","Dr. B.R. Ambedkar","Sardar Patel","Rajendra Prasad",1],
    ["Which is the largest ocean in the world?","Indian Ocean","Atlantic Ocean","Arctic Ocean","Pacific Ocean",3],
    ["What is the currency of Japan?","Dollar","Won","Yen","Rupee",2]
]
score = 0
for questions in question:
    print("\n" + questions[0])
    print(f"a.{questions[1]}")
    print(f"b.{questions[2]}")
    print(f"c.{questions[3]}")
    print(f"d.{questions[4]}")
    a =int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d:\n "))
    if(questions[5] == a):
        print("Correct answer!")
        score += 1
    else:
        print(f"Incorrect, the correct answer is option {questions[5]}")
        print("Better luck next time!")
        break
print("Game Over")
print(f"Your final score is: {score}/{len(question)}")
