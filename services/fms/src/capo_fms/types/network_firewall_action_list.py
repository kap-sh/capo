"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.network_firewall_action

NetworkFirewallActionList: TypeAlias = list[
    "capo_fms.types.network_firewall_action.NetworkFirewallAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallActionList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NetworkFirewallActionList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallActionList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> NetworkFirewallActionList:
    return [item for item in data if item is not None]
