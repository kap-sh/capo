"""Generated from Smithy shape ``com.amazonaws.qapps#CategoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.uuid


class CategoryInput(TypedDict, closed=True):
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the category.</p>"""
    title: "str"
    """<p>The name of the category.</p>"""
    color: NotRequired["str"]
    """<p>The color of the category, represented as a hexadecimal value of either 3 or 6 digits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoryInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    if "color" in value:
        out["color"] = value["color"]
    return out


def deserialize_json(data: dict) -> CategoryInput:
    out: CategoryInput = {}  # type: ignore[typeddict-item]
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
    return out
