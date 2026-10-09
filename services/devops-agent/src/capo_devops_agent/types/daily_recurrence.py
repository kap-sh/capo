"""Generated from Smithy shape ``com.amazonaws.devopsagent#DailyRecurrence``."""

from typing_extensions import TypedDict


class DailyRecurrence(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DailyRecurrence) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DailyRecurrence:
    out: DailyRecurrence = {}  # type: ignore[typeddict-item]
    return out
