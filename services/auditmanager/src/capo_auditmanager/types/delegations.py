"""Generated from Smithy shape ``com.amazonaws.auditmanager#Delegations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.delegation

Delegations: TypeAlias = list["capo_auditmanager.types.delegation.Delegation"]


# --- restJson1 ser/de ---
def serialize_json(value: Delegations) -> list:
    import capo_auditmanager.types.delegation

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.delegation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Delegations:
    import capo_auditmanager.types.delegation

    out: Delegations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_auditmanager.types.delegation.deserialize_json(item))
    return out


def redact_sensitive(value: Delegations) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
