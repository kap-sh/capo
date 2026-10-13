"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveMessageResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.envelope
    import capo_mailmanager.types.metadata
    import capo_mailmanager.types.s3_presigned_url


class GetArchiveMessageResponse(TypedDict, closed=True):
    message_download_link: NotRequired[
        "capo_mailmanager.types.s3_presigned_url.S3PresignedURL"
    ]
    """<p>A pre-signed URL to temporarily download the full message content.</p>"""
    metadata: NotRequired["capo_mailmanager.types.metadata.Metadata"]
    """<p>The metadata about the email.</p>"""
    envelope: NotRequired["capo_mailmanager.types.envelope.Envelope"]
    """<p>The SMTP envelope information of the email.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveMessageResponse) -> dict:
    out: dict = {}
    if "message_download_link" in value:
        out["MessageDownloadLink"] = value["message_download_link"]
    if "metadata" in value:
        import capo_mailmanager.types.metadata

        out["Metadata"] = capo_mailmanager.types.metadata.serialize_aws_json_1_0(
            value["metadata"]
        )
    if "envelope" in value:
        import capo_mailmanager.types.envelope

        out["Envelope"] = capo_mailmanager.types.envelope.serialize_aws_json_1_0(
            value["envelope"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveMessageResponse:
    out: GetArchiveMessageResponse = {}  # type: ignore[typeddict-item]
    if data.get("MessageDownloadLink") is not None:
        out["message_download_link"] = data["MessageDownloadLink"]
    if data.get("Metadata") is not None:
        import capo_mailmanager.types.metadata

        out["metadata"] = capo_mailmanager.types.metadata.deserialize_aws_json_1_0(
            data["Metadata"]
        )
    if data.get("Envelope") is not None:
        import capo_mailmanager.types.envelope

        out["envelope"] = capo_mailmanager.types.envelope.deserialize_aws_json_1_0(
            data["Envelope"]
        )
    return out


def redact_sensitive(value: GetArchiveMessageResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "metadata" in value:
        import capo_mailmanager.types.metadata

        out["metadata"] = capo_mailmanager.types.metadata.redact_sensitive(
            value["metadata"]
        )
    return out
