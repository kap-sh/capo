"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#ConfigurationSetInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.configuration_set_name
    import capo_pinpoint_sms_voice_v2.types.event_destination_list
    import capo_pinpoint_sms_voice_v2.types.message_type
    import capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn
    import capo_pinpoint_sms_voice_v2.types.sender_id


class ConfigurationSetInformation(TypedDict, closed=True):
    configuration_set_arn: "str"
    """<p>The Resource Name (ARN) of the ConfigurationSet.</p>"""
    configuration_set_name: (
        "capo_pinpoint_sms_voice_v2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the ConfigurationSet.</p>"""
    event_destinations: (
        "capo_pinpoint_sms_voice_v2.types.event_destination_list.EventDestinationList"
    )
    """<p>An array of EventDestination objects that describe any events to log and where to log them.</p>"""
    default_message_type: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.message_type.MessageType"
    ]
    """<p>The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive.</p>"""
    default_sender_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.sender_id.SenderId"
    ]
    """<p>The default sender ID used by the ConfigurationSet.</p>"""
    default_message_feedback_enabled: NotRequired["bool"]
    """<p>True if message feedback is enabled.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the ConfigurationSet was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""
    protect_configuration_id: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.protect_configuration_id_or_arn.ProtectConfigurationIdOrArn"
    ]
    """<p>The unique identifier for the protect configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConfigurationSetInformation) -> dict:
    out: dict = {}
    out["ConfigurationSetArn"] = value["configuration_set_arn"]
    out["ConfigurationSetName"] = value["configuration_set_name"]
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
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    if "protect_configuration_id" in value:
        out["ProtectConfigurationId"] = value["protect_configuration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ConfigurationSetInformation:
    out: ConfigurationSetInformation = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetArn") is not None:
        out["configuration_set_arn"] = data["ConfigurationSetArn"]
    else:
        raise DeserializationError(
            "ConfigurationSetInformation.configuration_set_arn required"
        )
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        raise DeserializationError(
            "ConfigurationSetInformation.configuration_set_name required"
        )
    if data.get("EventDestinations") is not None:
        import capo_pinpoint_sms_voice_v2.types.event_destination_list

        out["event_destinations"] = (
            capo_pinpoint_sms_voice_v2.types.event_destination_list.deserialize_aws_json_1_0(
                data["EventDestinations"]
            )
        )
    else:
        raise DeserializationError(
            "ConfigurationSetInformation.event_destinations required"
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
    else:
        raise DeserializationError(
            "ConfigurationSetInformation.created_timestamp required"
        )
    if data.get("ProtectConfigurationId") is not None:
        out["protect_configuration_id"] = data["ProtectConfigurationId"]
    return out
