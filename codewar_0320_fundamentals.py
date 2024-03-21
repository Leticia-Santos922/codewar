# Convert a string to a number

def string_to_numbers(s):
    return int(s)


# Summation of every number from 1 to num

def summation(num):
    return (num*(num + 1)) / 2
#     sum(range(1,num+1))


# Return the time since midnight in milliseconds
def past(h, m, s):
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        return (h * 3600000) + (m * 60000) + (s * 1000)


# multiply a given a number by 8 if even, else by 9
def simple_multiplication(number):
    if (number % 2) == 0:
        return number * 8
    else:
        return number * 9


# Reverse a string
def solution(string):
    return string[::-1]


# convert given boolean value into its string representation
def boolean_to_string(b):
    if b:
        return "True"
    else:
        return "False"
# return str(b)
# return f"{b}"


# there are 'n' classmates, paperwork has 'm' pages
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m


# rock, paper, scissors
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    else:
        return "Player 1 won!"


def rps1(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif ((p1 == 'rock' and p2 == 'scissors') or
          (p1 == 'scissors' and p2 == 'paper') or
          (p1 == 'paper' and p2 == 'rock')):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'


def rps2(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


# Remove first and last character of a string
def remove_char(s):
    return s[1:-1]


# convert number to string
def number_to_string(num):
    return str(num)
#   return f"{num}"


# one has to be true and one has to false
def love_func(flower1, flower2):
    if (flower1 % 2) == 0 and (flower2 % 2) == 0:
        return False
    if (flower1 % 2) == 1 and (flower2 % 2) == 1:
        return False
    else:
        return True

# return (flower1+flower2)%2


# make number negative
def make_negative(number):
    return -abs(number)


# convert a string to an array
def string_to_array(s):
    mylist = s.split()
    if len(mylist) == 0:
        mylist = ['']
    return mylist

# def string_to_array(string):
#     return string.split(" ")


# Given a non-negative integer, return a string with a murmur, 1 sheep, 2 sheep, 3 sheep
def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n+1))

# def count_sheep(n):
#     mylist = []
#     for n in range(1, n + 1):
#         mylist += str(n) + ' sheep...'
#     return "".join(mylist)


# sentence smash
def smash(words):
    return " ".join(words)


# find the position of the word within the list
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"


# work out rent of car, 7 days is 50 off, 3 days is 20 off, each day is 40
def rental_car_cost(d):
    if d >= 7:
        discount = 50
    elif d >= 3:
        discount = 20
    else:
        discount = 0
    cost = d * 40 - discount
    return cost

# def rental_car_cost(d):
#     result = d * 40
#     if d >= 7:
#         result -= 50
#     elif d >= 3:
#         result -= 20
#     return result

# def rental_car_cost(d):
#   return d * 40 - (d > 2) * 20 - (d > 6) * 30


# work out bmi
def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"


# drink 0.5l every hour
import math


def litres(time):
    total = math.floor(time*0.5)
    return total

# def litres(time):
#     return time // 2


# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives,
# and the negatives become positives.

def invert(lst):
    lists = 0
    for num in lst:
        lists.append(num*-1)
    return lists

# def invert(lst):
#    return [i*-1 for i in lst]
