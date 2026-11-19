"""Generated from Smithy shape ``com.amazonaws.codedeploy#OutdatedInstancesStrategy``."""

from typing import Literal, TypeAlias, cast

OutdatedInstancesStrategy: TypeAlias = Literal[
    "UPDATE",
    "IGNORE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutdatedInstancesStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutdatedInstancesStrategy:
    return cast(OutdatedInstancesStrategy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OutdatedInstancesStrategy) -> str:
    return value


def deserialize_cbor(data: str) -> OutdatedInstancesStrategy:
    return cast(OutdatedInstancesStrategy, data)
