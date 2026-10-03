"""Generated from Smithy shape ``com.amazonaws.dynamodb#KeySchemaElement``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.key_schema_attribute_name
    import capo_dynamodb.types.key_type


class KeySchemaElement(TypedDict, closed=True):
    attribute_name: (
        "capo_dynamodb.types.key_schema_attribute_name.KeySchemaAttributeName"
    )
    """<p>The name of a key attribute.</p>"""
    key_type: "capo_dynamodb.types.key_type.KeyType"
    """<p>The role that this key attribute will assume:</p> <ul> <li> <p> <code>HASH</code> - partition key</p> </li> <li> <p> <code>RANGE</code> - sort key</p> </li> </ul> <note> <p>The partition key of an item is also known as its <i>hash attribute</i>. The term "hash attribute" derives from DynamoDB's usage of an internal hash function to evenly distribute data items across partitions, based on their partition key values.</p> <p>The sort key of an item is also known as its <i>range attribute</i>. The term "range attribute" derives from the way DynamoDB stores items with the same partition key physically close together, in sorted order by the sort key value.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeySchemaElement) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_dynamodb.types.key_type

    out["KeyType"] = capo_dynamodb.types.key_type.serialize_aws_json_1_0(
        value["key_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeySchemaElement:
    out: KeySchemaElement = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("KeySchemaElement.attribute_name required")
    if data.get("KeyType") is not None:
        import capo_dynamodb.types.key_type

        out["key_type"] = capo_dynamodb.types.key_type.deserialize_aws_json_1_0(
            data["KeyType"]
        )
    else:
        raise DeserializationError("KeySchemaElement.key_type required")
    return out
