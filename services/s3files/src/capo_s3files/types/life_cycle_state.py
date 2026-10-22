"""Generated from Smithy shape ``com.amazonaws.s3files#LifeCycleState``."""

from typing import Literal, TypeAlias, cast

LifeCycleState: TypeAlias = Literal[
    "available",
    "creating",
    "deleting",
    "deleted",
    "error",
    "updating",
    "misconfigured",
]


# --- restJson1 ser/de ---
def serialize_json(value: LifeCycleState) -> str:
    return value


def deserialize_json(data: str) -> LifeCycleState:
    return cast(LifeCycleState, data)
