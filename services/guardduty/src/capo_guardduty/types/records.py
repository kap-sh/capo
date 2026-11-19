"""Generated from Smithy shape ``com.amazonaws.guardduty#Records``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_record

Records: TypeAlias = list[
    "capo_guardduty.types.investigation_record.InvestigationRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: Records) -> list:
    import capo_guardduty.types.investigation_record

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.investigation_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> Records:
    import capo_guardduty.types.investigation_record

    out: Records = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.investigation_record.deserialize_json(item))
    return out


def redact_sensitive(value: Records) -> list[Any]:
    import capo_guardduty.types.investigation_record

    return [
        capo_guardduty.types.investigation_record.redact_sensitive(item)
        for item in value
    ]
