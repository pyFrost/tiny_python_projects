#!/usr/bin/env python3
"""
Author : pyFrost
Date   : 2022-07-11
Title  : Crow's Nest
Purpose: Play with strings
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Steps towards solution"""

    # get input from user
    args = get_args()

    # save user input to a variable
    word = args.word

    # determine required article
    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    # print message
    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
