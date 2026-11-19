"""Generated from Smithy shape ``com.amazonaws.elementalinference#PassthroughFunctionTarget``."""

from typing_extensions import TypedDict


class PassthroughFunctionTarget(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PassthroughFunctionTarget) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PassthroughFunctionTarget:
    out: PassthroughFunctionTarget = {}  # type: ignore[typeddict-item]
    return out
