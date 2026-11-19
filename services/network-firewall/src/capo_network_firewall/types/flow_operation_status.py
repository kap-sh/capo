"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowOperationStatus``."""

from typing import Literal, TypeAlias, cast

FlowOperationStatus: TypeAlias = Literal[
    "COMPLETED",
    "IN_PROGRESS",
    "FAILED",
    "COMPLETED_WITH_ERRORS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowOperationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FlowOperationStatus:
    return cast(FlowOperationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlowOperationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> FlowOperationStatus:
    return cast(FlowOperationStatus, data)
