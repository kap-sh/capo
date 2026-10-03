"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneySMSMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.message_type


class JourneySMSMessage(TypedDict, closed=True):
    message_type: NotRequired["capo_pinpoint.types.message_type.MessageType"]
    """<p>The SMS message type. Valid values are TRANSACTIONAL (for messages that are critical or time-sensitive, such as a one-time passwords) and PROMOTIONAL (for messsages that aren't critical or time-sensitive, such as marketing messages).</p>"""
    origination_number: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The long code to send the SMS message from. This value should be one of the dedicated long codes that's assigned to your AWS account. Although it isn't required, we recommend that you specify the long code using an E.164 format to ensure prompt and accurate delivery of the message. For example, +12065550100.</p>"""
    sender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The sender ID to display as the sender of the message on a recipient's device. Support for sender IDs varies by country or region. For more information, see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms-countries.html">Supported Countries and Regions</a> in the Amazon Pinpoint User Guide.</p>"""
    entity_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The entity ID or Principal Entity (PE) id received from the regulatory body for sending SMS in your country.</p>"""
    template_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The template ID received from the regulatory body for sending SMS in your country.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneySMSMessage) -> dict:
    out: dict = {}
    if "message_type" in value:
        import capo_pinpoint.types.message_type

        out["MessageType"] = capo_pinpoint.types.message_type.serialize_json(
            value["message_type"]
        )
    if "origination_number" in value:
        out["OriginationNumber"] = value["origination_number"]
    if "sender_id" in value:
        out["SenderId"] = value["sender_id"]
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    return out


def deserialize_json(data: dict) -> JourneySMSMessage:
    out: JourneySMSMessage = {}  # type: ignore[typeddict-item]
    if data.get("MessageType") is not None:
        import capo_pinpoint.types.message_type

        out["message_type"] = capo_pinpoint.types.message_type.deserialize_json(
            data["MessageType"]
        )
    if data.get("OriginationNumber") is not None:
        out["origination_number"] = data["OriginationNumber"]
    if data.get("SenderId") is not None:
        out["sender_id"] = data["SenderId"]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("TemplateId") is not None:
        out["template_id"] = data["TemplateId"]
    return out
