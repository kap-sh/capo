"""Generated from Smithy shape ``com.amazonaws.lambdacore#ThrottleReason``."""

from typing import Literal, TypeAlias, cast

ThrottleReason: TypeAlias = Literal[
    "ConcurrentInvocationLimitExceeded",
    "FunctionInvocationRateLimitExceeded",
    "ReservedFunctionConcurrentInvocationLimitExceeded",
    "ReservedFunctionInvocationRateLimitExceeded",
    "CallerRateLimitExceeded",
    "ConcurrentSnapshotCreateLimitExceeded",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottleReason) -> str:
    return value


def deserialize_json(data: str) -> ThrottleReason:
    return cast(ThrottleReason, data)
