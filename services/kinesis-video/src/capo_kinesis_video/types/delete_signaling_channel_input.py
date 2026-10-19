"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DeleteSignalingChannelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.version


class DeleteSignalingChannelInput(TypedDict, closed=True):
    channel_arn: "capo_kinesis_video.types.resource_arn.ResourceARN"
    """<p>The Amazon Resource Name (ARN) of the signaling channel that you want to delete.</p>"""
    current_version: NotRequired["capo_kinesis_video.types.version.Version"]
    """<p>The current version of the signaling channel that you want to delete. You can obtain the current version by invoking the <code>DescribeSignalingChannel</code> or <code>ListSignalingChannels</code> API operations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSignalingChannelInput) -> dict:
    out: dict = {}
    out["ChannelARN"] = value["channel_arn"]
    if "current_version" in value:
        out["CurrentVersion"] = value["current_version"]
    return out


def deserialize_json(data: dict) -> DeleteSignalingChannelInput:
    out: DeleteSignalingChannelInput = {}  # type: ignore[typeddict-item]
    if data.get("ChannelARN") is not None:
        out["channel_arn"] = data["ChannelARN"]
    else:
        out["channel_arn"] = ""
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    return out
