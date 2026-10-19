"""Generated from Smithy shape ``com.amazonaws.iot#DeprecateThingTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.thing_type_name
    import capo_iot.types.undo_deprecate


class DeprecateThingTypeRequest(TypedDict, closed=True):
    thing_type_name: "capo_iot.types.thing_type_name.ThingTypeName"
    """<p>The name of the thing type to deprecate.</p>"""
    undo_deprecate: NotRequired["capo_iot.types.undo_deprecate.UndoDeprecate"]
    """<p>Whether to undeprecate a deprecated thing type. If <b>true</b>, the thing type will not be deprecated anymore and you can associate it with things.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecateThingTypeRequest) -> dict:
    out: dict = {}
    if "undo_deprecate" in value:
        out["undoDeprecate"] = value["undo_deprecate"]
    return out


def deserialize_json(data: dict) -> DeprecateThingTypeRequest:
    out: DeprecateThingTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("undoDeprecate") is not None:
        out["undo_deprecate"] = data["undoDeprecate"]
    return out
