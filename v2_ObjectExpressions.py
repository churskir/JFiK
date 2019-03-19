from utilities import *
from v2_ClassesExpressions import many_classes_productions

# ObjectIntersectionOf ::= 'ObjectIntersectionOf(' ManyClassExpressions ')'
# ObjectUnionOf ::= 'ObjectUnionOf(' ManyClassExpressions ')'
# ObjectComplementOf ::= 'ObjectComplementOf(' ClassExpression ')'
# ObjectOneOf ::= 'ObjectOneOf(' ManyClasses ')'

# class_expr_for_object_expr = {
#     "ObjectIntersectionOf": ManyClassExpressions,
#     "ObjectUnionOf": ManyClassExpressions,
#     "ObjectComplementOf": ClassExpression,
#     "ObjectOneOf": many_classes_productions
# }

class_expr_for_object_expr = {
    "ObjectIntersectionOf": many_classes_productions,
    "ObjectUnionOf": many_classes_productions,
    "ObjectComplementOf": many_classes_productions,
    "ObjectOneOf": many_classes_productions
}


def detect_object_expression(file_reader):
    word = file_reader.pop_first()
    try:
        validate_object_expression(
            file_reader,
            class_expr_for_object_expr[word]
        )
    except KeyError:
        keys = []
        for key in class_expr_for_object_expr:
            keys.append(key)
        report_error(file_reader.get_line_index(), keys, word)


def validate_object_expression(file_reader, parameters_validator):
    check_opening_colon(file_reader)
    parameters_validator(file_reader)
    check_closing_colon(file_reader)
