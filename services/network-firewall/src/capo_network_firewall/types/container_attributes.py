"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContainerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.container_attribute

ContainerAttributes: TypeAlias = list[
    "capo_network_firewall.types.container_attribute.ContainerAttribute"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerAttributes) -> list:
    import capo_network_firewall.types.container_attribute

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.container_attribute.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContainerAttributes:
    import capo_network_firewall.types.container_attribute

    out: ContainerAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.container_attribute.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerAttributes) -> list:
    import capo_network_firewall.types.container_attribute

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.container_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ContainerAttributes:
    import capo_network_firewall.types.container_attribute

    out: ContainerAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.container_attribute.deserialize_cbor(item)
        )
    return out
