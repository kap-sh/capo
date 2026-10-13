"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentReportsMetadata``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_report_metadata

AssessmentReportsMetadata: TypeAlias = list[
    "capo_auditmanager.types.assessment_report_metadata.AssessmentReportMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentReportsMetadata) -> list:
    import capo_auditmanager.types.assessment_report_metadata

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.assessment_report_metadata.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssessmentReportsMetadata:
    import capo_auditmanager.types.assessment_report_metadata

    out: AssessmentReportsMetadata = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.assessment_report_metadata.deserialize_json(item)
        )
    return out


def redact_sensitive(value: AssessmentReportsMetadata) -> list[Any]:
    import capo_auditmanager.types.assessment_report_metadata

    return [
        capo_auditmanager.types.assessment_report_metadata.redact_sensitive(item)
        for item in value
    ]
