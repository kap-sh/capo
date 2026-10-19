"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SendDestinationNumberVerificationCodeResult``."""

from typing_extensions import TypedDict


class SendDestinationNumberVerificationCodeResult(TypedDict, closed=True):
    message_id: "str"
    """<p>The unique identifier for the message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendDestinationNumberVerificationCodeResult) -> dict:
    out: dict = {}
    out["MessageId"] = value["message_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendDestinationNumberVerificationCodeResult:
    out: SendDestinationNumberVerificationCodeResult = {}  # type: ignore[typeddict-item]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    else:
        out["message_id"] = ""
    return out
