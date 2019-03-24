import fileReader
import v2_Axioms


file_reader = fileReader.FileReader(file_path="test2.txt")

if not v2_Axioms.detect_and_validate_axiom(file_reader): exit(1)
while not file_reader.no_more_words():
    if not v2_Axioms.detect_and_validate_axiom(file_reader):
        exit(1)

print("Validation succeeded")

