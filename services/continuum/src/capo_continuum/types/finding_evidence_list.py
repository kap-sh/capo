"""Generated from Smithy shape ``com.amazonaws.continuum#FindingEvidenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.finding_evidence

FindingEvidenceList: TypeAlias = list[
    "capo_continuum.types.finding_evidence.FindingEvidence"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingEvidenceList) -> list:
    import capo_continuum.types.finding_evidence

    out: list = []
    for item in value:
        out.append(capo_continuum.types.finding_evidence.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingEvidenceList:
    import capo_continuum.types.finding_evidence

    out: FindingEvidenceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.finding_evidence.deserialize_json(item))
    return out
