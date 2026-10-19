"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Sort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.boolean_optional
    import capo_resiliencehub.types.string255


class Sort(TypedDict, closed=True):
    field: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the order in which you want to sort the metrics. By default, the list is sorted in ascending order. To sort the list in descending order, set this field to False.</p>"""
    ascending: NotRequired["capo_resiliencehub.types.boolean_optional.BooleanOptional"]
    """<p>Indicates the name or identifier of the field or attribute that should be used as the basis for sorting the metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Sort) -> dict:
    out: dict = {}
    out["field"] = value["field"]
    if "ascending" in value:
        out["ascending"] = value["ascending"]
    return out


def deserialize_json(data: dict) -> Sort:
    out: Sort = {}  # type: ignore[typeddict-item]
    if data.get("field") is not None:
        out["field"] = data["field"]
    else:
        out["field"] = ""
    if data.get("ascending") is not None:
        out["ascending"] = data["ascending"]
    return out
