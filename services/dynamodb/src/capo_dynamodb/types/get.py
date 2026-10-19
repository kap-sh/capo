"""Generated from Smithy shape ``com.amazonaws.dynamodb#Get``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.key
    import capo_dynamodb.types.projection_expression
    import capo_dynamodb.types.table_arn


class Get(TypedDict, closed=True):
    key: "capo_dynamodb.types.key.Key"
    """<p>A map of attribute names to <code>AttributeValue</code> objects that specifies the primary key of the item to retrieve.</p>"""
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table from which to retrieve the specified item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes of the specified item to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes of the specified item are returned. If any of the requested attributes are not found, they do not appear in the result.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in the ProjectionExpression parameter.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Get) -> dict:
    out: dict = {}
    import capo_dynamodb.types.key

    out["Key"] = capo_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    out["TableName"] = value["table_name"]
    if "projection_expression" in value:
        out["ProjectionExpression"] = value["projection_expression"]
    if "expression_attribute_names" in value:
        import capo_dynamodb.types.expression_attribute_name_map

        out["ExpressionAttributeNames"] = (
            capo_dynamodb.types.expression_attribute_name_map.serialize_aws_json_1_0(
                value["expression_attribute_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Get:
    out: Get = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_dynamodb.types.key

        out["key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        out["key"] = {}
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("ProjectionExpression") is not None:
        out["projection_expression"] = data["ProjectionExpression"]
    if data.get("ExpressionAttributeNames") is not None:
        import capo_dynamodb.types.expression_attribute_name_map

        out["expression_attribute_names"] = (
            capo_dynamodb.types.expression_attribute_name_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeNames"]
            )
        )
    return out
