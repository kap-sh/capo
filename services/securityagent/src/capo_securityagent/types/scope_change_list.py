"""Generated from Smithy shape ``com.amazonaws.securityagent#ScopeChangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityagent.types.scope_change

ScopeChangeList: TypeAlias = list["capo_securityagent.types.scope_change.ScopeChange"]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeChangeList) -> list:
    import capo_securityagent.types.scope_change

    out: list = []
    for item in value:
        out.append(capo_securityagent.types.scope_change.serialize_json(item))
    return out


def deserialize_json(data: list) -> ScopeChangeList:
    import capo_securityagent.types.scope_change

    out: ScopeChangeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_securityagent.types.scope_change.deserialize_json(item))
    return out
