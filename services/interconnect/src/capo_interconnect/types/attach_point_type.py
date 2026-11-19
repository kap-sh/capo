"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPointType``."""

from typing import Literal, TypeAlias, cast

AttachPointType: TypeAlias = Literal["DirectConnectGateway",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachPointType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AttachPointType:
    return cast(AttachPointType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttachPointType) -> str:
    return value


def deserialize_cbor(data: str) -> AttachPointType:
    return cast(AttachPointType, data)
