"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.condition_expression
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.expression_attribute_value_map
    import capo_dynamodb.types.key
    import capo_dynamodb.types.return_values_on_condition_check_failure
    import capo_dynamodb.types.table_arn


class ConditionCheck(TypedDict, closed=True):
    key: "capo_dynamodb.types.key.Key"
    """<p>The primary key of the item to be checked. Each element consists of an attribute name and a value for that attribute.</p>"""
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>Name of the table for the check item request. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    condition_expression: "capo_dynamodb.types.condition_expression.ConditionExpression"
    """<p>A condition that must be satisfied in order for a conditional update to succeed. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html">Condition expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html">Expression attribute names</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_values: NotRequired[
        "capo_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html">Condition expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    return_values_on_condition_check_failure: NotRequired[
        "capo_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>Use <code>ReturnValuesOnConditionCheckFailure</code> to get the item attributes if the <code>ConditionCheck</code> condition fails. For <code>ReturnValuesOnConditionCheckFailure</code>, the valid values are: NONE and ALL_OLD.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConditionCheck) -> dict:
    out: dict = {}
    import capo_dynamodb.types.key

    out["Key"] = capo_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    out["TableName"] = value["table_name"]
    out["ConditionExpression"] = value["condition_expression"]
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
    if "return_values_on_condition_check_failure" in value:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConditionCheck:
    out: ConditionCheck = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_dynamodb.types.key

        out["key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        raise DeserializationError("ConditionCheck.key required")
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("ConditionCheck.table_name required")
    if data.get("ConditionExpression") is not None:
        out["condition_expression"] = data["ConditionExpression"]
    else:
        raise DeserializationError("ConditionCheck.condition_expression required")
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
    if data.get("ReturnValuesOnConditionCheckFailure") is not None:
        import capo_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            capo_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
