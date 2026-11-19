"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomImageProtocol``."""

from typing import Literal, TypeAlias, cast

CustomImageProtocol: TypeAlias = Literal[
    "PCOIP",
    "DCV",
    "BYOP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomImageProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomImageProtocol:
    return cast(CustomImageProtocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomImageProtocol) -> str:
    return value


def deserialize_cbor(data: str) -> CustomImageProtocol:
    return cast(CustomImageProtocol, data)
