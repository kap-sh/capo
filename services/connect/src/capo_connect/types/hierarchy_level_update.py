"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyLevelUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_level_name


class HierarchyLevelUpdate(TypedDict, closed=True):
    name: "capo_connect.types.hierarchy_level_name.HierarchyLevelName"
    """<p>The name of the user hierarchy level. Must not be more than 50 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyLevelUpdate) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> HierarchyLevelUpdate:
    out: HierarchyLevelUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
