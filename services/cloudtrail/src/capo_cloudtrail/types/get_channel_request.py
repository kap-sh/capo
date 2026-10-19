"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_arn


class GetChannelRequest(TypedDict, closed=True):
    channel: "capo_cloudtrail.types.channel_arn.ChannelArn"
    """<p>The ARN or <code>UUID</code> of a channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetChannelRequest) -> dict:
    out: dict = {}
    out["Channel"] = value["channel"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetChannelRequest:
    out: GetChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        out["channel"] = data["Channel"]
    else:
        out["channel"] = ""
    return out
