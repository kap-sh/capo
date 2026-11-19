"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "ERROR",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
