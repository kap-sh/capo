"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PineconeFieldMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.field_name


class PineconeFieldMapping(TypedDict, closed=True):
    text_field: "capo_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.</p>"""
    metadata_field: "capo_bedrock_agent.types.field_name.FieldName"
    """<p>The name of the field in which Amazon Bedrock stores metadata about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PineconeFieldMapping) -> dict:
    out: dict = {}
    out["textField"] = value["text_field"]
    out["metadataField"] = value["metadata_field"]
    return out


def deserialize_json(data: dict) -> PineconeFieldMapping:
    out: PineconeFieldMapping = {}  # type: ignore[typeddict-item]
    if data.get("textField") is not None:
        out["text_field"] = data["textField"]
    else:
        out["text_field"] = ""
    if data.get("metadataField") is not None:
        out["metadata_field"] = data["metadataField"]
    else:
        out["metadata_field"] = ""
    return out
