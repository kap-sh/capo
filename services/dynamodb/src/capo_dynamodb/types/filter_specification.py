"""Generated from Smithy shape ``com.amazonaws.dynamodb#FilterSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.key_expression
    import capo_dynamodb.types.projection_expression


class FilterSpecification(TypedDict, closed=True):
    filter_expression: NotRequired[
        "capo_dynamodb.types.condition_expression.ConditionExpression"
    ]
    """<p>A condition that filters which items are included in the export. This parameter uses the same syntax as <code>FilterExpression</code> in <code>Query</code> and <code>Scan</code>. If you don't provide <code>KeyConditionExpression</code>, this expression can also reference key attributes. If you don't specify this parameter, all items are included in the export.</p>"""
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>The attributes you want to retrieve for items included in the export. Separate attribute names in the expression with commas. If you don't specify this parameter, all attributes are returned.</p>"""
    key_condition_expression: NotRequired[
        "capo_dynamodb.types.key_expression.KeyExpression"
    ]
    """<p>A condition expression that filters items by key values. The expression must test equality on a single partition key value and can optionally compare a sort key value. This parameter uses the same syntax as <code>KeyConditionExpression</code> in <code>Query</code>. When you provide this parameter, <code>FilterExpression</code> can only reference non-key attributes. If you don't specify this parameter, all items are eligible for export.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html">Expression Attribute Names</a> in the Amazon DynamoDB Developer Guide.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeValues.html">Expression Attribute Values</a> in the Amazon DynamoDB Developer Guide.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FilterSpecification) -> dict:
    out: dict = {}
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    if "projection_expression" in value:
        out["ProjectionExpression"] = value["projection_expression"]
    if "key_condition_expression" in value:
        out["KeyConditionExpression"] = value["key_condition_expression"]
    if "expression_attribute_names" in value:
        import capo_dynamodb.types.expression_attribute_name_map

        out["ExpressionAttributeNames"] = (
            capo_dynamodb.types.expression_attribute_name_map.serialize_aws_json_1_0(
                value["expression_attribute_names"]
            )
        )
    if "expression_attribute_values" in value:
        import capo_dynamodb.types.expression_attribute_value_map

        out["ExpressionAttributeValues"] = (
            capo_dynamodb.types.expression_attribute_value_map.serialize_aws_json_1_0(
                value["expression_attribute_values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FilterSpecification:
    out: FilterSpecification = {}  # type: ignore[typeddict-item]
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
    if data.get("ProjectionExpression") is not None:
        out["projection_expression"] = data["ProjectionExpression"]
    if data.get("KeyConditionExpression") is not None:
        out["key_condition_expression"] = data["KeyConditionExpression"]
    if data.get("ExpressionAttributeNames") is not None:
        import capo_dynamodb.types.expression_attribute_name_map

        out["expression_attribute_names"] = (
            capo_dynamodb.types.expression_attribute_name_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeNames"]
            )
        )
    if data.get("ExpressionAttributeValues") is not None:
        import capo_dynamodb.types.expression_attribute_value_map

        out["expression_attribute_values"] = (
            capo_dynamodb.types.expression_attribute_value_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeValues"]
            )
        )
    return out
