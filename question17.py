import requests
from bs4 import BeautifulSoup
import random

# question 17
# url = "https://www.nytimes.com/"
# nyt_res = requests.get(url)
# nytres_text = nyt_res.text
# soup = BeautifulSoup(nytres_text, 'lxml')
# h3_titles = []
# for title in soup.find_all(class_="story-heading"):
#     h3_titles.append(title.prettify())
# print(h3_titles)

# question 19 and 21 combined
# add an input to make the user define the name of the file
# url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# van_res = requests.get(url)
# vanres_text = van_res.text
# soup = BeautifulSoup(vanres_text, "lxml")
# words = ""
# for text in soup.find_all('p'):
#     words += text.get_text()
#
# with open("prac-file.txt", "w") as open_file:
#     open_file.write(words)

# question 22
# def question22():
#     counter_dict = {}
#     with open('question22_ex.txt') as f:
#     	line = f.readline()
#     	while line:
#     		line = line.strip()
#     		if line in counter_dict:
#     			counter_dict[line] += 1
#     		else:
#     			counter_dict[line] = 1
#     		line = f.readline()
#     print(counter_dict)

# def question22():
#     counter_dict = {}
#     with open('question22_ex.txt') as f:
#     	line = f.readline()
#     	while line:
#     		line = line[3:-26]
#     		if line in counter_dict:
#     			counter_dict[line] += 1
#     		else:
#     			counter_dict[line] = 1
#     		line = f.readline()
#     print(counter_dict)
#
# question22()
#
# def duplicates():
#     l = []
#     with open("prime-nums.txt", "r") as x:
#         primes = [int(line.strip()) for line in x]
#     with open("happy-nums.txt", "r") as x:
#         happy = [int(line.strip()) for line in x]
#
#     overlap = [x for x in primes if x in happy]
#     print(overlap)
# duplicates()

# def random_pod():
#     import random
#     l = []
#     with open("sowpods.txt", "r") as f:
#         word = f.readline()
#         while word:
#             word = f.readline()
#             l.append(word.strip())
#     pick = random.choice(l)
#     s = ""
#     for i in pick:
#         s += i
#         for char in s
# random_pod()

# def game():
#     print("""
#     Welcome to Hangman, here are some simple rules:
#     1.) If you enter a letter and the count is more than 1, enter the letter x amount of times
#     2.) You will be given a certain number of chances to complete the word
#     3.) Whether you win or lose you will be prompted to play again
#     4.) Enjoy the game :)
#     """)
#     import random
#     l = []
#     incorrect = 0
#     def sowpods():
#         with open("sowpods.txt", "r") as f:
#             word = f.readline()
#             while word:
#                 word = f.readline()
#                 l.append(word.strip())
#     sowpods()
#     pick = random.choice(l)
#     low_word = pick.lower()
#     s = ""
#     print(len(low_word))
#     while True:
#         letter = input("Please enter a letter to start Hangman: ")
#         if letter in low_word:
#             print(low_word.count(letter))
#             s += letter
#         elif letter not in low_word:
#             incorrect += 1
#             print(f"letter is {incorrect}")
#         elif len(s) == len(low_word):
#             print(f"Congratulations the correct word was {low_word}")
#             break
#         elif incorrect > 10:
#             print("You lose!")
#             break
#
# game()

def append_sowpods():
    with open("sowpods.txt", "r") as f:
        sowspods_list = [line.strip() for line in f]
    word = random.choice(sowspods_list)
    return word.lower()

def check_letters():
    ATTEMPTS_ALLOWED = 10
    pick = append_sowpods()
    attempts = 0
    letters_guessed = []
    word = []
    for char in range(len(pick)):
        word.append("_")

    while attempts < ATTEMPTS_ALLOWED:
        guess = input("Guess a letter: ")
        if guess in pick:
            print(f"That {guess} is in the word")
            for index, value in enumerate(pick):
                if value == guess:
                    word[index] = guess
            letters_guessed.append(guess)
        else:
            print("Incorrect guess.")
            attempts += 1
            letters_guessed.append(guess)

        # print("you have guessed these letters: %s"%(''.join(letters_guessed)))
        print(f"You have guessed these letters: {''.join(letters_guessed)}")
        # print('Letters matched so far %s'%''.join(word))
        print(f"Letters matched so far {''.join(word)}")
        print()

        if ''.join(word) == pick:
            print(f"You were right! The correct word was {''.join(word)}")
            break

    if attempts == 10:
        print("You lose the word was %s"%(pick))



check_letters()
