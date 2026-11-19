"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsProvider``."""

from typing import Literal, TypeAlias, cast

StandardsProvider: TypeAlias = Literal[
    "AWS",
    "Azure",
    "GCP",
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsProvider) -> str:
    return value


def deserialize_json(data: str) -> StandardsProvider:
    return cast(StandardsProvider, data)
