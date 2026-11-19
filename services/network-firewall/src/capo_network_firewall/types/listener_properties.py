"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListenerProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.listener_property

ListenerProperties: TypeAlias = list[
    "capo_network_firewall.types.listener_property.ListenerProperty"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListenerProperties) -> list:
    import capo_network_firewall.types.listener_property

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.listener_property.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ListenerProperties:
    import capo_network_firewall.types.listener_property

    out: ListenerProperties = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.listener_property.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListenerProperties) -> list:
    import capo_network_firewall.types.listener_property

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.listener_property.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ListenerProperties:
    import capo_network_firewall.types.listener_property

    out: ListenerProperties = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.listener_property.deserialize_cbor(item))
    return out
