'''
Atharv phadale
23/10/2023
'''
# todo kaun banega corepati
# todo Rules


import random


def get_questions(my_dict,my_correct_dict):
    dict = {}
    correct_dict = {}
    i = 0
    j=0
    while i<7:
        selected_key = random.choice(list(my_dict.keys()))

        if selected_key in dict:
            continue
        else:
            dict[selected_key] = my_dict.get(selected_key)
        i+=1
    for outerkey,value in my_correct_dict.items():
        if outerkey in dict:
            correct_dict[outerkey] = my_correct_dict.get(outerkey)
        else:
            continue
    return dict,correct_dict


def fifty_fifty(inner_dict , correct_naswer):
    fifty = {}
    for key, value in inner_dict.items():
        if value == correct_naswer:
            fifty[key] = value
    while True:
        ran = int(random.uniform(1,5))
        if ran in fifty:
            continue
        else:
            secondkey = ran
            break
    fifty[secondkey] = inner_dict.get(secondkey)
    print(fifty)



def audience_poll(outerkey, inner_dict,correct_answer):

    presented_to_user = {}
    for inner_key,inner_value in inner_dict.items():
        if inner_value == correct_answer:
            max_value  = round(random.uniform(0.60,0.85),2)
            presented_to_user[correct_answer] = max_value
    random_values = []
    og = 1 -  max_value

    remaining_sum = og

    for i in range(2):
        m_val = remaining_sum/(3-i)
        value = round(random.uniform(0,m_val),2)
        random_values.append(value)
        remaining_sum -= value
    random_values.append(round(og - sum(random_values),2))

    for inner_key,inner_value in inner_dict.items():
        if inner_value == correct_answer:
            continue
        else:
            presented_to_user[inner_value] = random_values.pop()
    for key,value in presented_to_user.items():
        presented_to_user[key] = value*100
    print(presented_to_user)





my_dict = {
    "What is the capital of France?": {
        1: "Paris",
        2: "London",
        3: "Berlin",
        4: "Madrid",
    },
    "Who wrote the play 'Romeo and Juliet'?": {
        1: "William Shakespeare",
        2: "George Orwell",
        3: "Charles Dickens",
        4: "Jane Austen",
    },
    "Which planet is known as the 'Red Planet'?": {
        1: "Mars",
        2: "Venus",
        3: "Jupiter",
        4: "Saturn",
    },
    "Which country won the FIFA World Cup in 2018?": {
        1: "France",
        2: "Brazil",
        3: "Germany",
        4: "Argentina",
    },
    "What is the largest mammal in the world?": {
        1: "Elephant",
        2: "Blue Whale",
        3: "Giraffe",
        4: "Hippopotamus",
    },
    "Who painted the 'Mona Lisa'?": {
        1: "Pablo Picasso",
        2: "Vincent van Gogh",
        3: "Leonardo da Vinci",
        4: "Michelangelo",
    },
    "Which gas is most abundant in Earth's atmosphere?": {
        1: "Oxygen",
        2: "Nitrogen",
        3: "Carbon Dioxide",
        4: "Argon",
    },
    "Which movie won the Academy Award for Best Picture in 2020?": {
        1: "Parasite",
        2: "Joker",
        3: "1917",
        4: "Once Upon a Time in Hollywood",
    },
    "What is the chemical symbol for gold?": {
        1: "Au",
        2: "Ag",
        3: "Fe",
        4: "Hg",
    },
    "Who was the first woman to fly solo across the Atlantic Ocean?": {
        1: "Amelia Earhart",
        2: "Bessie Coleman",
        3: "Valentina Tereshkova",
        4: "Sally Ride",
    },
    #----------------------------------------------------
"What is the largest planet in our solar system?": {
        1: "Earth",
        2: "Mars",
        3: "Jupiter",
        4: "Saturn",
    },
    "Which scientist is famous for the theory of relativity?": {
        1: "Isaac Newton",
        2: "Stephen Hawking",
        3: "Galileo Galilei",
        4: "Albert Einstein",
    },
    "In which year did Christopher Columbus discover America?": {
        1: "1492",
        2: "1620",
        3: "1776",
        4: "1812",
    },
    "Who wrote 'To Kill a Mockingbird'?": {
        1: "J.K. Rowling",
        2: "George Orwell",
        3: "Harper Lee",
        4: "Mark Twain",
    },
    "What is the largest ocean on Earth?": {
        1: "Atlantic Ocean",
        2: "Indian Ocean",
        3: "Arctic Ocean",
        4: "Pacific Ocean",
    },
    "Which gas do plants absorb from the atmosphere during photosynthesis?": {
        1: "Carbon Dioxide",
        2: "Oxygen",
        3: "Nitrogen",
        4: "Hydrogen",
    },
    "Who is the lead character in 'The Lord of the Rings' series?": {
        1: "Frodo Baggins",
        2: "Gandalf",
        3: "Harry Potter",
        4: "Luke Skywalker",
    },
    "What is the currency of Japan?": {
        1: "Yen",
        2: "Dollar",
        3: "Euro",
        4: "Pound",
    },
    "Who was the first woman to win a Nobel Prize?": {
        1: "Marie Curie",
        2: "Rosa Parks",
        3: "Mother Teresa",
        4: "Eleanor Roosevelt",
    },
    "What is the main component of the Earth's core?": {
        1: "Gold",
        2: "Iron",
        3: "Silver",
        4: "Copper",
    },
    #----------------------------------
"What is the largest desert in the world?": {
        1: "Gobi Desert",
        2: "Sahara Desert",
        3: "Mojave Desert",
        4: "Atacama Desert",
    },
    "Who is the author of 'War and Peace'?": {
        1: "Fyodor Dostoevsky",
        2: "Charles Dickens",
        3: "Leo Tolstoy",
        4: "Jane Austen",
    },
    "What is the chemical symbol for water?": {
        1: "H2O",
        2: "CO2",
        3: "NaCl",
        4: "O2",
    },
    "In which year did the Titanic sink?": {
        1: "1907",
        2: "1912",
        3: "1923",
        4: "1931",
    },
    "Who is known as the 'Father of Modern Physics'?": {
        1: "Albert Einstein",
        2: "Isaac Newton",
        3: "Galileo Galilei",
        4: "Stephen Hawking",
    },
    "Which planet is known as the 'Evening Star'?": {
        1: "Venus",
        2: "Mars",
        3: "Jupiter",
        4: "Saturn",
    },
    "What is the chemical symbol for silver?": {
        1: "Si",
        2: "Sv",
        3: "Ag",
        4: "Sl",
    },
    "Who wrote 'The Great Gatsby'?": {
        1: "Ernest Hemingway",
        2: "F. Scott Fitzgerald",
        3: "Harper Lee",
        4: "J.D. Salinger",
    },
    "What is the largest mammal on Earth?": {
        1: "Elephant",
        2: "Blue Whale",
        3: "Lion",
        4: "Giraffe",
    },
    "Which gas is responsible for the green color of plants?": {
        1: "Carbon Dioxide",
        2: "Oxygen",
        3: "Nitrogen",
        4: "Chlorophyll",
    }
}

