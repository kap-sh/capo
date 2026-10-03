"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteConfigurationSetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.configuration_set_name
    import capo_pinpoint_sms_voice_v2.types.event_destination_list
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.sender_id


class DeleteConfigurationSetResult(TypedDict, closed=True):
    configuration_set_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the deleted configuration set.</p>"""
    configuration_set_name: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the deleted configuration set.</p>"""
    event_destinations: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.event_destination_list.EventDestinationList"
    ]
    """<p>An array of any EventDestination objects that were associated with the deleted configuration set.</p>"""
    default_message_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The default message type of the configuration set that was deleted.</p>"""
    default_sender_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId"
    ]
    """<p>The default Sender ID of the configuration set that was deleted.</p>"""
    default_message_feedback_enabled: NotRequired["bool"]
    """<p>True if the configuration set has message feedback enabled. By default this is set to false. </p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The time that the deleted configuration set was created in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConfigurationSetResult) -> dict:
    out: dict = {}
    if "configuration_set_arn" in value:
        out["ConfigurationSetArn"] = value["configuration_set_arn"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "event_destinations" in value:
        import capo_pinpoint_sms_voice_v2.types.event_destination_list

        out["EventDestinations"] = (
            capo_pinpoint_sms_voice_v2.types.event_destination_list.serialize_aws_json_1_0(
                value["event_destinations"]
            )
        )
    if "default_message_type" in value:
        out["DefaultMessageType"] = value["default_message_type"]
    if "default_sender_id" in value:
        out["DefaultSenderId"] = value["default_sender_id"]
    if "default_message_feedback_enabled" in value:
        out["DefaultMessageFeedbackEnabled"] = value["default_message_feedback_enabled"]
    if "created_timestamp" in value:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConfigurationSetResult:
    out: DeleteConfigurationSetResult = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetArn") is not None:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("EventDestinations") is not None:
        import capo_pinpoint_sms_voice_v2.types.event_destination_list

        out["event_destinations"] = (
            capo_pinpoint_sms_voice_v2.types.event_destination_list.deserialize_aws_json_1_0(
                data["EventDestinations"]
            )
        )
    if data.get("DefaultMessageType") is not None:
        out["default_message_type"] = data["DefaultMessageType"]
    if data.get("DefaultSenderId") is not None:
        out["default_sender_id"] = data["DefaultSenderId"]
    if data.get("DefaultMessageFeedbackEnabled") is not None:
        out["default_message_feedback_enabled"] = data["DefaultMessageFeedbackEnabled"]
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    return out
