"""Generated from Smithy shape ``com.amazonaws.bedrock#MetadataAttributeSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.attribute_type


class MetadataAttributeSchema(TypedDict, closed=True):
    key: "str"
    """<p>The unique identifier for the metadata attribute. This key is used to reference the attribute in filter expressions and reranking configurations.</p>"""
    type: "capo_bedrock.types.attribute_type.AttributeType"
    """<p>The data type of the metadata attribute. The type determines how the attribute can be used in filter expressions and reranking.</p>"""
    description: "str"
    """<p>An optional description of the metadata attribute that provides additional context about its purpose and usage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeSchema) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock.types.attribute_type

    out["type"] = capo_bedrock.types.attribute_type.serialize_json(value["type"])
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> MetadataAttributeSchema:
    out: MetadataAttributeSchema = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("type") is not None:
        import capo_bedrock.types.attribute_type

        out["type"] = capo_bedrock.types.attribute_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_bedrock.types.attribute_type.AttributeType", "")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
