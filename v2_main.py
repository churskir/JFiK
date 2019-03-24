from fileReader import *
from v2_Axioms import detect_and_validate_axiom


file_reader = FileReader(file_path="test2.txt")

if not detect_and_validate_axiom(file_reader): exit(1)
while not file_reader.no_more_words():
    if not detect_and_validate_axiom(file_reader):
        exit(1)

print("Validation succeeded")

