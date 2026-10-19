"""Generated from Smithy shape ``com.amazonaws.notifications#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.text_part_reference


class Dimension(TypedDict, closed=True):
    name: "capo_notifications.types.text_part_reference.TextPartReference"
    """<p>The name of the dimension</p>"""
    value: "capo_notifications.types.text_part_reference.TextPartReference"
    """<p>The value of the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
