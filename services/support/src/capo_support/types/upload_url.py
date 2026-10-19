"""Generated from Smithy shape ``com.amazonaws.support#UploadUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.https_url
    import capo_support.types.integer
    import capo_support.types.validated_date_time


class UploadUrl(TypedDict, closed=True):
    url: "capo_support.types.https_url.HttpsUrl"
    """<p>The presigned HTTPS URL that you use to upload a single part with HTTP <code>PUT</code>. Upload URLs are served from <code>uploadv1.attachments.support.{region}.amazonaws.com</code>. The <code>uploadv1</code> prefix is subject to change.</p>"""
    part_index: "capo_support.types.integer.Integer"
    """<p>The index of the part that this URL uploads.</p>"""
    expiry_date: "capo_support.types.validated_date_time.ValidatedDateTime"
    """<p>The date and time, in ISO-8601 format, when the presigned URL expires. Upload the part before this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadUrl) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    out["partIndex"] = value.get("part_index", 0)
    out["expiryDate"] = value["expiry_date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadUrl:
    out: UploadUrl = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("partIndex") is not None:
        out["part_index"] = data["partIndex"]
    else:
        out["part_index"] = 0
    if data.get("expiryDate") is not None:
        out["expiry_date"] = data["expiryDate"]
    else:
        out["expiry_date"] = ""
    return out
