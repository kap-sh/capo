"""Generated from Smithy shape ``com.amazonaws.connecthealth#Checklist``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.checklist_id
    import capo_connecthealth.types.checklist_item_list


class Checklist(TypedDict, closed=True):
    checklist_id: "capo_connecthealth.types.checklist_id.ChecklistId"
    """<p>The identifier of the checklist. For a managed note template, this value is the template type, such as <code>HISTORY_AND_PHYSICAL</code>. For a custom note template, this value is <code>CUSTOM_</code> followed by the template base, such as <code>CUSTOM_GIRPP</code>.</p>"""
    items: "capo_connecthealth.types.checklist_item_list.ChecklistItemList"
    """<p>The checklist items in template order. The list contains one item for each checklist section, including sections that have not been discussed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Checklist) -> dict:
    out: dict = {}
    out["checklistId"] = value["checklist_id"]
    import capo_connecthealth.types.checklist_item_list

    out["items"] = capo_connecthealth.types.checklist_item_list.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> Checklist:
    out: Checklist = {}  # type: ignore[typeddict-item]
    if data.get("checklistId") is not None:
        out["checklist_id"] = data["checklistId"]
    else:
        out["checklist_id"] = ""
    if data.get("items") is not None:
        import capo_connecthealth.types.checklist_item_list

        out["items"] = capo_connecthealth.types.checklist_item_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    return out


def redact_sensitive(value: Checklist) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_connecthealth.types.checklist_item_list

        out["items"] = capo_connecthealth.types.checklist_item_list.redact_sensitive(
            value["items"]
        )
    return out
