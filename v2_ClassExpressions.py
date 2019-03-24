from v2_ObjectExpressions import *
from v2_ClassProductions import *
from utilities import DEBUG

# ClassExpression ::= Class | ObjectIntersectionOf | ObjectUnionOf | ObjectComplementOf | ObjectOneOf
#
# TwoClassExpressions ::= ClassExpression ClassExpression
# ManyClassExpressions ::= ClassExpression ManyClassExpressions | TwoClassExpressions


# Returns False if failed
def class_expression(file_reader):
    word = file_reader.get(0)
    if DEBUG:
        print("class_expression")
        print("Interpreting '%s'" % word)
    if word == ':':
        return class_production(file_reader)
    return detect_and_validate_object_expression(file_reader)


# Returns False if failed
def two_class_expressions(file_reader):
    if DEBUG:
        print("two_class_expressions")
    return class_expression(file_reader) and class_expression(file_reader)


# Returns False if failed
def many_class_expressions(file_reader):
    if DEBUG:
        print("many_class_expressions")
    file_reader_copy = file_reader.copy()
    if two_class_expressions(file_reader):
        return True
    file_reader = file_reader_copy
    return class_expression(file_reader) and many_class_expressions(file_reader)
