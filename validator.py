from ClassesExpressions import *


def validate(lines):
    for line in lines:
        validateLine(line)


def validateLine(line):
    word = line.pop(0)
    print(word)
    if word == "SubClassOf":
        return SubClassOf(line)
    elif word == "EquivalentClasses":
        return EquivalentClasses(line)
    elif word == "DisjointClasses":
        return DisjointClasses(line)
    elif word == "SameIndividual":
        return SameIndividual(line)
    elif word == "DifferentIndividuals":
        return DifferentIndividuals(line)
    else:
        print("Error in validateLine")


def SubClassOf(line):
    print(line)
    if line.pop(0) != "(":
        print("Error in SubClassOf")
    print(line)
    two_class_expressions(line)


def EquivalentClasses(line):
    1

def DisjointClasses(line):
    1

def SameIndividual(line):
    1

def DifferentIndividuals(line):
    1