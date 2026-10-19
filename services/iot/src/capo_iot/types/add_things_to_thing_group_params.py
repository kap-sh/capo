"""Generated from Smithy shape ``com.amazonaws.iot#AddThingsToThingGroupParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.nullable_boolean
    import capo_iot.types.thing_group_names


class AddThingsToThingGroupParams(TypedDict, closed=True):
    thing_group_names: "capo_iot.types.thing_group_names.ThingGroupNames"
    """<p>The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you can't add a thing to more than one group in the same hierarchy.</p>"""
    override_dynamic_groups: NotRequired[
        "capo_iot.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddThingsToThingGroupParams) -> dict:
    out: dict = {}
    import capo_iot.types.thing_group_names

    out["thingGroupNames"] = capo_iot.types.thing_group_names.serialize_json(
        value["thing_group_names"]
    )
    if "override_dynamic_groups" in value:
        out["overrideDynamicGroups"] = value["override_dynamic_groups"]
    return out


def deserialize_json(data: dict) -> AddThingsToThingGroupParams:
    out: AddThingsToThingGroupParams = {}  # type: ignore[typeddict-item]
    if data.get("thingGroupNames") is not None:
        import capo_iot.types.thing_group_names

        out["thing_group_names"] = capo_iot.types.thing_group_names.deserialize_json(
            data["thingGroupNames"]
        )
    else:
        out["thing_group_names"] = []
    if data.get("overrideDynamicGroups") is not None:
        out["override_dynamic_groups"] = data["overrideDynamicGroups"]
    return out
