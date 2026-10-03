"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeysAndAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_name_list
    import capo_dynamodb.types.consistent_read
    import capo_dynamodb.types.expression_attribute_name_map
    import capo_dynamodb.types.key_list
    import capo_dynamodb.types.projection_expression


class KeysAndAttributes(TypedDict, closed=True):
    keys: "capo_dynamodb.types.key_list.KeyList"
    """<p>The primary key attribute values that define the items and the attributes associated with the items.</p>"""
    attributes_to_get: NotRequired[
        "capo_dynamodb.types.attribute_name_list.AttributeNameList"
    ]
    """<p>This is a legacy parameter. Use <code>ProjectionExpression</code> instead. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.html">Legacy Conditional Parameters</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    consistent_read: NotRequired["capo_dynamodb.types.consistent_read.ConsistentRead"]
    """<p>The consistency of a read operation. If set to <code>true</code>, then a strongly consistent read is used; otherwise, an eventually consistent read is used.</p>"""
    projection_expression: NotRequired[
        "capo_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the <code>ProjectionExpression</code> must be separated by commas.</p> <p>If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Accessing Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "capo_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. The following are some use cases for using <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p>To access an attribute whose name conflicts with a DynamoDB reserved word.</p> </li> <li> <p>To create a placeholder for repeating occurrences of an attribute name in an expression.</p> </li> <li> <p>To prevent special characters in an attribute name from being misinterpreted in an expression.</p> </li> </ul> <p>Use the <b>#</b> character in an expression to dereference an attribute name. For example, consider the following attribute name:</p> <ul> <li> <p> <code>Percentile</code> </p> </li> </ul> <p>The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ReservedWords.html">Reserved Words</a> in the <i>Amazon DynamoDB Developer Guide</i>). To work around this, you could specify the following for <code>ExpressionAttributeNames</code>:</p> <ul> <li> <p> <code>{"#P":"Percentile"}</code> </p> </li> </ul> <p>You could then use this substitution in an expression, as in this example:</p> <ul> <li> <p> <code>#P = :val</code> </p> </li> </ul> <note> <p>Tokens that begin with the <b>:</b> character are <i>expression attribute values</i>, which are placeholders for the actual value at runtime.</p> </note> <p>For more information on expression attribute names, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.AccessingItemAttributes.html">Accessing Item Attributes</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeysAndAttributes) -> dict:
    out: dict = {}
    import capo_dynamodb.types.key_list

    out["Keys"] = capo_dynamodb.types.key_list.serialize_aws_json_1_0(value["keys"])
    if "attributes_to_get" in value:
        import capo_dynamodb.types.attribute_name_list

        out["AttributesToGet"] = (
            capo_dynamodb.types.attribute_name_list.serialize_aws_json_1_0(
                value["attributes_to_get"]
            )
        )
    if "consistent_read" in value:
        out["ConsistentRead"] = value["consistent_read"]
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


def deserialize_aws_json_1_0(data: dict) -> KeysAndAttributes:
    out: KeysAndAttributes = {}  # type: ignore[typeddict-item]
    if data.get("Keys") is not None:
        import capo_dynamodb.types.key_list

        out["keys"] = capo_dynamodb.types.key_list.deserialize_aws_json_1_0(
            data["Keys"]
        )
    else:
        raise DeserializationError("KeysAndAttributes.keys required")
    if data.get("AttributesToGet") is not None:
        import capo_dynamodb.types.attribute_name_list

        out["attributes_to_get"] = (
            capo_dynamodb.types.attribute_name_list.deserialize_aws_json_1_0(
                data["AttributesToGet"]
            )
        )
    if data.get("ConsistentRead") is not None:
        out["consistent_read"] = data["ConsistentRead"]
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
