"""Generated from Smithy shape ``com.amazonaws.directoryservice#RadiusStatus``."""

from typing import Literal, TypeAlias, cast

RadiusStatus: TypeAlias = Literal[
    "Creating",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RadiusStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RadiusStatus:
    return cast(RadiusStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RadiusStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RadiusStatus:
    return cast(RadiusStatus, data)
