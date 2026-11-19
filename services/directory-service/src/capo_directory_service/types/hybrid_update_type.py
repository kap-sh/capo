"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateType``."""

from typing import Literal, TypeAlias, cast

HybridUpdateType: TypeAlias = Literal[
    "SelfManagedInstances",
    "HybridAdministratorAccount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HybridUpdateType:
    return cast(HybridUpdateType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HybridUpdateType) -> str:
    return value


def deserialize_cbor(data: str) -> HybridUpdateType:
    return cast(HybridUpdateType, data)
