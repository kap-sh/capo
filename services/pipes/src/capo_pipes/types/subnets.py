"""Generated from Smithy shape ``com.amazonaws.pipes#Subnets``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.subnet

Subnets: TypeAlias = list["capo_pipes.types.subnet.Subnet"]


# --- restJson1 ser/de ---
def serialize_json(value: Subnets) -> list:
    return list(value)


def deserialize_json(data: list) -> Subnets:
    return [item for item in data if item is not None]


def redact_sensitive(value: Subnets) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
