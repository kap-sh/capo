"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.custom_document_identifier
    import capo_bedrock_agent.types.custom_s3_location
    import capo_bedrock_agent.types.custom_source_type
    import capo_bedrock_agent.types.inline_content


class CustomContent(TypedDict, closed=True):
    custom_document_identifier: (
        "capo_bedrock_agent.types.custom_document_identifier.CustomDocumentIdentifier"
    )
    """<p>A unique identifier for the document.</p>"""
    source_type: "capo_bedrock_agent.types.custom_source_type.CustomSourceType"
    """<p>The source of the data to ingest.</p>"""
    s3_location: NotRequired[
        "capo_bedrock_agent.types.custom_s3_location.CustomS3Location"
    ]
    """<p>Contains information about the Amazon S3 location of the file from which to ingest data.</p>"""
    inline_content: NotRequired["capo_bedrock_agent.types.inline_content.InlineContent"]
    """<p>Contains information about content defined inline to ingest into a knowledge base.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomContent) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.custom_document_identifier

    out["customDocumentIdentifier"] = (
        capo_bedrock_agent.types.custom_document_identifier.serialize_json(
            value["custom_document_identifier"]
        )
    )
    import capo_bedrock_agent.types.custom_source_type

    out["sourceType"] = capo_bedrock_agent.types.custom_source_type.serialize_json(
        value["source_type"]
    )
    if "s3_location" in value:
        import capo_bedrock_agent.types.custom_s3_location

        out["s3Location"] = capo_bedrock_agent.types.custom_s3_location.serialize_json(
            value["s3_location"]
        )
    if "inline_content" in value:
        import capo_bedrock_agent.types.inline_content

        out["inlineContent"] = capo_bedrock_agent.types.inline_content.serialize_json(
            value["inline_content"]
        )
    return out


def deserialize_json(data: dict) -> CustomContent:
    out: CustomContent = {}  # type: ignore[typeddict-item]
    if data.get("customDocumentIdentifier") is not None:
        import capo_bedrock_agent.types.custom_document_identifier

        out["custom_document_identifier"] = (
            capo_bedrock_agent.types.custom_document_identifier.deserialize_json(
                data["customDocumentIdentifier"]
            )
        )
    else:
        raise DeserializationError("CustomContent.custom_document_identifier required")
    if data.get("sourceType") is not None:
        import capo_bedrock_agent.types.custom_source_type

        out["source_type"] = (
            capo_bedrock_agent.types.custom_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_bedrock_agent.types.custom_source_type.CustomSourceType", ""
        )
    if data.get("s3Location") is not None:
        import capo_bedrock_agent.types.custom_s3_location

        out["s3_location"] = (
            capo_bedrock_agent.types.custom_s3_location.deserialize_json(
                data["s3Location"]
            )
        )
    if data.get("inlineContent") is not None:
        import capo_bedrock_agent.types.inline_content

        out["inline_content"] = (
            capo_bedrock_agent.types.inline_content.deserialize_json(
                data["inlineContent"]
            )
        )
    return out


def redact_sensitive(value: CustomContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_content" in value:
        import capo_bedrock_agent.types.inline_content

        out["inline_content"] = (
            capo_bedrock_agent.types.inline_content.redact_sensitive(
                value["inline_content"]
            )
        )
    return out
