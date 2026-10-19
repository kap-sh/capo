"""Generated from Smithy shape ``com.amazonaws.qapps#Category``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.uuid


class Category(TypedDict, closed=True):
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the category.</p>"""
    title: "str"
    """<p>The title or name of the category.</p>"""
    color: NotRequired["str"]
    """<p>The color of the category</p>"""
    app_count: NotRequired["int"]
    """<p>The number of published Amazon Q Apps associated with a category</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    if "color" in value:
        out["color"] = value["color"]
    if "app_count" in value:
        out["appCount"] = value["app_count"]
    return out


def deserialize_json(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("color") is not None:
        out["color"] = data["color"]
    if data.get("appCount") is not None:
        out["app_count"] = data["appCount"]
    return out
