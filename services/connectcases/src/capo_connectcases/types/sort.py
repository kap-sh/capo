"""Generated from Smithy shape ``com.amazonaws.connectcases#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_id
    import capo_connectcases.types.order


class Sort(TypedDict, closed=True):
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>Unique identifier of a field.</p>"""
    sort_order: "capo_connectcases.types.order.Order"
    """<p>A structured set of sort terms</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if data.get("fieldId") is not None:
        out["field_id"] = data["fieldId"]
    else:
        out["field_id"] = ""
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    else:
        out["sort_order"] = ""
    return out
