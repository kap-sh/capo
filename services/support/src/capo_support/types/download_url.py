"""Generated from Smithy shape ``com.amazonaws.support#DownloadUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.https_url
    import capo_support.types.validated_date_time


class DownloadUrl(TypedDict, closed=True):
    url: "capo_support.types.https_url.HttpsUrl"
    """<p>The presigned HTTPS URL that you can use to download the attachment. Download URLs are served from <code>downloadv1.attachments.support.{region}.amazonaws.com</code>. The <code>downloadv1</code> prefix is subject to change.</p>"""
    expiry_date: "capo_support.types.validated_date_time.ValidatedDateTime"
    """<p>The date and time, in ISO-8601 format, when the presigned URL expires. Download the attachment before this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DownloadUrl) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    out["expiryDate"] = value["expiry_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DownloadUrl:
    out: DownloadUrl = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("expiryDate") is not None:
        out["expiry_date"] = data["expiryDate"]
    else:
        out["expiry_date"] = ""
    return out
