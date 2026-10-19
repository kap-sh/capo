"""Generated from Smithy shape ``com.amazonaws.support#GetAttachmentDownloadLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.download_url
    import capo_support.types.file_name


class GetAttachmentDownloadLinkResponse(TypedDict, closed=True):
    file_name: "capo_support.types.file_name.FileName"
    """<p>The name of the attachment file, including the file extension.</p>"""
    download_url: "capo_support.types.download_url.DownloadUrl"
    """<p>The presigned download URL and the date and time the URL expires.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAttachmentDownloadLinkResponse) -> dict:
    out: dict = {}
    out["fileName"] = value["file_name"]
    import capo_support.types.download_url

    out["downloadUrl"] = capo_support.types.download_url.serialize_aws_json_1_1(
        value["download_url"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAttachmentDownloadLinkResponse:
    out: GetAttachmentDownloadLinkResponse = {}  # type: ignore[typeddict-item]
    if data.get("fileName") is not None:
        out["file_name"] = data["fileName"]
    else:
        out["file_name"] = ""
    if data.get("downloadUrl") is not None:
        import capo_support.types.download_url

        out["download_url"] = capo_support.types.download_url.deserialize_aws_json_1_1(
            data["downloadUrl"]
        )
    else:
        raise DeserializationError(
            "GetAttachmentDownloadLinkResponse.download_url required"
        )
    return out
