"""Generated from Smithy shape ``com.amazonaws.lambdacore#CompatibilityPolicy``."""

from typing import Literal, TypeAlias, cast

"""Indicates whether a runtime version supports a feature."""
CompatibilityPolicy: TypeAlias = Literal[
    "Supported",
    "NotSupported",
]


# --- restJson1 ser/de ---
def serialize_json(value: CompatibilityPolicy) -> str:
    return value


def deserialize_json(data: str) -> CompatibilityPolicy:
    return cast(CompatibilityPolicy, data)
