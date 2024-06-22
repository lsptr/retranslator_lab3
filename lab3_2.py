import sys
import re
class Reader:
    def __init__(self, filename):
        self.assignments = {}
        self.functions = {}
        self.variables = {}

        self.read_file(filename)

    def read_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                newline = line.strip().replace(";", "")
                print(newline)
                if ": " in newline:
                    key, value = newline.split(": ")
                    self.functions[key] = value
                elif "=" in newline:
                    self.assign_op(newline)
                elif "print" in newline:
                    newprint = newline.split(" ")
                    self.print_op(newprint)
            print("functions:   ", self.functions)
            print("variables:   ", self.variables)

    def print_op(self, newprint):
        if len(newprint) == 1:
            print("variables:   ", self.variables)
        elif len(newprint) == 2:
            print(newprint[1], ":    ", self.variables[newprint[1]])
        else:
            raise StopIteration("Invalid print command")

    def assign_op(self, newline):
        key, value = newline.split("=")
        self.variables[key] = self.do_instruction(value)
        print("variables:   ", self.variables)

    def do_instruction(self, instruction):
        stack = self.parse_instruction(instruction)
        print("stack:  ", stack)

        if (len(stack) == 1) and (stack[0].isdigit()):
            return stack[0]
        else:
            pass

    def parse_instruction(self, instruction):
        stack = []
        word = ""
        for char in instruction:
            if char in ['-', '+', '*', '/', '(', ')']:
                if word:
                    stack.append(word)
                    word = ""
                stack.append(char)
            else:
                word += char
        if word:
            stack.append(word)
        return stack




filename = 'file2_1.txt'
reader = Reader(filename)