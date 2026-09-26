"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ScopeList``."""

from typing import TypeAlias

ScopeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ScopeList:
    return [item for item in data if item is not None]
