"""Generated from Smithy shape ``com.amazonaws.elementalinference#ExtendedAnalysisMode``."""

from typing import Literal, TypeAlias, cast

ExtendedAnalysisMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExtendedAnalysisMode) -> str:
    return value


def deserialize_json(data: str) -> ExtendedAnalysisMode:
    return cast(ExtendedAnalysisMode, data)
