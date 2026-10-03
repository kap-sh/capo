"""Generated from Smithy shape ``com.amazonaws.iot#IotAnalyticsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.batch_mode
    import capo_iot.types.channel_name


class IotAnalyticsAction(TypedDict, closed=True):
    channel_arn: NotRequired["capo_iot.types.aws_arn.AwsArn"]
    """<p>(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.</p>"""
    channel_name: NotRequired["capo_iot.types.channel_name.ChannelName"]
    """<p>The name of the IoT Analytics channel to which message data will be sent.</p>"""
    batch_mode: NotRequired["capo_iot.types.batch_mode.BatchMode"]
    """<p>Whether to process the action as a batch. The default value is <code>false</code>.</p> <p>When <code>batchMode</code> is <code>true</code> and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by <a href="https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage.html"> <code>BatchPutMessage</code> </a> to the IoT Analytics channel. The resulting array can't have more than 100 messages.</p>"""
    role_arn: NotRequired["capo_iot.types.aws_arn.AwsArn"]
    """<p>The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotAnalyticsAction) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["channelArn"] = value["channel_arn"]
    if "channel_name" in value:
        out["channelName"] = value["channel_name"]
    if "batch_mode" in value:
        out["batchMode"] = value["batch_mode"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IotAnalyticsAction:
    out: IotAnalyticsAction = {}  # type: ignore[typeddict-item]
    if data.get("channelArn") is not None:
        out["channel_arn"] = data["channelArn"]
    if data.get("channelName") is not None:
        out["channel_name"] = data["channelName"]
    if data.get("batchMode") is not None:
        out["batch_mode"] = data["batchMode"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
