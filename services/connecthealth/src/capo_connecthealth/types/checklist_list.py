"""Generated from Smithy shape ``com.amazonaws.connecthealth#ChecklistList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.checklist

ChecklistList: TypeAlias = list["capo_connecthealth.types.checklist.Checklist"]


# --- restJson1 ser/de ---
def serialize_json(value: ChecklistList) -> list:
    import capo_connecthealth.types.checklist

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.checklist.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChecklistList:
    import capo_connecthealth.types.checklist

    out: ChecklistList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connecthealth.types.checklist.deserialize_json(item))
    return out


def redact_sensitive(value: ChecklistList) -> list[Any]:
    import capo_connecthealth.types.checklist

    return [capo_connecthealth.types.checklist.redact_sensitive(item) for item in value]
