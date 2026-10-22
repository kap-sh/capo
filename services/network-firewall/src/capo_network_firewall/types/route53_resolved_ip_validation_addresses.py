"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Route53ResolvedIPValidationAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.address

Route53ResolvedIPValidationAddresses: TypeAlias = list[
    "capo_network_firewall.types.address.Address"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53ResolvedIPValidationAddresses) -> list:
    import capo_network_firewall.types.address

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.address.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Route53ResolvedIPValidationAddresses:
    import capo_network_firewall.types.address

    out: Route53ResolvedIPValidationAddresses = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.address.deserialize_aws_json_1_0(item))
    return out
