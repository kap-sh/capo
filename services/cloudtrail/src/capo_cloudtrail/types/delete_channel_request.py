"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_arn


class DeleteChannelRequest(TypedDict, closed=True):
    channel: "capo_cloudtrail.types.channel_arn.ChannelArn"
    """<p>The ARN or the <code>UUID</code> value of the channel that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteChannelRequest) -> dict:
    out: dict = {}
    out["Channel"] = value["channel"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteChannelRequest:
    out: DeleteChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        out["channel"] = data["Channel"]
    else:
        out["channel"] = ""
    return out
