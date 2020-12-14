#!/usr/bin/env python3

"""
Author : Sophia
Date   : 2020-12-14
Purpose: List and sort picnic items
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic Game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "item", metavar="str", help="Item(s) to bring", nargs="+", type=str
    )

    parser.add_argument("-s", "--sorted", help="Sort the items", action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Fetch arguments and display results"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()
    if num == 1:
        print(f"You are bringing {items[0]}.")
    elif num == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    else:
        last_elem = items.pop()
        print("You are bringing " + ", ".join(items) + ', and ' + last_elem + '.')


# --------------------------------------------------
if __name__ == "__main__":
    main()
