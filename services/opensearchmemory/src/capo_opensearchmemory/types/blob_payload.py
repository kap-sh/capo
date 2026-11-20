"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BlobPayload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.blob_content_type
    import capo_opensearchmemory.types.blob_source


class BlobPayload(TypedDict, closed=True):
    content_type: "capo_opensearchmemory.types.blob_content_type.BlobContentType"
    """<p>The document's media type. Only <code>application/pdf</code> is supported. Any other value fails with <code>ValidationException</code>.</p>"""
    source: "capo_opensearchmemory.types.blob_source.BlobSource"
    """<p>The location of the document.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BlobPayload) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.blob_content_type

    out["contentType"] = (
        capo_opensearchmemory.types.blob_content_type.serialize_aws_json_1_0(
            value["content_type"]
        )
    )
    import capo_opensearchmemory.types.blob_source

    out["source"] = capo_opensearchmemory.types.blob_source.serialize_aws_json_1_0(
        value["source"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BlobPayload:
    out: BlobPayload = {}  # type: ignore[typeddict-item]
    if data.get("contentType") is not None:
        import capo_opensearchmemory.types.blob_content_type

        out["content_type"] = (
            capo_opensearchmemory.types.blob_content_type.deserialize_aws_json_1_0(
                data["contentType"]
            )
        )
    else:
        import typing

        out["content_type"] = typing.cast(
            "capo_opensearchmemory.types.blob_content_type.BlobContentType", ""
        )
    if data.get("source") is not None:
        import capo_opensearchmemory.types.blob_source

        out["source"] = (
            capo_opensearchmemory.types.blob_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: BlobPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        out["source"] = "*** Sensitive Data Redacted ***"
    return out
