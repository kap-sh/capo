"""Generated from Smithy shape ``com.amazonaws.auditmanager#Controls``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control

Controls: TypeAlias = list["capo_auditmanager.types.control.Control"]


# --- restJson1 ser/de ---
def serialize_json(value: Controls) -> list:
    import capo_auditmanager.types.control

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control.serialize_json(item))
    return out


def deserialize_json(data: list) -> Controls:
    import capo_auditmanager.types.control

    out: Controls = []
    for item in data:
        if item is None:
            continue
        out.append(capo_auditmanager.types.control.deserialize_json(item))
    return out


def redact_sensitive(value: Controls) -> list[Any]:
    import capo_auditmanager.types.control

    return [capo_auditmanager.types.control.redact_sensitive(item) for item in value]
