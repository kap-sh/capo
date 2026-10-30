"""Generated from Smithy shape ``com.amazonaws.continuum#ValidationTerminalStatus``."""

from typing import Literal, TypeAlias, cast

"""How a validation run ended. Producer statuses map onto these; an unmapped status omits `terminalStatus` while the rest of the body still projects."""
ValidationTerminalStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "NO_SOURCE_AVAILABLE",
    "PARTIAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationTerminalStatus) -> str:
    return value


def deserialize_json(data: str) -> ValidationTerminalStatus:
    return cast(ValidationTerminalStatus, data)
