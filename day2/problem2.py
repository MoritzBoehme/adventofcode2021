#!/usr/bin/env python3
from typing import List, Tuple


class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
        self.aim = 0

    def __str__(self):
        return f"Horizontal: {self.horizontal} Vertical: {self.vertical}"

    def read_commands_from_file(self, file: str) -> None:
        lines = self.parse_file(file)
        commands = list(map(self.split_line, lines))
        for command in commands:
            self.parse_command(command[0], command[1])

    def parse_command(self, command: str, value: int) -> None:
        if command == "forward":
            self.horizontal += value
            self.vertical += self.aim * value
        elif command == "up":
            self.aim -= value
        elif command == "down":
            self.aim += value
        else:
            raise ValueError(f"Command {command} is not supported.")

    @staticmethod
    def split_line(line: str) -> Tuple[str, int]:
        split_line = line.split()
        if len(split_line) != 2:
            raise ValueError(f"Line {line} cannot be split into command and value.")
        command = split_line[0]
        value = int(split_line[1])
        return (command, value)

    @staticmethod
    def parse_file(file: str) -> List[str]:
        with open(file, "r") as f:
            return f.read().splitlines()


if __name__ == "__main__":
    submarine = Submarine()
    submarine.read_commands_from_file("input.txt")
    print(submarine. horizontal * submarine.vertical)
