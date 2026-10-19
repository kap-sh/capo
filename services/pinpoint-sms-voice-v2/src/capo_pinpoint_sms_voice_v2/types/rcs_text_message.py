"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsTextMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_text_body


class RcsTextMessage(TypedDict, closed=True):
    body: "capo_pinpoint_sms_voice_v2.types.rcs_text_body.RcsTextBody"
    """<p>The text body of the RCS message. Maximum 3072 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsTextMessage) -> dict:
    out: dict = {}
    out["Body"] = value["body"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsTextMessage:
    out: RcsTextMessage = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    else:
        out["body"] = ""
    return out
