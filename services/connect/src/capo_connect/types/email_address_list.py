"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.email_address_metadata

EmailAddressList: TypeAlias = list[
    "capo_connect.types.email_address_metadata.EmailAddressMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressList) -> list:
    import capo_connect.types.email_address_metadata

    out: list = []
    for item in value:
        out.append(capo_connect.types.email_address_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAddressList:
    import capo_connect.types.email_address_metadata

    out: EmailAddressList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.email_address_metadata.deserialize_json(item))
    return out


def redact_sensitive(value: EmailAddressList) -> list[Any]:
    import capo_connect.types.email_address_metadata

    return [
        capo_connect.types.email_address_metadata.redact_sensitive(item)
        for item in value
    ]
