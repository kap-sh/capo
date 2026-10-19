"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#SetDefaultMessageFeedbackEnabledRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn


class SetDefaultMessageFeedbackEnabledRequest(TypedDict, closed=True):
    configuration_set_name: "capo_pinpoint_sms_voice_v2.types.configuration_set_name_or_arn.ConfigurationSetNameOrArn"
    """<p>The name of the configuration set to use. This can be either the ConfigurationSetName or ConfigurationSetArn.</p>"""
    message_feedback_enabled: "bool"
    """<p>Set to true to enable message feedback.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetDefaultMessageFeedbackEnabledRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    out["MessageFeedbackEnabled"] = value["message_feedback_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetDefaultMessageFeedbackEnabledRequest:
    out: SetDefaultMessageFeedbackEnabledRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        out["configuration_set_name"] = ""
    if data.get("MessageFeedbackEnabled") is not None:
        out["message_feedback_enabled"] = data["MessageFeedbackEnabled"]
    else:
        out["message_feedback_enabled"] = False
    return out
