"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeArchitecture``."""

from typing import Literal, TypeAlias, cast

"""Supported CPU architecture for a runtime."""
RuntimeArchitecture: TypeAlias = Literal[
    "x86_64",
    "arm64",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeArchitecture) -> str:
    return value


def deserialize_json(data: str) -> RuntimeArchitecture:
    return cast(RuntimeArchitecture, data)
