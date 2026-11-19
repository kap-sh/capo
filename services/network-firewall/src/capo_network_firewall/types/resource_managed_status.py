"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceManagedStatus``."""

from typing import Literal, TypeAlias, cast

ResourceManagedStatus: TypeAlias = Literal[
    "MANAGED",
    "ACCOUNT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceManagedStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceManagedStatus:
    return cast(ResourceManagedStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceManagedStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceManagedStatus:
    return cast(ResourceManagedStatus, data)
