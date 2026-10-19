"""Generated from Smithy shape ``com.amazonaws.iotevents#SNSTopicPublishAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.payload


class SNSTopicPublishAction(TypedDict, closed=True):
    target_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Amazon SNS target where the message is sent.</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message as an Amazon SNS push notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SNSTopicPublishAction) -> dict:
    out: dict = {}
    out["targetArn"] = value["target_arn"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> SNSTopicPublishAction:
    out: SNSTopicPublishAction = {}  # type: ignore[typeddict-item]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        out["target_arn"] = ""
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out
