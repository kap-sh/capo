"""Generated from Smithy shape ``com.amazonaws.lambda#EventType``."""

from typing import Literal, TypeAlias, cast

EventType: TypeAlias = Literal[
    "ExecutionStarted",
    "ExecutionSucceeded",
    "ExecutionFailed",
    "ExecutionTimedOut",
    "ExecutionStopped",
    "ContextStarted",
    "ContextSucceeded",
    "ContextFailed",
    "WaitStarted",
    "WaitSucceeded",
    "WaitCancelled",
    "StepStarted",
    "StepSucceeded",
    "StepFailed",
    "ChainedInvokeStarted",
    "ChainedInvokeSucceeded",
    "ChainedInvokeFailed",
    "ChainedInvokeTimedOut",
    "ChainedInvokeStopped",
    "CallbackStarted",
    "CallbackSucceeded",
    "CallbackFailed",
    "CallbackTimedOut",
    "InvocationCompleted",
    "ExecutionPaused",
    "ExecutionResumed",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventType) -> str:
    return value


def deserialize_json(data: str) -> EventType:
    return cast(EventType, data)
