"""Generated from Smithy shape ``com.amazonaws.opensearch#DiffFieldPolicy``."""

from typing import Literal, TypeAlias, cast

DiffFieldPolicy: TypeAlias = Literal["redacted",]


# --- restJson1 ser/de ---
def serialize_json(value: DiffFieldPolicy) -> str:
    return value


def deserialize_json(data: str) -> DiffFieldPolicy:
    return cast(DiffFieldPolicy, data)
