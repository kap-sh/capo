"""Generated from Smithy shape ``com.amazonaws.connect#NullableAdditionalRecipients``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.optional_email_address_recipient_list


class NullableAdditionalRecipients(TypedDict, closed=True):
    cc_email_addresses: NotRequired[
        "capo_connect.types.optional_email_address_recipient_list.OptionalEmailAddressRecipientList"
    ]
    """<p>The additional CC email address recipients. You can specify up to 50 addresses. Provide an empty list to clear the existing CC recipients.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NullableAdditionalRecipients) -> dict:
    out: dict = {}
    if "cc_email_addresses" in value:
        import capo_connect.types.optional_email_address_recipient_list

        out["CcEmailAddresses"] = (
            capo_connect.types.optional_email_address_recipient_list.serialize_json(
                value["cc_email_addresses"]
            )
        )
    return out


def deserialize_json(data: dict) -> NullableAdditionalRecipients:
    out: NullableAdditionalRecipients = {}  # type: ignore[typeddict-item]
    if data.get("CcEmailAddresses") is not None:
        import capo_connect.types.optional_email_address_recipient_list

        out["cc_email_addresses"] = (
            capo_connect.types.optional_email_address_recipient_list.deserialize_json(
                data["CcEmailAddresses"]
            )
        )
    return out


def redact_sensitive(value: NullableAdditionalRecipients) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cc_email_addresses" in value:
        import capo_connect.types.optional_email_address_recipient_list

        out["cc_email_addresses"] = (
            capo_connect.types.optional_email_address_recipient_list.redact_sensitive(
                value["cc_email_addresses"]
            )
        )
    return out
