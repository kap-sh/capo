"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentControlSets``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_control_set

AssessmentControlSets: TypeAlias = list[
    "capo_auditmanager.types.assessment_control_set.AssessmentControlSet"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentControlSets) -> list:
    import capo_auditmanager.types.assessment_control_set

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.assessment_control_set.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssessmentControlSets:
    import capo_auditmanager.types.assessment_control_set

    out: AssessmentControlSets = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.assessment_control_set.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AssessmentControlSets) -> list[Any]:
    import capo_auditmanager.types.assessment_control_set

    return [
        capo_auditmanager.types.assessment_control_set.redact_sensitive(item)
        for item in value
    ]
