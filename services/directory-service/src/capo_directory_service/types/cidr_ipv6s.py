"""Generated from Smithy shape ``com.amazonaws.directoryservice#CidrIpv6s``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.cidr_ipv6

CidrIpv6s: TypeAlias = list["capo_directory_service.types.cidr_ipv6.CidrIpv6"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CidrIpv6s) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CidrIpv6s:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CidrIpv6s) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CidrIpv6s:
    return [item for item in data if item is not None]
