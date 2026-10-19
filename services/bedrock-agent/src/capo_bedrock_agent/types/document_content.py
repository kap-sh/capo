"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.content_data_source_type
    import capo_bedrock_agent.types.custom_content
    import capo_bedrock_agent.types.s3_content


class DocumentContent(TypedDict, closed=True):
    data_source_type: (
        "capo_bedrock_agent.types.content_data_source_type.ContentDataSourceType"
    )
    """<p>The type of data source that is connected to the knowledge base to which to ingest this document.</p>"""
    custom: NotRequired["capo_bedrock_agent.types.custom_content.CustomContent"]
    """<p>Contains information about the content to ingest into a knowledge base connected to a custom data source.</p>"""
    s3: NotRequired["capo_bedrock_agent.types.s3_content.S3Content"]
    """<p>Contains information about the content to ingest into a knowledge base connected to an Amazon S3 data source</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContent) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.content_data_source_type

    out["dataSourceType"] = (
        capo_bedrock_agent.types.content_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    if "custom" in value:
        import capo_bedrock_agent.types.custom_content

        out["custom"] = capo_bedrock_agent.types.custom_content.serialize_json(
            value["custom"]
        )
    if "s3" in value:
        import capo_bedrock_agent.types.s3_content

        out["s3"] = capo_bedrock_agent.types.s3_content.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> DocumentContent:
    out: DocumentContent = {}  # type: ignore[typeddict-item]
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
    if data.get("custom") is not None:
        import capo_bedrock_agent.types.custom_content

        out["custom"] = capo_bedrock_agent.types.custom_content.deserialize_json(
            data["custom"]
        )
    if data.get("s3") is not None:
        import capo_bedrock_agent.types.s3_content

        out["s3"] = capo_bedrock_agent.types.s3_content.deserialize_json(data["s3"])
    return out


def redact_sensitive(value: DocumentContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom" in value:
        import capo_bedrock_agent.types.custom_content

        out["custom"] = capo_bedrock_agent.types.custom_content.redact_sensitive(
            value["custom"]
        )
    return out
