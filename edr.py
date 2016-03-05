#!/usr/bin/python3
import argparse
import random
import termcolor
import inflect

def d10():
    return random.randint(1, 10)

def display_dice(dice, target_number, hilight_ones = False):
    dice.sort()
    dice.reverse()
    return " ".join([display_die(die, target_number, hilight_ones) for die in dice])

def display_die(die, target_number, hilight_ones):
    if die == 10:
        return termcolor.colored(str(die), 'yellow', attrs = ['bold'])
    elif die >= target_number:
        return termcolor.colored(str(die), attrs = ['bold'])
    elif die == 1 and hilight_ones:
        return termcolor.colored(str(die), 'red', attrs = ['bold'])
    else:
        return str(die)

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
        if supernatural != 0:
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

    p = inflect.engine()
    s = "Rolling {dice} {die_noun}".format(dice = dice, die_noun = p.plural("die", dice))
    if autos > 0:
        s += " and adding {autos} automatic {success_noun}".format(autos = autos, success_noun = p.plural("success", autos))
    print(s + ".")
    roll(dice, autos = autos)
