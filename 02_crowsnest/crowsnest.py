#!/usr/bin/env python3
"""
Author : Sophia Raji <sophiaraji@gmail.com>
Date   : 2020-12-12
Purpose: Decides proper article for the input and prints string
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Run command line function"""

    args = get_args()
    word = args.word
    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')
    # print("Ahoy, Captain, {} {} off the larboard bow!".format(article, word))


# --------------------------------------------------
if __name__ == "__main__":
    main()
