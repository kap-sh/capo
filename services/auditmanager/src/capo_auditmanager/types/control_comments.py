"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlComments``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.control_comment

ControlComments: TypeAlias = list[
    "capo_auditmanager.types.control_comment.ControlComment"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlComments) -> list:
    import capo_auditmanager.types.control_comment

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.control_comment.serialize_json(item))
    return out


def deserialize_json(data: list) -> ControlComments:
    import capo_auditmanager.types.control_comment

    out: ControlComments = []
    for item in data:
        if item is None:
            continue
        out.append(capo_auditmanager.types.control_comment.deserialize_json(item))
    return out


def redact_sensitive(value: ControlComments) -> list[Any]:
    import capo_auditmanager.types.control_comment

    return [
        capo_auditmanager.types.control_comment.redact_sensitive(item) for item in value
    ]
