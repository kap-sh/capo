"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.content_data_source_type
    import capo_bedrock_agent.types.custom_document_identifier
    import capo_bedrock_agent.types.s3_location


class DocumentIdentifier(TypedDict, closed=True):
    data_source_type: (
        "capo_bedrock_agent.types.content_data_source_type.ContentDataSourceType"
    )
    """<p>The type of data source connected to the knowledge base that contains the document.</p>"""
    s3: NotRequired["capo_bedrock_agent.types.s3_location.S3Location"]
    """<p>Contains information that identifies the document in an S3 data source.</p>"""
    custom: NotRequired[
        "capo_bedrock_agent.types.custom_document_identifier.CustomDocumentIdentifier"
    ]
    """<p>Contains information that identifies the document in a custom data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentIdentifier) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.content_data_source_type

    out["dataSourceType"] = (
        capo_bedrock_agent.types.content_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    if "s3" in value:
        import capo_bedrock_agent.types.s3_location

        out["s3"] = capo_bedrock_agent.types.s3_location.serialize_json(value["s3"])
    if "custom" in value:
        import capo_bedrock_agent.types.custom_document_identifier

        out["custom"] = (
            capo_bedrock_agent.types.custom_document_identifier.serialize_json(
                value["custom"]
            )
        )
    return out


def deserialize_json(data: dict) -> DocumentIdentifier:
    out: DocumentIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("dataSourceType") is not None:
        import capo_bedrock_agent.types.content_data_source_type

        out["data_source_type"] = (
            capo_bedrock_agent.types.content_data_source_type.deserialize_json(
                data["dataSourceType"]
            )
        )
    else:
        import typing

        out["data_source_type"] = typing.cast(
            "capo_bedrock_agent.types.content_data_source_type.ContentDataSourceType",
            "",
        )
    if data.get("s3") is not None:
        import capo_bedrock_agent.types.s3_location

        out["s3"] = capo_bedrock_agent.types.s3_location.deserialize_json(data["s3"])
    if data.get("custom") is not None:
        import capo_bedrock_agent.types.custom_document_identifier

        out["custom"] = (
            capo_bedrock_agent.types.custom_document_identifier.deserialize_json(
                data["custom"]
            )
        )
    return out
