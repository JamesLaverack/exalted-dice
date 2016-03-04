#!/bin/python3
import argparse
import random

def d10():
    return random.randint(1, 10)

def count_successes(results, target_number):
    count = 0
    double_count = 0
    for result in results:
        if result >= target_number:
            count += 1
        if result == 10:
            double_count += 1
    return [count, count + double_count]

def roll(dice, autos = 0, target_number = 7):
    # Roll the correct number of dice
    results = [d10() for x in range(0, dice)]
    print(results)
    normal, double = count_successes(results, target_number)

    normal += autos
    double += autos

    print("Rolled {double} successes ({normal} without 10s giving two successes)".format(normal = normal, double = double))

def parse_dice_expression(epr):
    splr = epr.split("a")
    if not splr[0]:
        splr[0] = 0
    if len(splr) == 1:
        splr.append(0)
    return [int(x) for x in splr]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dice", help = "A dice expression")
    args = parser.parse_args()

    dice, autos = parse_dice_expression(args.dice)

    print("Rolling {dice} dice with {autos} automatic successes".format(dice = dice, autos = autos))
    roll(dice, autos = autos)
    
