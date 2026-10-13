"""Generated from Smithy shape ``com.amazonaws.connect#InboundAdditionalRecipients``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.email_address_recipient_list


class InboundAdditionalRecipients(TypedDict, closed=True):
    to_addresses: NotRequired[
        "capo_connect.types.email_address_recipient_list.EmailAddressRecipientList"
    ]
    """<p>The <b>additional</b> recipients information present in to list. You must have 1 required recipient (<code>DestinationEmailAddress</code>). You can then specify up to 49 additional recipients (across <code>ToAddresses</code> and <code>CcAddresses</code>), for a total of 50 recipients.</p>"""
    cc_addresses: NotRequired[
        "capo_connect.types.email_address_recipient_list.EmailAddressRecipientList"
    ]
    """<p>The <b>additional</b> recipients information present in cc list. You must have 1 required recipient (<code>DestinationEmailAddress</code>). You can then specify up to 49 additional recipients (across <code>ToAddresses</code> and <code>CcAddresses</code>), for a total of 50 recipients.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundAdditionalRecipients) -> dict:
    out: dict = {}
    if "to_addresses" in value:
        import capo_connect.types.email_address_recipient_list

        out["ToAddresses"] = (
            capo_connect.types.email_address_recipient_list.serialize_json(
                value["to_addresses"]
            )
        )
    if "cc_addresses" in value:
        import capo_connect.types.email_address_recipient_list

        out["CcAddresses"] = (
            capo_connect.types.email_address_recipient_list.serialize_json(
                value["cc_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> InboundAdditionalRecipients:
    out: InboundAdditionalRecipients = {}  # type: ignore[typeddict-item]
    if data.get("ToAddresses") is not None:
        import capo_connect.types.email_address_recipient_list

        out["to_addresses"] = (
            capo_connect.types.email_address_recipient_list.deserialize_json(
                data["ToAddresses"]
            )
        )
    if data.get("CcAddresses") is not None:
        import capo_connect.types.email_address_recipient_list

        out["cc_addresses"] = (
            capo_connect.types.email_address_recipient_list.deserialize_json(
                data["CcAddresses"]
            )
        )
    return out


def redact_sensitive(value: InboundAdditionalRecipients) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "to_addresses" in value:
        import capo_connect.types.email_address_recipient_list

        out["to_addresses"] = (
            capo_connect.types.email_address_recipient_list.redact_sensitive(
                value["to_addresses"]
            )
        )
    if "cc_addresses" in value:
        import capo_connect.types.email_address_recipient_list

        out["cc_addresses"] = (
            capo_connect.types.email_address_recipient_list.redact_sensitive(
                value["cc_addresses"]
            )
        )
    return out
