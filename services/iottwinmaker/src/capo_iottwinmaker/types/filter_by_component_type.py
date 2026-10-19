"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FilterByComponentType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.component_type_id


class FilterByComponentType(TypedDict, closed=True):
    component_type_id: "capo_iottwinmaker.types.component_type_id.ComponentTypeId"
    """<p>The component type Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterByComponentType) -> dict:
    out: dict = {}
    out["componentTypeId"] = value["component_type_id"]
    return out


def deserialize_json(data: dict) -> FilterByComponentType:
    out: FilterByComponentType = {}  # type: ignore[typeddict-item]
    if data.get("componentTypeId") is not None:
        out["component_type_id"] = data["componentTypeId"]
    else:
        out["component_type_id"] = ""
    return out
