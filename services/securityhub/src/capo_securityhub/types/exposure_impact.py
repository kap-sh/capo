"""Generated from Smithy shape ``com.amazonaws.securityhub#ExposureImpact``."""

from typing import Literal, TypeAlias, cast

ExposureImpact: TypeAlias = Literal[
    "Reduces",
    "Resolves",
    "Unchanged",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExposureImpact) -> str:
    return value


def deserialize_json(data: str) -> ExposureImpact:
    return cast(ExposureImpact, data)
