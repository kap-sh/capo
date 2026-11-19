"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadTypesPreference``."""

from typing import Literal, TypeAlias, cast

InferredWorkloadTypesPreference: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferredWorkloadTypesPreference) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferredWorkloadTypesPreference:
    return cast(InferredWorkloadTypesPreference, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InferredWorkloadTypesPreference) -> str:
    return value


def deserialize_cbor(data: str) -> InferredWorkloadTypesPreference:
    return cast(InferredWorkloadTypesPreference, data)
