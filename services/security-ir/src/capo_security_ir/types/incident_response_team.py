"""Generated from Smithy shape ``com.amazonaws.securityir#IncidentResponseTeam``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.incident_responder

IncidentResponseTeam: TypeAlias = list[
    "capo_security_ir.types.incident_responder.IncidentResponder"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncidentResponseTeam) -> list:
    import capo_security_ir.types.incident_responder

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.incident_responder.serialize_json(item))
    return out


def deserialize_json(data: list) -> IncidentResponseTeam:
    import capo_security_ir.types.incident_responder

    out: IncidentResponseTeam = []
    for item in data:
        if item is None:
            continue
        out.append(capo_security_ir.types.incident_responder.deserialize_json(item))
    return out


def redact_sensitive(value: IncidentResponseTeam) -> list[Any]:
    import capo_security_ir.types.incident_responder

    return [
        capo_security_ir.types.incident_responder.redact_sensitive(item)
        for item in value
    ]
