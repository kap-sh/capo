"""Generated from Smithy shape ``com.amazonaws.datasync#PhaseStatus``."""

from typing import Literal, TypeAlias, cast

PhaseStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhaseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PhaseStatus:
    return cast(PhaseStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PhaseStatus) -> str:
    return value


def deserialize_cbor(data: str) -> PhaseStatus:
    return cast(PhaseStatus, data)
