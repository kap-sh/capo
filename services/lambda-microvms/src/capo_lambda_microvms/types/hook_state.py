"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#HookState``."""

from typing import Literal, TypeAlias, cast

"""Whether invocation hooks are enabled or disabled on a MicroVm."""
HookState: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HookState) -> str:
    return value


def deserialize_json(data: str) -> HookState:
    return cast(HookState, data)
