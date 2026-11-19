"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SyncStateConfig``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.per_object_status
    import capo_network_firewall.types.resource_name

SyncStateConfig: TypeAlias = dict[
    "capo_network_firewall.types.resource_name.ResourceName",
    "capo_network_firewall.types.per_object_status.PerObjectStatus",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: SyncStateConfig) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.per_object_status

        out[key] = capo_network_firewall.types.per_object_status.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncStateConfig:
    out: SyncStateConfig = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.per_object_status

        out[key] = (
            capo_network_firewall.types.per_object_status.deserialize_aws_json_1_0(
                value
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: SyncStateConfig) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_firewall.types.per_object_status

        out[key] = capo_network_firewall.types.per_object_status.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> SyncStateConfig:
    out: SyncStateConfig = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_network_firewall.types.per_object_status

        out[key] = capo_network_firewall.types.per_object_status.deserialize_cbor(value)
    return out
