"""Generated from Smithy shape ``com.amazonaws.securityagent#TriggerFilterMatchMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether a filter's value must match its patterns.</p>"""
TriggerFilterMatchMode: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TriggerFilterMatchMode) -> str:
    return value


def deserialize_json(data: str) -> TriggerFilterMatchMode:
    return cast(TriggerFilterMatchMode, data)
