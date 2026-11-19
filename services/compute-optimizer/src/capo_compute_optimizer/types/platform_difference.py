"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#PlatformDifference``."""

from typing import Literal, TypeAlias, cast

PlatformDifference: TypeAlias = Literal[
    "Hypervisor",
    "NetworkInterface",
    "StorageInterface",
    "InstanceStoreAvailability",
    "VirtualizationType",
    "Architecture",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PlatformDifference) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PlatformDifference:
    return cast(PlatformDifference, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlatformDifference) -> str:
    return value


def deserialize_cbor(data: str) -> PlatformDifference:
    return cast(PlatformDifference, data)
