"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControls``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_control

AssessmentControls: TypeAlias = list[
    "capo_auditmanager.types.assessment_control.AssessmentControl"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentControls) -> list:
    import capo_auditmanager.types.assessment_control

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.assessment_control.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssessmentControls:
    import capo_auditmanager.types.assessment_control

    out: AssessmentControls = []
    for item in data:
        if item is None:
            continue
        out.append(capo_auditmanager.types.assessment_control.deserialize_json(item))
    return out


def redact_sensitive(value: AssessmentControls) -> list[Any]:
    import capo_auditmanager.types.assessment_control

    return [
        capo_auditmanager.types.assessment_control.redact_sensitive(item)
        for item in value
    ]
