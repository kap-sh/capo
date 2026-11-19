"""Generated from Smithy shape ``com.amazonaws.connecthealth#ChecklistItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.checklist_item

ChecklistItemList: TypeAlias = list[
    "capo_connecthealth.types.checklist_item.ChecklistItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChecklistItemList) -> list:
    import capo_connecthealth.types.checklist_item

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.checklist_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChecklistItemList:
    import capo_connecthealth.types.checklist_item

    out: ChecklistItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connecthealth.types.checklist_item.deserialize_json(item))
    return out


def redact_sensitive(value: ChecklistItemList) -> list[Any]:
    import capo_connecthealth.types.checklist_item

    return [
        capo_connecthealth.types.checklist_item.redact_sensitive(item) for item in value
    ]
