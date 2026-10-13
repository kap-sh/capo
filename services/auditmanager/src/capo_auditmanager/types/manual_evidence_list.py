"""Generated from Smithy shape ``com.amazonaws.auditmanager#ManualEvidenceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.manual_evidence

ManualEvidenceList: TypeAlias = list[
    "capo_auditmanager.types.manual_evidence.ManualEvidence"
]


# --- restJson1 ser/de ---
def serialize_json(value: ManualEvidenceList) -> list:
    import capo_auditmanager.types.manual_evidence

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.manual_evidence.serialize_json(item))
    return out


def deserialize_json(data: list) -> ManualEvidenceList:
    import capo_auditmanager.types.manual_evidence

    out: ManualEvidenceList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_auditmanager.types.manual_evidence.deserialize_json(item))
    return out


def redact_sensitive(value: ManualEvidenceList) -> list[Any]:
    import capo_auditmanager.types.manual_evidence

    return [
        capo_auditmanager.types.manual_evidence.redact_sensitive(item) for item in value
    ]
