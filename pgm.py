#!/usr/bin/env python3

import os

def parse_data(input_lines):    #parse data from txt to array
    
    m = int(input_lines[0].split(":")[-1].strip())
    items = []
    prices = []

    for item in input_lines[4:]:
        if item:
            name = item.split(':')[0]
            price = int(item.split(':')[1].strip())

            items.append([name, price])  #item[0] --> name item[0]--> price
    return m, items



def find_gudie(items, m):    #logic   item[0] --> name item[0]--> price
    difference = None
    start_gudie = None

    for index, item in enumerate(items):
        if index + (m - 1) >= len(items):
            break

        if difference is None:
            start_gudie = 0
            difference = items[m -1][1] - items[0][1]
            continue
        if items[index + m -1][1] - items[index][1] < difference:
            start_gudie = index
            difference = items[index + m -1][1] - items[index][1]

    return start_gudie, difference



def write_output(items, m, start_guddie, difference):
    with open("output3.txt", "w") as f:
        print("The goodies selected for distribution are:\n", file=f)
        for item in items[start_guddie:start_guddie+m]:
            print("{}: {}".format(item[0], item[1]), file=f)
        print(f"\nAnd the difference between the chosen goodie with highest price and the lowest price is {difference}", file=f)
        print("File output.txt genrated")


if __name__ == '__main__':
    #script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    #rel_path = "/input.txt"
    #abs_file_path = os.path.join(script_dir, rel_path)
    # m = number of employees
    # items = list of guddie, price
    input_data = open(r"C:\Users\jojoj\OneDrive\Desktop\nikhilJohn\input3.txt").readlines()

    m, items = parse_data(input_data)

    n = len(items)  # number of items

    # sort items by price
    items.sort(key=lambda x: x[1])
    start_guddie, difference = find_gudie(items, m)    
    write_output(items, m, start_guddie, difference)

