"""Generated from Smithy shape ``com.amazonaws.connect#TranscriptCriteriaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.transcript_criteria

TranscriptCriteriaList: TypeAlias = list[
    "capo_connect.types.transcript_criteria.TranscriptCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: TranscriptCriteriaList) -> list:
    import capo_connect.types.transcript_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.transcript_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> TranscriptCriteriaList:
    import capo_connect.types.transcript_criteria

    out: TranscriptCriteriaList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.transcript_criteria.deserialize_json(item))
    return out


def redact_sensitive(value: TranscriptCriteriaList) -> list[Any]:
    import capo_connect.types.transcript_criteria

    return [
        capo_connect.types.transcript_criteria.redact_sensitive(item) for item in value
    ]
