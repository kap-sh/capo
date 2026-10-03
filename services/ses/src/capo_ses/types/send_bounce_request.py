"""Generated from Smithy shape ``com.amazonaws.ses#SendBounceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.address
    import capo_ses.types.amazon_resource_name
    import capo_ses.types.bounced_recipient_info_list
    import capo_ses.types.explanation
    import capo_ses.types.message_dsn
    import capo_ses.types.message_id


class SendBounceRequest(TypedDict, closed=True):
    original_message_id: "capo_ses.types.message_id.MessageId"
    """<p>The message ID of the message to be bounced.</p>"""
    bounce_sender: "capo_ses.types.address.Address"
    """<p>The address to use in the "From" header of the bounce message. This must be an identity that you have verified with Amazon SES.</p>"""
    explanation: NotRequired["capo_ses.types.explanation.Explanation"]
    """<p>Human-readable text for the bounce message to explain the failure. If not specified, the text is auto-generated based on the bounced recipient information.</p>"""
    message_dsn: NotRequired["capo_ses.types.message_dsn.MessageDsn"]
    """<p>Message-related DSN fields. If not specified, Amazon SES chooses the values.</p>"""
    bounced_recipient_info_list: (
        "capo_ses.types.bounced_recipient_info_list.BouncedRecipientInfoList"
    )
    """<p>A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one <code>BouncedRecipientInfo</code> in the list.</p>"""
    bounce_sender_arn: NotRequired[
        "capo_ses.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the "From" header of the bounce. For more information about sending authorization, see the <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html">Amazon SES Developer Guide</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SendBounceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}OriginalMessageId", str(value["original_message_id"])))
    pairs.append((f"{key_prefix}BounceSender", str(value["bounce_sender"])))
    if "explanation" in value:
        pairs.append((f"{key_prefix}Explanation", str(value["explanation"])))
    if "message_dsn" in value:
        import capo_ses.types.message_dsn

        capo_ses.types.message_dsn.serialize_query(
            value["message_dsn"], pairs, f"{key_prefix}MessageDsn"
        )
    import capo_ses.types.bounced_recipient_info_list

    capo_ses.types.bounced_recipient_info_list.serialize_query(
        value["bounced_recipient_info_list"],
        pairs,
        f"{key_prefix}BouncedRecipientInfoList",
    )
    if "bounce_sender_arn" in value:
        pairs.append((f"{key_prefix}BounceSenderArn", str(value["bounce_sender_arn"])))


def deserialize_query(el: Element) -> SendBounceRequest:
    out: SendBounceRequest = {}  # type: ignore[typeddict-item]
    child_original_message_id = el.find("OriginalMessageId")
    if child_original_message_id is not None:
        out["original_message_id"] = str(child_original_message_id.text or "")
    else:
        raise DeserializationError("SendBounceRequest.original_message_id required")
    child_bounce_sender = el.find("BounceSender")
    if child_bounce_sender is not None:
        out["bounce_sender"] = str(child_bounce_sender.text or "")
    else:
        raise DeserializationError("SendBounceRequest.bounce_sender required")
    child_explanation = el.find("Explanation")
    if child_explanation is not None:
        out["explanation"] = str(child_explanation.text or "")
    child_message_dsn = el.find("MessageDsn")
    if child_message_dsn is not None:
        import capo_ses.types.message_dsn

        out["message_dsn"] = capo_ses.types.message_dsn.deserialize_query(
            child_message_dsn
        )
    child_bounced_recipient_info_list = el.find("BouncedRecipientInfoList")
    if child_bounced_recipient_info_list is not None:
        import capo_ses.types.bounced_recipient_info_list

        out["bounced_recipient_info_list"] = (
            capo_ses.types.bounced_recipient_info_list.deserialize_query(
                child_bounced_recipient_info_list
            )
        )
    else:
        raise DeserializationError(
            "SendBounceRequest.bounced_recipient_info_list required"
        )
    child_bounce_sender_arn = el.find("BounceSenderArn")
    if child_bounce_sender_arn is not None:
        out["bounce_sender_arn"] = str(child_bounce_sender_arn.text or "")
    return out
