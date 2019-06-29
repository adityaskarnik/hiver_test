# Find anagram in the given list and return the max of them all
from itertools import groupby

def input_anagram(anagram_list):
    d = sorted(anagram_list, key=sorted)
    print(d)
    for a, b in groupby(sorted(anagram_list, key=sorted), sorted):
        b = list(b)
        if len(b) > 1:
            print(b)


if __name__ == "__main__":
    list_input = input("Input the list elements: ")
    input_anagram(list_input.split())