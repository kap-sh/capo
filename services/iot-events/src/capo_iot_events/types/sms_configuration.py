"""Generated from Smithy shape ``com.amazonaws.iotevents#SMSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.notification_additional_message
    import capo_iot_events.types.recipient_details
    import capo_iot_events.types.sms_sender_id


class SMSConfiguration(TypedDict, closed=True):
    sender_id: NotRequired["capo_iot_events.types.sms_sender_id.SMSSenderId"]
    """<p>The sender ID.</p>"""
    additional_message: NotRequired[
        "capo_iot_events.types.notification_additional_message.NotificationAdditionalMessage"
    ]
    """<p>The message that you want to send. The message can be up to 200 characters.</p>"""
    recipients: "capo_iot_events.types.recipient_details.RecipientDetails"
    """<p>Specifies one or more recipients who receive the message.</p> <important> <p>You must <a href="https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html">add the users that receive SMS messages to your AWS SSO store</a>.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSConfiguration) -> dict:
    out: dict = {}
    if "sender_id" in value:
        out["senderId"] = value["sender_id"]
    if "additional_message" in value:
        out["additionalMessage"] = value["additional_message"]
    import capo_iot_events.types.recipient_details

    out["recipients"] = capo_iot_events.types.recipient_details.serialize_json(
        value["recipients"]
    )
    return out


def deserialize_json(data: dict) -> SMSConfiguration:
    out: SMSConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("senderId") is not None:
        out["sender_id"] = data["senderId"]
    if data.get("additionalMessage") is not None:
        out["additional_message"] = data["additionalMessage"]
    if data.get("recipients") is not None:
        import capo_iot_events.types.recipient_details

        out["recipients"] = capo_iot_events.types.recipient_details.deserialize_json(
            data["recipients"]
        )
    else:
        raise DeserializationError("SMSConfiguration.recipients required")
    return out
