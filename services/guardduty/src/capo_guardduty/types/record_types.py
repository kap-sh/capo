"""Generated from Smithy shape ``com.amazonaws.guardduty#RecordTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.record_type

RecordTypes: TypeAlias = list["capo_guardduty.types.record_type.RecordType"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordTypes) -> list:
    import capo_guardduty.types.record_type

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.record_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecordTypes:
    import capo_guardduty.types.record_type

    out: RecordTypes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.record_type.deserialize_json(item))
    return out
