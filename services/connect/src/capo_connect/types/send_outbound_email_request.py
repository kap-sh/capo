"""Generated from Smithy shape ``com.amazonaws.connect#SendOutboundEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.email_address_info
    import capo_connect.types.instance_id
    import capo_connect.types.outbound_additional_recipients
    import capo_connect.types.outbound_email_content
    import capo_connect.types.source_campaign
    import capo_connect.types.traffic_type


class SendOutboundEmailRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    from_email_address: "capo_connect.types.email_address_info.EmailAddressInfo"
    """<p>The email address to be used for sending email.</p>"""
    destination_email_address: "capo_connect.types.email_address_info.EmailAddressInfo"
    """<p>The email address to send the email to.</p>"""
    additional_recipients: NotRequired[
        "capo_connect.types.outbound_additional_recipients.OutboundAdditionalRecipients"
    ]
    """<p>The additional recipients address of the email in CC.</p>"""
    email_message: "capo_connect.types.outbound_email_content.OutboundEmailContent"
    """<p>The email message body to be sent to the newly created email.</p>"""
    traffic_type: "capo_connect.types.traffic_type.TrafficType"
    """<p>Denotes the class of traffic.</p> <note> <p>Only the CAMPAIGN traffic type is supported.</p> </note>"""
    source_campaign: NotRequired["capo_connect.types.source_campaign.SourceCampaign"]
    """<p>A Campaign object need for Campaign traffic type.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendOutboundEmailRequest) -> dict:
    out: dict = {}
    import capo_connect.types.email_address_info

    out["FromEmailAddress"] = capo_connect.types.email_address_info.serialize_json(
        value["from_email_address"]
    )
    import capo_connect.types.email_address_info

    out["DestinationEmailAddress"] = (
        capo_connect.types.email_address_info.serialize_json(
            value["destination_email_address"]
        )
    )
    if "additional_recipients" in value:
        import capo_connect.types.outbound_additional_recipients

        out["AdditionalRecipients"] = (
            capo_connect.types.outbound_additional_recipients.serialize_json(
                value["additional_recipients"]
            )
        )
    import capo_connect.types.outbound_email_content

    out["EmailMessage"] = capo_connect.types.outbound_email_content.serialize_json(
        value["email_message"]
    )
    import capo_connect.types.traffic_type

    out["TrafficType"] = capo_connect.types.traffic_type.serialize_json(
        value["traffic_type"]
    )
    if "source_campaign" in value:
        import capo_connect.types.source_campaign

        out["SourceCampaign"] = capo_connect.types.source_campaign.serialize_json(
            value["source_campaign"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendOutboundEmailRequest:
    out: SendOutboundEmailRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromEmailAddress") is not None:
        import capo_connect.types.email_address_info

        out["from_email_address"] = (
            capo_connect.types.email_address_info.deserialize_json(
                data["FromEmailAddress"]
            )
        )
    else:
        raise DeserializationError(
            "SendOutboundEmailRequest.from_email_address required"
        )
    if data.get("DestinationEmailAddress") is not None:
        import capo_connect.types.email_address_info

        out["destination_email_address"] = (
            capo_connect.types.email_address_info.deserialize_json(
                data["DestinationEmailAddress"]
            )
        )
    else:
        raise DeserializationError(
            "SendOutboundEmailRequest.destination_email_address required"
        )
    if data.get("AdditionalRecipients") is not None:
        import capo_connect.types.outbound_additional_recipients

        out["additional_recipients"] = (
            capo_connect.types.outbound_additional_recipients.deserialize_json(
                data["AdditionalRecipients"]
            )
        )
    if data.get("EmailMessage") is not None:
        import capo_connect.types.outbound_email_content

        out["email_message"] = (
            capo_connect.types.outbound_email_content.deserialize_json(
                data["EmailMessage"]
            )
        )
    else:
        raise DeserializationError("SendOutboundEmailRequest.email_message required")
    if data.get("TrafficType") is not None:
        import capo_connect.types.traffic_type

        out["traffic_type"] = capo_connect.types.traffic_type.deserialize_json(
            data["TrafficType"]
        )
    else:
        raise DeserializationError("SendOutboundEmailRequest.traffic_type required")
    if data.get("SourceCampaign") is not None:
        import capo_connect.types.source_campaign

        out["source_campaign"] = capo_connect.types.source_campaign.deserialize_json(
            data["SourceCampaign"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
