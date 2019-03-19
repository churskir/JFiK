from ClassesExpressions import *


def object_expression_validator(expressions):
    expression = expressions.pop(0)
    print(expression)
    function = None
    if expression == 'ObjectIntersectionOf':
        function = object_intersection_of
    elif expression == 'ObjectUnionOf':
        function = object_union_of
    elif expression == 'ObjectComplementOf':
        function = object_complement_of
    elif expression == 'ObjectOneOf':
        function = object_one_of
    if function is not None:
        function(expressions)
        return True
    else:
        return False


# ObjectIntersectionOf ::= 'ObjectIntersectionOf(' ManyClassExpressions ')'
def object_intersection_of(expressions):
    print('XX')
    assert(expressions.pop(0) == '(')
    many_class_expressions(expressions)
    assert(expressions.pop(0) == ')')


# ObjectUnionOf ::= 'ObjectUnionOf(' ManyClassExpressions ')'
def object_union_of(expressions):
    print('XX')
    assert(expressions.pop(0) == '(')
    many_class_expressions(expressions)
    assert(expressions.pop(0) == ')')


# ObjectComplementOf ::= 'ObjectComplementOf(' ClassExpression ')'
def object_complement_of(expressions):
    print('XX')
    assert(expressions.pop(0) == '(')
    class_expression(expressions)
    assert(expressions.pop(0) == ')')


# ObjectOneOf ::= 'ObjectOneOf(' ManyClasses ')'
def object_one_of(expressions):
    print('XX')
    assert(expressions.pop(0) == '(')
    many_classes_productions(expressions)
    assert(expressions.pop(0) == ')')
