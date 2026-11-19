"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlsProvider``."""

from typing import Literal, TypeAlias, cast

SecurityControlsProvider: TypeAlias = Literal[
    "AWS",
    "Azure",
    "GCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlsProvider) -> str:
    return value


def deserialize_json(data: str) -> SecurityControlsProvider:
    return cast(SecurityControlsProvider, data)
