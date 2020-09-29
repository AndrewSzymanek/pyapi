#!usr/bin/python3

import argparse

#char_name = input("Which character do you want to know about? (Flash, Batman, Superman")
#name_upper = char_name.capitalize()
#char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)")
heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

parser = argparse.ArgumentParser(description='Research superheroes')

parser.add_argument('name', choices=heroes.keys(), help='name of the superhero to look up')
args = parser.parse_args()
parser.add_argument('stat', choices = heroes.keys(args.name).get(), )

parser.parse_args()

#stat_value = heroes.get("flash").get(char_stat)

#dict_values = heroes.values()
#stat_values = dict_values.keys()
def main():
    #if char_name not in heroes.keys() or char_stat not in stat_values:
       # print("Try again!")
    #else:
        print(f"{args.name}\'s {args.stat} is: {args.name.get(args.stat)}")

main()
