"""Generated from Smithy shape ``com.amazonaws.bedrock#ExternalSource``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.byte_content_doc
    import capo_bedrock.types.external_source_type
    import capo_bedrock.types.s3_object_doc


class ExternalSource(TypedDict, closed=True):
    source_type: "capo_bedrock.types.external_source_type.ExternalSourceType"
    """<p>The source type of the external source wrapper object.</p>"""
    s3_location: NotRequired["capo_bedrock.types.s3_object_doc.S3ObjectDoc"]
    """<p>The S3 location of the external source wrapper object.</p>"""
    byte_content: NotRequired["capo_bedrock.types.byte_content_doc.ByteContentDoc"]
    """<p>The identifier, content type, and data of the external source wrapper object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSource) -> dict:
    out: dict = {}
    import capo_bedrock.types.external_source_type

    out["sourceType"] = capo_bedrock.types.external_source_type.serialize_json(
        value["source_type"]
    )
    if "s3_location" in value:
        import capo_bedrock.types.s3_object_doc

        out["s3Location"] = capo_bedrock.types.s3_object_doc.serialize_json(
            value["s3_location"]
        )
    if "byte_content" in value:
        import capo_bedrock.types.byte_content_doc

        out["byteContent"] = capo_bedrock.types.byte_content_doc.serialize_json(
            value["byte_content"]
        )
    return out


def deserialize_json(data: dict) -> ExternalSource:
    out: ExternalSource = {}  # type: ignore[typeddict-item]
    if data.get("sourceType") is not None:
        import capo_bedrock.types.external_source_type

        out["source_type"] = capo_bedrock.types.external_source_type.deserialize_json(
            data["sourceType"]
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_bedrock.types.external_source_type.ExternalSourceType", ""
        )
    if data.get("s3Location") is not None:
        import capo_bedrock.types.s3_object_doc

        out["s3_location"] = capo_bedrock.types.s3_object_doc.deserialize_json(
            data["s3Location"]
        )
    if data.get("byteContent") is not None:
        import capo_bedrock.types.byte_content_doc

        out["byte_content"] = capo_bedrock.types.byte_content_doc.deserialize_json(
            data["byteContent"]
        )
    return out


def redact_sensitive(value: ExternalSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "byte_content" in value:
        import capo_bedrock.types.byte_content_doc

        out["byte_content"] = capo_bedrock.types.byte_content_doc.redact_sensitive(
            value["byte_content"]
        )
    return out
