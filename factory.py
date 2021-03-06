import sys
import json

CREATURES_LIST_FILE = "creatures.json"


class Creature:

    def __init__(self, creature_name):
        self._creature_name = creature_name
    
    def get_creature_name(self):
        return self._creature_name


class Dragon(Creature):

    def __init__(self, creature_name, color, temp_of_fire):
        Creature.__init__(self, creature_name)
        self._color = color
        self._temp_of_fire = temp_of_fire

    def print_creature(self):
        print "This is a Dragon, is it %s and its' fire tempature is %d. Its' name is %s."%\
              (self._color, self._temp_of_fire, self.get_creature_name())


class Giraffe(Creature):

    def __init__(self, creature_name, height, num_of_dots):
        Creature.__init__(self, creature_name)
        self._height = height
        self._num_of_dots = num_of_dots

    def print_creature(self):
        print "This is a Giraffe, is it %d meters tall and has %d dots. Its' name is %s."%\
              (self._height, self._num_of_dots, self.get_creature_name())


class Monster(Creature):

    def __init__(self, creature_name, num_of_eyes, num_of_teeth, num_of_legs):
        Creature.__init__(self, creature_name)
        self._num_of_eyes = num_of_eyes
        self._num_of_teeth = num_of_teeth
        self._num_of_legs = num_of_legs

    def print_creature(self):
        print "This is a Monster, is has %d eyes, %d teeth and %d legs. Its' name is %s."%\
              (self._num_of_eyes, self._num_of_teeth, self._num_of_legs,  self.get_creature_name())


def creature_factory(creature_name, features):
    if features["type"] == "dragon":
        return Dragon(creature_name, features["color"], features["temp_of_fire"])
    if features["type"] == "giraffe":
        return Giraffe(creature_name, features["height"], features["num_of_dots"])
    if features["type"] == "monster":
        return Monster(creature_name, features["num_of_eyes"], features["num_of_teeth"], features["num_of_legs"])


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
    if len(sys.argv) == 1:
        for creature_name, creature_data in creatures.iteritems():
            new_creature = creature_factory(creature_name, creature_data)
            new_creature.print_creature()
    elif name_exists(sys.argv[1], creatures):
        new_creature = creature_factory(sys.argv[1], creatures[sys.argv[1]])
        new_creature.print_creature()
    else:
        print "Creature not found"
        sys.exit(1)

if __name__ == '__main__':
    main()