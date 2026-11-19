"""Generated from Smithy shape ``com.amazonaws.connecthealth#ChecklistItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.checklist_item_key
    import capo_connecthealth.types.checklist_item_status


class ChecklistItem(TypedDict, closed=True):
    item_key: "capo_connecthealth.types.checklist_item_key.ChecklistItemKey"
    """<p>The key that uniquely identifies the item within the checklist. For a managed note template, this value is a service-defined section key, such as <code>CHIEF_COMPLAINT</code>. For a custom note template, this value is the <code>sectionHeader</code> of the section that you defined.</p>"""
    status: "capo_connecthealth.types.checklist_item_status.ChecklistItemStatus"
    """<p>The discussion status of the checklist item. The following values are valid:</p> <ul> <li> <p> <code>DISCUSSED</code>: The conversation has covered the item.</p> </li> <li> <p> <code>PARTIALLY_DISCUSSED</code>: The conversation has covered part of the item.</p> </li> <li> <p> <code>NOT_DISCUSSED</code>: The conversation has not covered the item.</p> </li> </ul> <p>The status usually progresses toward <code>DISCUSSED</code>, but it can return to <code>NOT_DISCUSSED</code> if a speaker retracts a statement.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChecklistItem) -> dict:
    out: dict = {}
    out["itemKey"] = value["item_key"]
    import capo_connecthealth.types.checklist_item_status

    out["status"] = capo_connecthealth.types.checklist_item_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ChecklistItem:
    out: ChecklistItem = {}  # type: ignore[typeddict-item]
    if data.get("itemKey") is not None:
        out["item_key"] = data["itemKey"]
    else:
        out["item_key"] = ""
    if data.get("status") is not None:
        import capo_connecthealth.types.checklist_item_status

        out["status"] = capo_connecthealth.types.checklist_item_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connecthealth.types.checklist_item_status.ChecklistItemStatus", ""
        )
    return out


def redact_sensitive(value: ChecklistItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "item_key" in value:
        out["item_key"] = "*** Sensitive Data Redacted ***"
    return out
