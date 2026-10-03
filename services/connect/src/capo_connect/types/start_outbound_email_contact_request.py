"""Generated from Smithy shape ``com.amazonaws.connect#StartOutboundEmailContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.email_address_info
    import capo_connect.types.instance_id
    import capo_connect.types.outbound_additional_recipients
    import capo_connect.types.outbound_email_content


class StartOutboundEmailContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    from_email_address: NotRequired[
        "capo_connect.types.email_address_info.EmailAddressInfo"
    ]
    """<p>The email address associated with the Connect Customer instance.</p>"""
    destination_email_address: "capo_connect.types.email_address_info.EmailAddressInfo"
    """<p>The email address of the customer.</p>"""
    additional_recipients: NotRequired[
        "capo_connect.types.outbound_additional_recipients.OutboundAdditionalRecipients"
    ]
    """<p>The additional recipients address of email in CC.</p>"""
    email_message: "capo_connect.types.outbound_email_content.OutboundEmailContent"
    """<p>The email message body to be sent to the newly created email.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutboundEmailContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    if "from_email_address" in value:
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartOutboundEmailContactRequest:
    out: StartOutboundEmailContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "StartOutboundEmailContactRequest.instance_id required"
        )
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError(
            "StartOutboundEmailContactRequest.contact_id required"
        )
    if data.get("FromEmailAddress") is not None:
        import capo_connect.types.email_address_info

        out["from_email_address"] = (
            capo_connect.types.email_address_info.deserialize_json(
                data["FromEmailAddress"]
            )
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
            "StartOutboundEmailContactRequest.destination_email_address required"
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
        raise DeserializationError(
            "StartOutboundEmailContactRequest.email_message required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
