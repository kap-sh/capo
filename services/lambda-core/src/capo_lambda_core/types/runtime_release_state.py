"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeReleaseState``."""

from typing import Literal, TypeAlias, cast

"""The release state declared by a runtime publisher for a runtime or runtime alias."""
RuntimeReleaseState: TypeAlias = Literal[
    "PREVIEW",
    "GA",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeReleaseState) -> str:
    return value


def deserialize_json(data: str) -> RuntimeReleaseState:
    return cast(RuntimeReleaseState, data)
