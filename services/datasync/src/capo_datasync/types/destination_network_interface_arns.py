"""Generated from Smithy shape ``com.amazonaws.datasync#DestinationNetworkInterfaceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.network_interface_arn

DestinationNetworkInterfaceArns: TypeAlias = list[
    "capo_datasync.types.network_interface_arn.NetworkInterfaceArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationNetworkInterfaceArns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DestinationNetworkInterfaceArns:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DestinationNetworkInterfaceArns) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DestinationNetworkInterfaceArns:
    return [item for item in data if item is not None]
