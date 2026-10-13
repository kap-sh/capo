"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFrameworkShareRequestList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_framework_share_request

AssessmentFrameworkShareRequestList: TypeAlias = list[
    "capo_auditmanager.types.assessment_framework_share_request.AssessmentFrameworkShareRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFrameworkShareRequestList) -> list:
    import capo_auditmanager.types.assessment_framework_share_request

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.assessment_framework_share_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssessmentFrameworkShareRequestList:
    import capo_auditmanager.types.assessment_framework_share_request

    out: AssessmentFrameworkShareRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.assessment_framework_share_request.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AssessmentFrameworkShareRequestList) -> list[Any]:
    import capo_auditmanager.types.assessment_framework_share_request

    return [
        capo_auditmanager.types.assessment_framework_share_request.redact_sensitive(
            item
        )
        for item in value
    ]
