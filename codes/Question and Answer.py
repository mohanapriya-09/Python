import random
questions = {"In which year of First World War Germany declared war on Russia and France?":["a.1914","b.1915","c.1916","d.1917","a"],
        "India has largest deposits of ____ in the world.":["a.gold","b.copper","c.mica","d.None of These","c"],
        "How many Lok Sabha seats belong to Rajasthan?":["a.32","b.25","c.30","d.17","b"],
        "India's first satellite is named after":["a.Aryabhatta","b.Bhaskara II","c.Bhaskara I","d.Albert Einstein","a"],
        "In a normal human body, the total number of red blood cells is":["a.15 trillion","b.20 trillion","c.25 trillion","d.30 trillion","d"],
        "The brain of any computer system is":["a.Memory","b.CPU","c.Control unit","d.None of the above","a"],
        "Which of the following computer language is used for artificial intelligence?":["a.FORTRAN","b.PROLOG","c.C","d.COBOL","b"],
        "The binary system uses powers of":["a.2","b.10","c.8","d.16","a"],
        "Any type of storage that is used for holding information between steps ":["a.CPU","b.Primary storage","c.Intermediate storage","d.Internal storage","c"],
        "A common boundary between two systems is called":["a.Interdiction","b.Interface","c.Surface","d.None of the above","b"],
        }
questions = list(questions.items())
random.shuffle(questions)
questions = dict(questions)
count = 0
for i in questions.keys():
    print(i)
    for j in range(0,len(questions[i])-1,1):
        print(questions[i][j])
    answer = input("Enter your answer : ")
    if answer == questions[i][len(questions[i])-1]:
        count +=1
print("Total Score:",count)

    
    
    

