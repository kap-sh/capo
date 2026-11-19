"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpScopeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_scope_value

GcpScopeValueList: TypeAlias = list[
    "capo_inspector2.types.gcp_scope_value.GcpScopeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: GcpScopeValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> GcpScopeValueList:
    return [item for item in data if item is not None]
