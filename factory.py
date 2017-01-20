import sys
import json

CREATURES_LIST_FILE = "creatures.json"


class Creature:
    __creature_name = ""

    def __init__(self, creature_name):
        self.__creature_name = creature_name

    # def __init__(self, creature_name, creature_type):
    #     self.__creature_name = creature_name
    #     self.__creature_type = creature_type

    def print_creature(self):
        print "hello"

    def get_creature_name(self):
        return self.__creature_name


class Dragon(Creature):
    __color = ""
    __temp_of_fire = 0

    def __init__(self, color, temp_of_fire):
        self.__color = color
        self.__temp_of_fire = temp_of_fire

    def print_creature(self):
        print "This is a Dragon, is it %s and its' fire tempature is %d. Its' name is %s"%\
              (self.__color, self.__temp_of_fire, self.get_creature_name())


class Giraffe(Creature):
    __height = 0.0
    __num_of_dots = 0

    def __init__(self, height, num_of_dots):
        self.__height = height
        self.__num_of_dots = num_of_dots

    def print_creature(self):
        print "This is a Giraffe, is it %d meters tall and has %d dots. Its' name is %s"%\
              (self.__height, self.__num_of_dots, self.get_creature_name())


class Monster(Creature):
    __num_of_eyes = 0
    __num_of_teeth = 0
    __num_of_legs = 0

    def __init__(self, num_of_eyes, num_of_teeth, num_of_legs):
        self.__num_of_eyes = num_of_eyes
        self.__num_of_teeth = num_of_teeth
        self.__num_of_legs = num_of_legs

    def print_creature(self):
        print "This is a Monster, is has %d eyes, %d teeth and %d legs. Its' name is %s"%\
              (self.__num_of_eyes, self.__num_of_teeth, self.__num_of_legs,  self.get_creature_name())


def creature_factory(creature_name, features):
    if features["type"] == "dragon":
        return Dragon(features["color"], features["temp_of_fire"])
    if features["type"] == "giraffe":
        return Giraffe(features["height"], features["num_of_dots"])
    if features["type"] == "monster":
        return Monster(features["num_of_eyes"], features["num_of_teeth"], features["num_of_legs"])


def name_exists(name, list):
    if name in list:
        return True
    else:
        return False


def parser(file_name):
    json_data = open(file_name).read()
    data = json.loads(json_data)
    return data


def main():
    creatures = parser(CREATURES_LIST_FILE)
    creature_name = sys.argv[1]
    if name_exists(creature_name, creatures):
        new_creature = creature_factory(creature_name, creatures[creature_name])
        new_creature.print_creature()

if __name__ == '__main__':
    main()

