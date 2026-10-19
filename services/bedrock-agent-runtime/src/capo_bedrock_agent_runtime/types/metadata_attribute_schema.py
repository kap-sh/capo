"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MetadataAttributeSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.attribute_type


class MetadataAttributeSchema(TypedDict, closed=True):
    key: "str"
    """<p>The attribute's key.</p>"""
    type: "capo_bedrock_agent_runtime.types.attribute_type.AttributeType"
    """<p>The attribute's type.</p>"""
    description: "str"
    """<p>The attribute's description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeSchema) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agent_runtime.types.attribute_type

    out["type"] = capo_bedrock_agent_runtime.types.attribute_type.serialize_json(
        value["type"]
    )
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> MetadataAttributeSchema:
    out: MetadataAttributeSchema = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("type") is not None:
        import capo_bedrock_agent_runtime.types.attribute_type

        out["type"] = capo_bedrock_agent_runtime.types.attribute_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.attribute_type.AttributeType", ""
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
