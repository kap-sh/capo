"""Generated from Smithy shape ``com.amazonaws.sesv2#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address_list


class Destination(TypedDict, closed=True):
    to_addresses: NotRequired["capo_sesv2.types.email_address_list.EmailAddressList"]
    """<p>An array that contains the email addresses of the "To" recipients for the email.</p>"""
    cc_addresses: NotRequired["capo_sesv2.types.email_address_list.EmailAddressList"]
    """<p>An array that contains the email addresses of the "CC" (carbon copy) recipients for the email.</p>"""
    bcc_addresses: NotRequired["capo_sesv2.types.email_address_list.EmailAddressList"]
    """<p>An array that contains the email addresses of the "BCC" (blind carbon copy) recipients for the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "to_addresses" in value:
        import capo_sesv2.types.email_address_list

        out["ToAddresses"] = capo_sesv2.types.email_address_list.serialize_json(
            value["to_addresses"]
        )
    if "cc_addresses" in value:
        import capo_sesv2.types.email_address_list

        out["CcAddresses"] = capo_sesv2.types.email_address_list.serialize_json(
            value["cc_addresses"]
        )
    if "bcc_addresses" in value:
        import capo_sesv2.types.email_address_list

        out["BccAddresses"] = capo_sesv2.types.email_address_list.serialize_json(
            value["bcc_addresses"]
        )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if data.get("ToAddresses") is not None:
        import capo_sesv2.types.email_address_list

        out["to_addresses"] = capo_sesv2.types.email_address_list.deserialize_json(
            data["ToAddresses"]
        )
    if data.get("CcAddresses") is not None:
        import capo_sesv2.types.email_address_list

        out["cc_addresses"] = capo_sesv2.types.email_address_list.deserialize_json(
            data["CcAddresses"]
        )
    if data.get("BccAddresses") is not None:
        import capo_sesv2.types.email_address_list

        out["bcc_addresses"] = capo_sesv2.types.email_address_list.deserialize_json(
            data["BccAddresses"]
        )
    return out
