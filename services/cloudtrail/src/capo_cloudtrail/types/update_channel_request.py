"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.channel_arn
    import capo_cloudtrail.types.channel_name
    import capo_cloudtrail.types.destinations


class UpdateChannelRequest(TypedDict, closed=True):
    channel: "capo_cloudtrail.types.channel_arn.ChannelArn"
    """<p>The ARN or ID (the ARN suffix) of the channel that you want to update.</p>"""
    destinations: NotRequired["capo_cloudtrail.types.destinations.Destinations"]
    """<p>The ARNs of event data stores that you want to log events arriving through the channel.</p>"""
    name: NotRequired["capo_cloudtrail.types.channel_name.ChannelName"]
    """<p> Changes the name of the channel. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateChannelRequest) -> dict:
    out: dict = {}
    out["Channel"] = value["channel"]
    if "destinations" in value:
        import capo_cloudtrail.types.destinations

        out["Destinations"] = capo_cloudtrail.types.destinations.serialize_aws_json_1_1(
            value["destinations"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateChannelRequest:
    out: UpdateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("Channel") is not None:
        out["channel"] = data["Channel"]
    else:
        out["channel"] = ""
    if data.get("Destinations") is not None:
        import capo_cloudtrail.types.destinations

        out["destinations"] = (
            capo_cloudtrail.types.destinations.deserialize_aws_json_1_1(
                data["Destinations"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
