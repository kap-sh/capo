"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationStatus``."""

from typing import Literal, TypeAlias, cast

OperationStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "ERROR",
    "SUCCESSFUL",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationStatus:
    return cast(OperationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OperationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> OperationStatus:
    return cast(OperationStatus, data)
