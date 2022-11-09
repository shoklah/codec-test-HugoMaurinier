#!/usr/bin/env python
from robot.robot import robot
from sys import argv

def main():
    if len(argv) != 3:
        print(f'''Usage: python3 pilot.py <map_dimensions> <command>
        ex: python3 pilot.py 5x5 FFRFLFLF''')
        exit(1)
    map_dimensions = argv[1].split('x')
    robot1 = robot(int(map_dimensions[0]), int(map_dimensions[1]))
    robot1.move(argv[2])
    robot1.print_position()
    exit(0)

if __name__ == "__main__":
    main()