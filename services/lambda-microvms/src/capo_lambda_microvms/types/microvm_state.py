"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmState``."""

from typing import Literal, TypeAlias, cast

"""The lifecycle state of a MicroVm."""
MicrovmState: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "SUSPENDING",
    "SUSPENDED",
    "TERMINATING",
    "TERMINATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmState) -> str:
    return value


def deserialize_json(data: str) -> MicrovmState:
    return cast(MicrovmState, data)
