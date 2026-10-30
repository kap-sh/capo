"""Generated from Smithy shape ``com.amazonaws.continuum#FlowVerdictValue``."""

from typing import Literal, TypeAlias, cast

"""Outcome recorded for one attack flow."""
FlowVerdictValue: TypeAlias = Literal[
    "CONFIRMED",
    "DENIED",
    "INCONCLUSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowVerdictValue) -> str:
    return value


def deserialize_json(data: str) -> FlowVerdictValue:
    return cast(FlowVerdictValue, data)
