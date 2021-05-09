#!/usr/bin/python3

import os
import sys

###########################################
# Your regex pattern runs in this function!
# Return the matching result as a string
###########################################

import re

def regex_play(str, prob_idx):
    result = ""
    if prob_idx == '1':
        print("==problem1==")
        regex = r"https?://www[.](cyworld|facebook|instagram|twitter)[.]com/[a-z]+$"
        match = re.match(regex, str, re.I)
        if match:
            result = match.group()

    elif prob_idx == '2':
        print("==problem2==")
        regex = r"([a-zA-Z][\w.]*@[a-z]+[.](ac[.]kr|com|net|co[.]kr)$|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)[.]){3}((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))$|(\d{4}-){3}\d{4}$)"
        match = re.match(regex, str)
        if match:
            result = match.group()

    elif prob_idx == '3':
        print("==problem3==")
        regex = r"((?=.{10,})((?P<con>[a-zA-Z~`!@#$%^&*()\-_+={}/:;<>,.?\\\'\"|[\]])((?!(?P=con){2})|(?P=con)(?!(?P=con))))+$)|((?!(\d+)$)(?!([a-zA-Z]+)$)(?!([~`!@#$%^&*()\-_+={}/:;<>,.?\\\'\"|[\]]+)$)(?=.{8,})((?P<ch>[a-zA-Z0-9~`!@#$%^&*()\-_+={}/:;<>,.?\\\'\"|[\]])((?!(?P=ch){2})|(?P=ch)(?!(?P=ch))))+$)"
        match = re.match(regex, str)
        if match:
            result = match.group()
    else:
        print("[ERROR] WRONG PROBLEM NUMBER")
        exit(1)

    return result


def main(file, prob_idx):
    result = []
    # open problem file
    try:
        with open(file, 'r') as f:
            data = f.read()
    except FileNotFoundError as e:
        print("[ERROR] FILE NOT FOUND!")
    split_data = data.splitlines()

    # Run the regex_play function line by line
    for line in split_data:
        result.append(regex_play(line, prob_idx))
    result = list(filter(None, result))
    w_data = '\n'.join(result)

    try:
        with open('output_'+prob_idx+'.txt', 'w', -1, "utf-8") as file:
            file.write(w_data)
            file.close()
    except FileNotFoundError as e:
        print("[ERROR] FILE NOT FOUND!")
    print(w_data)


if __name__ == '__main__':
    if(not sys.argv[1]):
        print("""USAGE: python3 "FILE NAME" "problem NUMBER" """)
    if(not sys.argv[2]):
        print("""USAGE: python3 "FILE NAME" "problem NUMBER" """)
    file = sys.argv[1]
    prob_idx = sys.argv[2]
    main(file, prob_idx)

