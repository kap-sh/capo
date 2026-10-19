"""Generated from Smithy shape ``com.amazonaws.inspector2#SortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.sort_field
    import capo_inspector2.types.sort_order


class SortCriteria(TypedDict, closed=True):
    field: "capo_inspector2.types.sort_field.SortField"
    """<p>The finding detail field by which results are sorted.</p>"""
    sort_order: "capo_inspector2.types.sort_order.SortOrder"
    """<p>The order by which findings are sorted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    out["sortOrder"] = value["sort_order"]
    return out


def deserialize_json(data: dict) -> SortCriteria:
    out: SortCriteria = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    else:
        out["sort_order"] = ""
    return out
