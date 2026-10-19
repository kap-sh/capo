"""Generated from Smithy shape ``com.amazonaws.iotevents#LambdaAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.payload


class LambdaAction(TypedDict, closed=True):
    function_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the Lambda function that is executed.</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]
    """<p>You can configure the action payload when you send a message to a Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaAction) -> dict:
    out: dict = {}
    out["functionArn"] = value["function_arn"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> LambdaAction:
    out: LambdaAction = {}  # type: ignore[typeddict-item]
    if data.get("functionArn") is not None:
        out["function_arn"] = data["functionArn"]
    else:
        out["function_arn"] = ""
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out
