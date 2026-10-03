"""Generated from Smithy shape ``com.amazonaws.iot#IotEventsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.batch_mode
    import capo_iot.types.input_name
    import capo_iot.types.message_id


class IotEventsAction(TypedDict, closed=True):
    input_name: "capo_iot.types.input_name.InputName"
    """<p>The name of the IoT Events input.</p>"""
    message_id: NotRequired["capo_iot.types.message_id.MessageId"]
    """<p>The ID of the message. The default <code>messageId</code> is a new UUID value.</p> <p>When <code>batchMode</code> is <code>true</code>, you can't specify a <code>messageId</code>--a new UUID value will be assigned.</p> <p>Assign a value to this property to ensure that only one input (message) with a given <code>messageId</code> will be processed by an IoT Events detector.</p>"""
    batch_mode: NotRequired["capo_iot.types.batch_mode.BatchMode"]
    """<p>Whether to process the event actions as a batch. The default value is <code>false</code>.</p> <p>When <code>batchMode</code> is <code>true</code>, you can't specify a <code>messageId</code>. </p> <p>When <code>batchMode</code> is <code>true</code> and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when it's sent to IoT Events by calling <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html"> <code>BatchPutMessage</code> </a>. The resulting array can't have more than 10 messages.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the role that grants IoT permission to send an input to an IoT Events detector. ("Action":"iotevents:BatchPutMessage").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IotEventsAction) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "batch_mode" in value:
        out["batchMode"] = value["batch_mode"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IotEventsAction:
    out: IotEventsAction = {}  # type: ignore[typeddict-item]
    if data.get("inputName") is not None:
        out["input_name"] = data["inputName"]
    else:
        raise DeserializationError("IotEventsAction.input_name required")
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    if data.get("batchMode") is not None:
        out["batch_mode"] = data["batchMode"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("IotEventsAction.role_arn required")
    return out
