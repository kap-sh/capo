"""Generated from Smithy shape ``com.amazonaws.directoryservice#RadiusAuthenticationProtocol``."""

from typing import Literal, TypeAlias, cast

RadiusAuthenticationProtocol: TypeAlias = Literal[
    "PAP",
    "CHAP",
    "MS-CHAPv1",
    "MS-CHAPv2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RadiusAuthenticationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RadiusAuthenticationProtocol:
    return cast(RadiusAuthenticationProtocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RadiusAuthenticationProtocol) -> str:
    return value


def deserialize_cbor(data: str) -> RadiusAuthenticationProtocol:
    return cast(RadiusAuthenticationProtocol, data)
