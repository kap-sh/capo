"""Generated from Smithy shape ``com.amazonaws.pricingplanmanager#ResourceArns``."""

from typing import TypeAlias

ResourceArns: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArns) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArns:
    return [item for item in data if item is not None]