# Dictionary for correct answers
my_correct_dict = {
    "What is the capital of France?": "Paris",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "Which planet is known as the 'Red Planet'?": "Mars",
    "Which country won the FIFA World Cup in 2018?": "France",
    "What is the largest mammal in the world?": "Blue Whale",
    "Who painted the 'Mona Lisa'?": "Leonardo da Vinci",
    "Which gas is most abundant in Earth's atmosphere?": "Nitrogen",
    "Which movie won the Academy Award for Best Picture in 2020?": "Parasite",
    "What is the chemical symbol for gold?": "Au",
    "Who was the first woman to fly solo across the Atlantic Ocean?": "Amelia Earhart",
    #-------------------------------------------------
"What is the largest planet in our solar system?": "Jupiter",
    "Which scientist is famous for the theory of relativity?": "Albert Einstein",
    "In which year did Christopher Columbus discover America?": "1492",
    "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
    "What is the largest ocean on Earth?": "Pacific Ocean",
    "Which gas do plants absorb from the atmosphere during photosynthesis?": "Carbon Dioxide",
    "Who is the lead character in 'The Lord of the Rings' series?": "Frodo Baggins",
    "What is the currency of Japan?": "Yen",
    "Who was the first woman to win a Nobel Prize?": "Marie Curie",
    "What is the main component of the Earth's core?": "Iron",
    #------------------------------------------------------------
"What is the largest desert in the world?": "Sahara Desert",
    "Who is the author of 'War and Peace'?": "Leo Tolstoy",
    "What is the chemical symbol for water?": "H2O",
    "In which year did the Titanic sink?": "1912",
    "Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
    "Which planet is known as the 'Evening Star'?": "Venus",
    "What is the chemical symbol for silver?": "Ag",
    "Who wrote 'The Great Gatsby'?": "F. Scott Fitzgerald",
    "What is the largest mammal on Earth?": "Blue Whale",
    "Which gas is responsible for the green color of plants?": "Chlorophyll"
}

dict, correct_dict = get_questions(my_dict,my_correct_dict)
#todo here that questions function

