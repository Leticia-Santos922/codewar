import re
# If your name starts with 'r' you're playing banjo


def are_you_playing_banjo(name):
    lower_case = name.lower()
    if lower_case[0] == 'r':
        return name + " does play banjo"
    else:
        return name + " does not play banjo"


def playing_banjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'


# sum of a list of numbers
def sum_array(a):
    return sum(a)


# return the numer of vowels in the string
def get_count(sentence):
    count = 0
    vowels = "aeiou"
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count


def get_count_re(sentence):
    vowels = re.findall('[aeiou]', sentence.lower())
    return len(vowels)


# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

# count positive, sum of negatives
def count_positives_sum_negatives(arr):
    positive_num = 0
    negative_num = 0
    if not arr:
        return []
    for numbers in arr:
        if numbers > 0:
            positive_num += 1
        elif numbers < 0:
            negative_num += numbers
    return [positive_num, negative_num]


# return boolean to string values
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     elif boolean == False:
#         return "No"


# calculate the sum of the numbers in the nth row of this triangle
def row_sum_odd_numbers(n):
    return n**3


# middle character of the word
def get_middle(s):
    middle = int(len(s)/2)
    if len(s) % 2 == 0:
        return s[middle-1:middle+1]
    else:
        return s[middle]

# def get_middle(s):
#     i = (len(s) - 1) // 2
#     return s[i:-i] or s


# find opposite of number
def opposite(number):
    if number > 0:
        return -abs(number)
    else:
        return abs(number)


# hello world!
def greet():
    return "hello world"


if __name__ == "__main__":
    print(are_you_playing_banjo('Name'))
    print(are_you_playing_banjo('richard'))
    print(are_you_playing_banjo('Rikki'))
    print(sum_array([1, 3]))
    print(get_count('hello'))
    print(count_positives_sum_negatives([1, 2, 3, 6, -1]))
    print(get_middle("hello"))
    print(get_middle("helloo"))
    print(opposite(2))
    print(opposite(-2))
