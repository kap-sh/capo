"""Generated from Smithy shape ``com.amazonaws.connect#OutboundAdditionalRecipients``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_address_recipient_list


class OutboundAdditionalRecipients(TypedDict, closed=True):
    cc_email_addresses: NotRequired[
        "capo_connect.types.email_address_recipient_list.EmailAddressRecipientList"
    ]
    """<p>Information about the <b>additional</b> CC email address recipients. Email recipients are limited to 50 total addresses: 1 required recipient in the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_SendOutboundEmail.html#API_SendOutboundEmail_RequestBody">DestinationEmailAddress</a> field and up to 49 recipients in the 'CcEmailAddresses' field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutboundAdditionalRecipients) -> dict:
    out: dict = {}
    if "cc_email_addresses" in value:
        import capo_connect.types.email_address_recipient_list

        out["CcEmailAddresses"] = (
            capo_connect.types.email_address_recipient_list.serialize_json(
                value["cc_email_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutboundAdditionalRecipients:
    out: OutboundAdditionalRecipients = {}  # type: ignore[typeddict-item]
    if data.get("CcEmailAddresses") is not None:
        import capo_connect.types.email_address_recipient_list

        out["cc_email_addresses"] = (
            capo_connect.types.email_address_recipient_list.deserialize_json(
                data["CcEmailAddresses"]
            )
        )
    return out
