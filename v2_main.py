from fileReader import *
from v2_ClassesExpressions import *
from v2_ObjectExpressions import *


file_reader = FileReader("test2.txt")

detect_object_expression(file_reader)
while not file_reader.no_more_words():
    detect_object_expression(file_reader)

print("Validation succeeded")

