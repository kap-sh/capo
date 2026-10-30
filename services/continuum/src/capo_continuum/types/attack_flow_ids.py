"""Generated from Smithy shape ``com.amazonaws.continuum#AttackFlowIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.attack_flow_id

AttackFlowIds: TypeAlias = list["capo_continuum.types.attack_flow_id.AttackFlowId"]


# --- restJson1 ser/de ---
def serialize_json(value: AttackFlowIds) -> list:
    return list(value)


def deserialize_json(data: list) -> AttackFlowIds:
    return [item for item in data if item is not None]
