"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ExecutionEventType``."""

from typing import Literal, TypeAlias, cast

ExecutionEventType: TypeAlias = Literal[
    "unknown",
    "executionPending",
    "executionStarted",
    "executionSucceeded",
    "executionFailed",
    "executionPausing",
    "executionPaused",
    "executionCanceling",
    "executionCanceled",
    "executionPendingApproval",
    "executionBehaviorChangedToUngraceful",
    "executionBehaviorChangedToGraceful",
    "executionPendingChildPlanManualApproval",
    "executionSuccessMonitoringApplicationHealth",
    "stepStarted",
    "stepUpdate",
    "stepSucceeded",
    "stepFailed",
    "stepSkipped",
    "stepPausedByError",
    "stepPausedByOperator",
    "stepCanceled",
    "stepPendingApproval",
    "stepExecutionBehaviorChangedToUngraceful",
    "stepPendingApplicationHealthMonitor",
    "planEvaluationWarning",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionEventType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionEventType:
    return cast(ExecutionEventType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExecutionEventType) -> str:
    return value


def deserialize_cbor(data: str) -> ExecutionEventType:
    return cast(ExecutionEventType, data)
