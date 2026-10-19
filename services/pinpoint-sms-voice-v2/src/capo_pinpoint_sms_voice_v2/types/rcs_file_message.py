"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsFileMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_media_url


class RcsFileMessage(TypedDict, closed=True):
    file_url: "capo_pinpoint_sms_voice_v2.types.rcs_media_url.RcsMediaUrl"
    """<p>The S3 URI of the media file to send, in the format <code>s3://bucket-name/key</code>. The service downloads the file from your S3 bucket, rehosts it, and generates a presigned URL for the aggregator. Maximum 2000 characters.</p>"""
    thumbnail_url: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_media_url.RcsMediaUrl"
    ]
    """<p>The S3 URI of an optional thumbnail image for the media file, in the format <code>s3://bucket-name/key</code>. Maximum 2000 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsFileMessage) -> dict:
    out: dict = {}
    out["FileUrl"] = value["file_url"]
    if "thumbnail_url" in value:
        out["ThumbnailUrl"] = value["thumbnail_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsFileMessage:
    out: RcsFileMessage = {}  # type: ignore[typeddict-item]
    if data.get("FileUrl") is not None:
        out["file_url"] = data["FileUrl"]
    else:
        out["file_url"] = ""
    if data.get("ThumbnailUrl") is not None:
        out["thumbnail_url"] = data["ThumbnailUrl"]
    return out
