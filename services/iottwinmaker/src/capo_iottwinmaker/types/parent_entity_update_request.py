"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ParentEntityUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.parent_entity_id
    import capo_iottwinmaker.types.parent_entity_update_type


class ParentEntityUpdateRequest(TypedDict, closed=True):
    update_type: (
        "capo_iottwinmaker.types.parent_entity_update_type.ParentEntityUpdateType"
    )
    """<p>The type of the update.</p>"""
    parent_entity_id: NotRequired[
        "capo_iottwinmaker.types.parent_entity_id.ParentEntityId"
    ]
    """<p>The ID of the parent entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParentEntityUpdateRequest) -> dict:
    out: dict = {}
    out["updateType"] = value["update_type"]
    if "parent_entity_id" in value:
        out["parentEntityId"] = value["parent_entity_id"]
    return out


def deserialize_json(data: dict) -> ParentEntityUpdateRequest:
    out: ParentEntityUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("updateType") is not None:
        out["update_type"] = data["updateType"]
    else:
        out["update_type"] = ""
    if data.get("parentEntityId") is not None:
        out["parent_entity_id"] = data["parentEntityId"]
    return out
