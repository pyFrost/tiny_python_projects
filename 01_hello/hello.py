#!/usr/bin/env python3
"""
Author: pyFrost
Date: 10.July.2022
Purpose: Say hello
"""

import argparse


def get_args():
    """ Get the command-line arguments """
        
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Steps to fulfil purpose"""
    
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
