'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # must move two characters at a time
    # if the characters match add to a count variable
    # finish when 2 charactar window reaches the leng of the word.

    
    window = word[:2]
    remaning = word[1:]

    print(window)

    # base case, traversed all the word
    if len(word) < 2:
        return 0

    
    if window == 'th':
        return 1 + count_th(remaning)

    elif window != 'th':
        return count_th(remaning)

# word = "abcthxry" #1
word = "abcthefthghith" #3
# word = "THtHThth" #1
print(count_th(word)) 

