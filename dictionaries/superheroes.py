#!usr/bin/python3

char_name = input("Which character do you want to know about? (Flash, Batman, Superman")
name_upper = char_name.capitalize()
char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)")

heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

stat_value = heroes.get("flash").get(char_stat)

def main():
    print(f"{name_upper}\'s {char_stat} is: {stat_value}")

main()
