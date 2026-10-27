"""Generated from Smithy shape ``com.amazonaws.connect#UpdateOutboundEmailContactMessageRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.update_outbound_email_content


class UpdateOutboundEmailContactMessageRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    email_message: (
        "capo_connect.types.update_outbound_email_content.UpdateOutboundEmailContent"
    )
    """<p>The email message body to update on the outbound email draft.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutboundEmailContactMessageRequest) -> dict:
    out: dict = {}
    import capo_connect.types.update_outbound_email_content

    out["EmailMessage"] = (
        capo_connect.types.update_outbound_email_content.serialize_json(
            value["email_message"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateOutboundEmailContactMessageRequest:
    out: UpdateOutboundEmailContactMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailMessage") is not None:
        import capo_connect.types.update_outbound_email_content

        out["email_message"] = (
            capo_connect.types.update_outbound_email_content.deserialize_json(
                data["EmailMessage"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateOutboundEmailContactMessageRequest.email_message required"
        )
    return out


def redact_sensitive(value: UpdateOutboundEmailContactMessageRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_message" in value:
        import capo_connect.types.update_outbound_email_content

        out["email_message"] = (
            capo_connect.types.update_outbound_email_content.redact_sensitive(
                value["email_message"]
            )
        )
    return out
