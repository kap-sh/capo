"""Generated from Smithy shape ``com.amazonaws.datasync#SourceNetworkInterfaceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.network_interface_arn

SourceNetworkInterfaceArns: TypeAlias = list[
    "capo_datasync.types.network_interface_arn.NetworkInterfaceArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceNetworkInterfaceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SourceNetworkInterfaceArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceNetworkInterfaceArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> SourceNetworkInterfaceArns:
    return [item for item in data if item is not None]
