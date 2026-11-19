"""Generated from Smithy shape ``com.amazonaws.mailmanager#IpType``."""

from typing import Literal, TypeAlias, cast

IpType: TypeAlias = Literal[
    "IPV4",
    "DUAL_STACK",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IpType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IpType:
    return cast(IpType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpType) -> str:
    return value


def deserialize_cbor(data: str) -> IpType:
    return cast(IpType, data)
