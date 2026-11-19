"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#UpdateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.update_ip_address_entry

UpdateIpAddressList: TypeAlias = list[
    "capo_route53globalresolver.types.update_ip_address_entry.UpdateIpAddressEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpAddressList) -> list:
    import capo_route53globalresolver.types.update_ip_address_entry

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.update_ip_address_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateIpAddressList:
    import capo_route53globalresolver.types.update_ip_address_entry

    out: UpdateIpAddressList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route53globalresolver.types.update_ip_address_entry.deserialize_json(
                item
            )
        )
    return out
