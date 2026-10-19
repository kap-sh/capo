"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#FilterByEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.entity_id


class FilterByEntity(TypedDict, closed=True):
    entity_id: "capo_iottwinmaker.types.entity_id.EntityId"
    """<p>The entity Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterByEntity) -> dict:
    out: dict = {}
    out["entityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> FilterByEntity:
    out: FilterByEntity = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    else:
        out["entity_id"] = ""
    return out
