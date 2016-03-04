#!/bin/python3
import argparse

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

    
