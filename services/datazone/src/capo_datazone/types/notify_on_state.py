"""Generated from Smithy shape ``com.amazonaws.datazone#NotifyOnState``."""

from typing import Literal, TypeAlias, cast

"""<p>A notebook run state that triggers a notification in Amazon SageMaker Unified Studio.</p>"""
NotifyOnState: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "STOPPED",
    "QUEUED",
    "STARTING",
    "RUNNING",
    "STOPPING",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotifyOnState) -> str:
    return value


def deserialize_json(data: str) -> NotifyOnState:
    return cast(NotifyOnState, data)
