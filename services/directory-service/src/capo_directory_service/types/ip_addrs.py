"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpAddrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.ip_addr

IpAddrs: TypeAlias = list["capo_directory_service.types.ip_addr.IpAddr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddrs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpAddrs:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpAddrs) -> list:
    return list(value)


def deserialize_cbor(data: list) -> IpAddrs:
    return [item for item in data if item is not None]
