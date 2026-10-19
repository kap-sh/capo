"""Generated from Smithy shape ``com.amazonaws.qapps#BatchCreateCategoryInputCategory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.uuid


class BatchCreateCategoryInputCategory(TypedDict, closed=True):
    id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>The unique identifier to be associated with a category. If you don't include a value, the category is automatically assigned a unique identifier.</p>"""
    title: "str"
    """<p>The name of the category.</p>"""
    color: NotRequired["str"]
    """<p>The color to be associated with a category. The color must be a hexadecimal value of either 3 or 6 digits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateCategoryInputCategory) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["title"] = value["title"]
    if "color" in value:
        out["color"] = value["color"]
    return out


def deserialize_json(data: dict) -> BatchCreateCategoryInputCategory:
    out: BatchCreateCategoryInputCategory = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("color") is not None:
        out["color"] = data["color"]
    return out
