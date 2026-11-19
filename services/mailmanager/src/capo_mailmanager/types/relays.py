"""Generated from Smithy shape ``com.amazonaws.mailmanager#Relays``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.relay

Relays: TypeAlias = list["capo_mailmanager.types.relay.Relay"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Relays) -> list:
    import capo_mailmanager.types.relay

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.relay.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Relays:
    import capo_mailmanager.types.relay

    out: Relays = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.relay.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Relays) -> list:
    import capo_mailmanager.types.relay

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.relay.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Relays:
    import capo_mailmanager.types.relay

    out: Relays = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.relay.deserialize_cbor(item))
    return out
