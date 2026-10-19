"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.byte_content_file
    import capo_bedrock_agent_runtime.types.file_source_type
    import capo_bedrock_agent_runtime.types.s3_object_file


class FileSource(TypedDict, closed=True):
    source_type: "capo_bedrock_agent_runtime.types.file_source_type.FileSourceType"
    """<p>The source type of the files to attach.</p>"""
    s3_location: NotRequired[
        "capo_bedrock_agent_runtime.types.s3_object_file.S3ObjectFile"
    ]
    """<p>The s3 location of the files to attach.</p>"""
    byte_content: NotRequired[
        "capo_bedrock_agent_runtime.types.byte_content_file.ByteContentFile"
    ]
    """<p>The data and the text of the attached files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSource) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.file_source_type

    out["sourceType"] = (
        capo_bedrock_agent_runtime.types.file_source_type.serialize_json(
            value["source_type"]
        )
    )
    if "s3_location" in value:
        import capo_bedrock_agent_runtime.types.s3_object_file

        out["s3Location"] = (
            capo_bedrock_agent_runtime.types.s3_object_file.serialize_json(
                value["s3_location"]
            )
        )
    if "byte_content" in value:
        import capo_bedrock_agent_runtime.types.byte_content_file

        out["byteContent"] = (
            capo_bedrock_agent_runtime.types.byte_content_file.serialize_json(
                value["byte_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileSource:
    out: FileSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceType") is not None:
        import capo_bedrock_agent_runtime.types.file_source_type

        out["source_type"] = (
            capo_bedrock_agent_runtime.types.file_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_bedrock_agent_runtime.types.file_source_type.FileSourceType", ""
        )
    if data.get("s3Location") is not None:
        import capo_bedrock_agent_runtime.types.s3_object_file

        out["s3_location"] = (
            capo_bedrock_agent_runtime.types.s3_object_file.deserialize_json(
                data["s3Location"]
            )
        )
    if data.get("byteContent") is not None:
        import capo_bedrock_agent_runtime.types.byte_content_file

        out["byte_content"] = (
            capo_bedrock_agent_runtime.types.byte_content_file.deserialize_json(
                data["byteContent"]
            )
        )
    return out


def redact_sensitive(value: FileSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "byte_content" in value:
        import capo_bedrock_agent_runtime.types.byte_content_file

        out["byte_content"] = (
            capo_bedrock_agent_runtime.types.byte_content_file.redact_sensitive(
                value["byte_content"]
            )
        )
    return out
