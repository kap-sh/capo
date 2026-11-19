"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionState``."""

from typing import Literal, TypeAlias, cast

ExecutionState: TypeAlias = Literal[
    "inProgress",
    "pausedByFailedStep",
    "pausedByOperator",
    "completed",
    "completedWithExceptions",
    "canceled",
    "planExecutionTimedOut",
    "pendingManualApproval",
    "failed",
    "pending",
    "completedMonitoringApplicationHealth",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionState:
    return cast(ExecutionState, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionState) -> str:
    return value


def deserialize_cbor(data: str) -> ExecutionState:
    return cast(ExecutionState, data)
