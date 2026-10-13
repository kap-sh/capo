"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.audit_event

AuditEventsList: TypeAlias = list[
    "capo_connectcases.types.audit_event.AuditEvent | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventsList) -> list:
    import capo_connectcases.types.audit_event

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(capo_connectcases.types.audit_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditEventsList:
    import capo_connectcases.types.audit_event

    out: AuditEventsList = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(capo_connectcases.types.audit_event.deserialize_json(item))
    return out


def redact_sensitive(value: AuditEventsList) -> list[Any]:
    import capo_connectcases.types.audit_event

    return [
        None
        if item is None
        else capo_connectcases.types.audit_event.redact_sensitive(item)
        for item in value
    ]
