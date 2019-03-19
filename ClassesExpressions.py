from ObjectExpressions import *


def class_production(expressions):
    assert(expressions.pop(0) == ":")
    assert(expressions.pop(0).isalnum())


# ClassExpression ::= Class | ObjectIntersectionOf | ObjectUnionOf | ObjectComplementOf | ObjectOneOf
def class_expression(expressions):
    try:
        class_production(expressions)
    except AssertionError:
        if not object_expression_validator(expressions):
            assert(False)


def two_class_expressions(expressions):
    print(expressions)
    class_expression(expressions)
    class_expression(expressions)


# ManyClassExpressions ::= ClassExpression ManyClassExpressions | TwoClassExpressions
def many_class_expressions(expressions):
    expressions_copy = expressions
    try:
        two_class_expressions(expressions_copy)
    except AssertionError:
        expressions = expressions_copy
        class_expression(expressions)
        many_class_expressions(expressions)


def two_classes_production(expressions):
    class_production(expressions)
    class_production(expressions)


def many_classes_productions(expressions):
    expressions_copy = expressions
    try:
        two_classes_production(expressions)
    except AssertionError:
        expressions = expressions_copy
        class_expression(expressions)
        many_class_expressions(expressions)
