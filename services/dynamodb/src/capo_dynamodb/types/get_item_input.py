"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name_list
    import capo_dynamodb.types.consistent_read
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.key
    import capo_dynamodb.types.projection_expression
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.table_arn


class GetItemInput(TypedDict, closed=True):
    table_name: "capo_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table containing the requested item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    key: "capo_dynamodb.types.key.Key"
    """<p>A map of attribute names to <code>AttributeValue</code> objects, representing the primary key of the item to retrieve.</p> <p>For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.</p>"""
    attributes_to_get: NotRequired[
        "capo_dynamodb.types.attribute_name_list.AttributeNameList"
    ]
    """<p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.AttributesToGet.html">AttributesToGet</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    consistent_read: NotRequired["capo_dynamodb.types.consistent_read.ConsistentRead"]
    """<p>Determines the read consistency model: If set to <code>true</code>, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads.</p>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas.</p> <p>If no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Specifying Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetItemInput) -> dict:
    out: dict = {}
    out["TableName"] = value["table_name"]
    import capo_dynamodb.types.key

    out["Key"] = capo_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    if "attributes_to_get" in value:
        import capo_dynamodb.types.attribute_name_list

        out["AttributesToGet"] = (
            capo_dynamodb.types.attribute_name_list.serialize_aws_json_1_0(
                value["attributes_to_get"]
            )
        )
    if "consistent_read" in value:
        out["ConsistentRead"] = value["consistent_read"]
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
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


def deserialize_aws_json_1_0(data: dict) -> GetItemInput:
    out: GetItemInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("GetItemInput.table_name required")
    if data.get("Key") is not None:
        import capo_dynamodb.types.key

        out["key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        raise DeserializationError("GetItemInput.key required")
    if data.get("AttributesToGet") is not None:
        import capo_dynamodb.types.attribute_name_list

        out["attributes_to_get"] = (
            capo_dynamodb.types.attribute_name_list.deserialize_aws_json_1_0(
                data["AttributesToGet"]
            )
        )
    if data.get("ConsistentRead") is not None:
        out["consistent_read"] = data["ConsistentRead"]
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
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
