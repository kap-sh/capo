"""Generated from Smithy shape ``com.amazonaws.dynamodb#AttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.key_schema_attribute_name
    import capo_dynamodb.types.scalar_attribute_type


class AttributeDefinition(TypedDict, closed=True):
    attribute_name: (
        "capo_dynamodb.types.key_schema_attribute_name.KeySchemaAttributeName"
    )
    """<p>A name for the attribute.</p>"""
    attribute_type: "capo_dynamodb.types.scalar_attribute_type.ScalarAttributeType"
    """<p>The data type for the attribute, where:</p> <ul> <li> <p> <code>S</code> - the attribute is of type String</p> </li> <li> <p> <code>N</code> - the attribute is of type Number</p> </li> <li> <p> <code>B</code> - the attribute is of type Binary</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttributeDefinition) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_dynamodb.types.scalar_attribute_type

    out["AttributeType"] = (
        capo_dynamodb.types.scalar_attribute_type.serialize_aws_json_1_0(
            value["attribute_type"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AttributeDefinition:
    out: AttributeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("AttributeType") is not None:
        import capo_dynamodb.types.scalar_attribute_type

        out["attribute_type"] = (
            capo_dynamodb.types.scalar_attribute_type.deserialize_aws_json_1_0(
                data["AttributeType"]
            )
        )
    else:
        import typing

        out["attribute_type"] = typing.cast(
            "capo_dynamodb.types.scalar_attribute_type.ScalarAttributeType", ""
        )
    return out
