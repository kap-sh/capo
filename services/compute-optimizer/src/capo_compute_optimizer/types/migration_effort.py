"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#MigrationEffort``."""

from typing import Literal, TypeAlias, cast

MigrationEffort: TypeAlias = Literal[
    "VeryLow",
    "Low",
    "Medium",
    "High",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MigrationEffort) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MigrationEffort:
    return cast(MigrationEffort, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MigrationEffort) -> str:
    return value


def deserialize_cbor(data: str) -> MigrationEffort:
    return cast(MigrationEffort, data)
