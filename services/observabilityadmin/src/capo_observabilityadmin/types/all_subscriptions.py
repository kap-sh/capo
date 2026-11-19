"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AllSubscriptions``."""

from typing_extensions import TypedDict


class AllSubscriptions(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: AllSubscriptions) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AllSubscriptions:
    out: AllSubscriptions = {}  # type: ignore[typeddict-item]
    return out
