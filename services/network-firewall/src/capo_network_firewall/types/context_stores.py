"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ContextStores``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.context_store

ContextStores: TypeAlias = list[
    "capo_network_firewall.types.context_store.ContextStore"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContextStores) -> list:
    import capo_network_firewall.types.context_store

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.context_store.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ContextStores:
    import capo_network_firewall.types.context_store

    out: ContextStores = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.context_store.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContextStores) -> list:
    import capo_network_firewall.types.context_store

    out: list = []
    for item in value:
        out.append(capo_network_firewall.types.context_store.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ContextStores:
    import capo_network_firewall.types.context_store

    out: ContextStores = []
    for item in data:
        if item is None:
            continue
        out.append(capo_network_firewall.types.context_store.deserialize_cbor(item))
    return out
