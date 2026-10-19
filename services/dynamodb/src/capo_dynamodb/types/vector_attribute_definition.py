"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorAttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.vector_attribute_name


class VectorAttributeDefinition(TypedDict, closed=True):
    attribute_name: "capo_dynamodb.types.vector_attribute_name.VectorAttributeName"
    """<p>The name of the vector attribute.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VectorAttributeDefinition) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorAttributeDefinition:
    out: VectorAttributeDefinition = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    return out
