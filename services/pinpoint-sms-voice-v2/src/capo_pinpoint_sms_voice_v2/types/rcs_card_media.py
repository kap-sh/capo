"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsCardMedia``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_media_url


class RcsCardMedia(TypedDict, closed=True):
    file_url: "capo_pinpoint_sms_voice_v2.types.rcs_media_url.RcsMediaUrl"
    """<p>The S3 URI of the media file for the card, in the format <code>s3://bucket-name/key</code>. Maximum 2000 characters.</p>"""
    thumbnail_url: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_media_url.RcsMediaUrl"
    ]
    """<p>The S3 URI of an optional thumbnail image for the card media. Maximum 2000 characters.</p>"""
    height: NotRequired["str"]
    """<p>The display height of the media in the card. Valid values are SHORT, MEDIUM, and TALL.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsCardMedia) -> dict:
    out: dict = {}
    out["FileUrl"] = value["file_url"]
    if "thumbnail_url" in value:
        out["ThumbnailUrl"] = value["thumbnail_url"]
    if "height" in value:
        out["Height"] = value["height"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsCardMedia:
    out: RcsCardMedia = {}  # type: ignore[typeddict-item]
    if data.get("FileUrl") is not None:
        out["file_url"] = data["FileUrl"]
    else:
        out["file_url"] = ""
    if data.get("ThumbnailUrl") is not None:
        out["thumbnail_url"] = data["ThumbnailUrl"]
    if data.get("Height") is not None:
        out["height"] = data["Height"]
    return out
