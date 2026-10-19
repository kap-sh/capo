"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ComponentPropertyGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.boolean
    import capo_iottwinmaker.types.group_type
    import capo_iottwinmaker.types.property_names


class ComponentPropertyGroupResponse(TypedDict, closed=True):
    group_type: "capo_iottwinmaker.types.group_type.GroupType"
    """<p>The group type.</p>"""
    property_names: "capo_iottwinmaker.types.property_names.PropertyNames"
    """<p>The names of properties</p>"""
    is_inherited: "capo_iottwinmaker.types.boolean.Boolean"
    """<p>A Boolean value that specifies whether the property group is inherited from a parent entity</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentPropertyGroupResponse) -> dict:
    out: dict = {}
    out["groupType"] = value["group_type"]
    import capo_iottwinmaker.types.property_names

    out["propertyNames"] = capo_iottwinmaker.types.property_names.serialize_json(
        value["property_names"]
    )
    out["isInherited"] = value["is_inherited"]
    return out


def deserialize_json(data: dict) -> ComponentPropertyGroupResponse:
    out: ComponentPropertyGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("groupType") is not None:
        out["group_type"] = data["groupType"]
    else:
        out["group_type"] = ""
    if data.get("propertyNames") is not None:
        import capo_iottwinmaker.types.property_names

        out["property_names"] = capo_iottwinmaker.types.property_names.deserialize_json(
            data["propertyNames"]
        )
    else:
        out["property_names"] = []
    if data.get("isInherited") is not None:
        out["is_inherited"] = data["isInherited"]
    else:
        out["is_inherited"] = False
    return out
