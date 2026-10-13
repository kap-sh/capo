"""Generated from Smithy shape ``com.amazonaws.guardduty#PrivateIpAddresses``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.private_ip_address_details

PrivateIpAddresses: TypeAlias = list[
    "capo_guardduty.types.private_ip_address_details.PrivateIpAddressDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateIpAddresses) -> list:
    import capo_guardduty.types.private_ip_address_details

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.private_ip_address_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> PrivateIpAddresses:
    import capo_guardduty.types.private_ip_address_details

    out: PrivateIpAddresses = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_guardduty.types.private_ip_address_details.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PrivateIpAddresses) -> list[Any]:
    import capo_guardduty.types.private_ip_address_details

    return [
        capo_guardduty.types.private_ip_address_details.redact_sensitive(item)
        for item in value
    ]
