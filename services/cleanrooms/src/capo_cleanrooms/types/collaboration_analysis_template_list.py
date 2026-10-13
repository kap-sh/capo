"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationAnalysisTemplateList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_analysis_template

CollaborationAnalysisTemplateList: TypeAlias = list[
    "capo_cleanrooms.types.collaboration_analysis_template.CollaborationAnalysisTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationAnalysisTemplateList) -> list:
    import capo_cleanrooms.types.collaboration_analysis_template

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.collaboration_analysis_template.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CollaborationAnalysisTemplateList:
    import capo_cleanrooms.types.collaboration_analysis_template

    out: CollaborationAnalysisTemplateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cleanrooms.types.collaboration_analysis_template.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CollaborationAnalysisTemplateList) -> list[Any]:
    import capo_cleanrooms.types.collaboration_analysis_template

    return [
        capo_cleanrooms.types.collaboration_analysis_template.redact_sensitive(item)
        for item in value
    ]
