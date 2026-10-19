"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RdsFieldMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.column_name


class RdsFieldMapping(TypedDict, closed=True):
    primary_key_field: "capo_bedrock_agent.types.column_name.ColumnName"
    """<p>The name of the field in which Amazon Bedrock stores the ID for each entry.</p>"""
    vector_field: "capo_bedrock_agent.types.column_name.ColumnName"
    """<p>The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.</p>"""
    text_field: "capo_bedrock_agent.types.column_name.ColumnName"
    """<p>The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.</p>"""
    metadata_field: "capo_bedrock_agent.types.column_name.ColumnName"
    """<p>The name of the field in which Amazon Bedrock stores metadata about the vector store.</p>"""
    custom_metadata_field: NotRequired[
        "capo_bedrock_agent.types.column_name.ColumnName"
    ]
    """<p>Provide a name for the universal metadata field where Amazon Bedrock will store any custom metadata from your data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RdsFieldMapping) -> dict:
    out: dict = {}
    out["primaryKeyField"] = value["primary_key_field"]
    out["vectorField"] = value["vector_field"]
    out["textField"] = value["text_field"]
    out["metadataField"] = value["metadata_field"]
    if "custom_metadata_field" in value:
        out["customMetadataField"] = value["custom_metadata_field"]
    return out


def deserialize_json(data: dict) -> RdsFieldMapping:
    out: RdsFieldMapping = {}  # type: ignore[typeddict-item]
    if data.get("primaryKeyField") is not None:
        out["primary_key_field"] = data["primaryKeyField"]
    else:
        out["primary_key_field"] = ""
    if data.get("vectorField") is not None:
        out["vector_field"] = data["vectorField"]
    else:
        out["vector_field"] = ""
    if data.get("textField") is not None:
        out["text_field"] = data["textField"]
    else:
        out["text_field"] = ""
    if data.get("metadataField") is not None:
        out["metadata_field"] = data["metadataField"]
    else:
        out["metadata_field"] = ""
    if data.get("customMetadataField") is not None:
        out["custom_metadata_field"] = data["customMetadataField"]
    return out
