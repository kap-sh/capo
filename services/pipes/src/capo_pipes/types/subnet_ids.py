"""Generated from Smithy shape ``com.amazonaws.pipes#SubnetIds``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.subnet_id

SubnetIds: TypeAlias = list["capo_pipes.types.subnet_id.SubnetId"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return [item for item in data if item is not None]


def redact_sensitive(value: SubnetIds) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