fix_money_stops = [100000, 3500000, 10000000]
money = { 1:10000 , 2:50000 , 3:100000 , 4:200000  , 5:3500000 , 6:5000000 ,  7:10000000}
fixed_price = [0]
current_price = [0]
life_lines = {6: 'Audience poll' , 7 : '50 - 50' , }

lifelines = {}

print('welcome to ')
print(f'------------------------- Kaun Banega Crorepati ------------------------------------')
print('Rules')
print('You have to select between any of the  1,2,3 or 4 options ')
print('press 5 to quit')
print('press 6,7 for lifelines you can used both lifelines')
print('you can used each lifeline only once ')
print('you can quit the game any time you want')

i=0
out = True
audiencepoll_lifeline = 1
fifty_fifty_lifeline = 1


for outerkey,inner_dict in dict.items():
    i += 1
    print('-----------------------------------------------------')
    print(f'Question number {i} is :')
    print(outerkey)
    for inner_key,inner_value in inner_dict.items():
        print(f'{inner_key} {inner_value}')


    if not life_lines:
        print(f'you are left with no life lines')
    else:
        print(f"you are left with following life lines: {', '.join([value for value in life_lines.values()])}")


    answer = int(input('enter the correct option between 1,2,3,4 or 5 to quit and 6 for Audience poll lifeline '
                       'and 7 for 50-50 lifeline \n'))
    #todo if lifeline then code
    #todo else below code

    if answer == 6  and audiencepoll_lifeline == 1:
        if answer == 6:
            del life_lines[6]
            audiencepoll_lifeline = 0
            correct_answer = correct_dict.get(outerkey)
            (audience_poll(outerkey,inner_dict,correct_answer))
            l_final_answer = int(input('select the correct answer among 1,2,3 or 4 \n '))
            double_final_answer = inner_dict.get(l_final_answer)
            if double_final_answer == correct_answer:
                temp = money.get(i)
                # print(f'temp {temp}')
                current_price.append(temp)
                if temp in fix_money_stops:
                    fixed_price.append(temp)
                print('correct answer ----------')
                print(f'your current amount is {temp}  and fixedprice is {fixed_price[-1]}')
                print('-----------------------------------------------------')
                continue
            elif answer == 5:
                print(f'you quit the game and take amount {current_price[-1]} with you ')
                out = False
                break
            else:
                print('wrong answer')
                xx = fixed_price.pop()
                print(f'you lose the game and take amount {xx}')
                out = False
                break

    elif answer == 7  and fifty_fifty_lifeline == 1:
        if answer == 7:
            del life_lines[7]
            fifty_fifty_lifeline = 0
            correct_answer = correct_dict.get(outerkey)
            (fifty_fifty(inner_dict,correct_answer))
            l_final_answer = int(input('select the correct answer among 1,2,3 or 4 \n '))
            double_final_answer = inner_dict.get(l_final_answer)
            if double_final_answer == correct_answer:
                temp = money.get(i)
                # print(f'temp {temp}')
                current_price.append(temp)
                if temp in fix_money_stops:
                    fixed_price.append(temp)
                print('correct answer ----------')
                print(f'your current amount is {temp}  and fixedprice is {fixed_price[-1]}')
                print('-----------------------------------------------------')
                continue
            elif answer == 5:
                print(f'you quit the game and take amount {current_price[-1]} with you ')
                out = False
                break
            else:
                print('wrong answer')
                xx = fixed_price.pop()
                print(f'you lose the game and take amount {xx}')
                out = False
                break

    else:

        final_answer = inner_dict.get(answer)
        correct_answer = correct_dict.get(outerkey)

        if final_answer == correct_answer:
            temp = money.get(i)
            # print(f'temp {temp}')
            current_price.append(temp)
            if temp in fix_money_stops:
                fixed_price.append(temp)
            print('correct answer ----------')
            print(f'your current amount is {temp}  and fixedprice is {fixed_price[-1]}')
            print('-----------------------------')
            continue
        elif answer == 5:
            print(f'you quit the game and take amount {current_price[-1]} with you ')
            out = False
            break
        elif answer == 6:
            out = False
            print('you have selected wrong option')
            xx = fixed_price.pop()
            print(f'you lose the game and take amount {xx}')
            break
        elif answer == 7:
            out = False
            print('you have selected wrong option')
            xx = fixed_price.pop()
            print(f'you lose the game and take amount {xx}')
            break
        else:
            print('wrong answer')
            xx = fixed_price.pop()
            print(f'you lose the game and take amount {xx}')
            out = False
            break
if out == True:
    print(f'you are the winner of the game with price 1 crore')






