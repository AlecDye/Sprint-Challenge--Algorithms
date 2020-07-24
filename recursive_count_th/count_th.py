"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

# check "st" example from lecture

# scan word and return a count int


def count_th(word):

    # The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1.

    # str.find(sub[, start[, end]] )

    # case: end condition check for "th"?
    # Using find -> case: if "th" isn't in word
    # -1 means not found
    if word.find("th") == -1:
        return 0

    # case: continue condition -> use recursion (instead of loop)
    else:
        # returns index position of first occurrence
        start = word.find("th")
        # start plus 2 (th takes up 2 positions in the index )
        # [index start: (rest of index)]
        recur = 1 + count_th(word[start + 2 :])

        return recur


print(count_th("path"))
print(count_th("this"))
print(count_th("th"))
print(count_th("hat"))

