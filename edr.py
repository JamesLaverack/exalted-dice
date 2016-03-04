#!/bin/python3
import argparse
import random
import termcolor

def d10():
    return random.randint(1, 10)

def printn(p):
    print(p, end = "")

def display_dice(dice, target_number, hilight_ones = False):
    dice.sort()
    dice.reverse()
    line = ""
    for die in dice:
        line += " "
        if die == 10:
            line += termcolor.colored(str(die), 'yellow', attrs = ['bold'])
        elif die >= target_number:
            line += termcolor.colored(str(die), attrs = ['bold'])
        elif die == 1:
            if hilight_ones:
                line += termcolor.colored(str(die), 'red', attrs = ['bold'])
            else:
                line += str(die)
        else:
            line += str(die)
    return line

def count_successes(results, target_number):
    count = 0
    double_count = 0
    for result in results:
        if result >= target_number:
            count += 1
        if result == 10:
            double_count += 1
    return [count + double_count, count]

def roll(dice, autos = 0, target_number = 7):
    # Roll the correct number of dice
    results = [d10() for x in range(0, dice)]
    supernatural, mortal = count_successes(results, target_number)

    if supernatural == 0 and 1 in results:
        # Botch
        print(display_dice(results, target_number, hilight_ones = True))
        print(termcolor.colored("Botch", 'red', attrs = ['bold']))
    else:
        # Apply auto successes
        supernatural += autos
        mortal += autos

        print(display_dice(results, target_number))
        print("Successes      : " + termcolor.colored(supernatural, 'yellow', attrs = ['bold']))
        print("Mortals/Damage : " + termcolor.colored(mortal, attrs = ['bold']))

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
    
