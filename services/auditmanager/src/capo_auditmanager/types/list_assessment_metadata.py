"""Generated from Smithy shape ``com.amazonaws.auditmanager#ListAssessmentMetadata``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_metadata_item

ListAssessmentMetadata: TypeAlias = list[
    "capo_auditmanager.types.assessment_metadata_item.AssessmentMetadataItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssessmentMetadata) -> list:
    import capo_auditmanager.types.assessment_metadata_item

    out: list = []
    for item in value:
        out.append(
            capo_auditmanager.types.assessment_metadata_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListAssessmentMetadata:
    import capo_auditmanager.types.assessment_metadata_item

    out: ListAssessmentMetadata = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_auditmanager.types.assessment_metadata_item.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ListAssessmentMetadata) -> list[Any]:
    import capo_auditmanager.types.assessment_metadata_item

    return [
        capo_auditmanager.types.assessment_metadata_item.redact_sensitive(item)
        for item in value
    ]
