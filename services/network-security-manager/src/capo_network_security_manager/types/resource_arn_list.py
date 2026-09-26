"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.arn

ResourceArnList: TypeAlias = list["capo_network_security_manager.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnList:
    return [item for item in data if item is not None]
