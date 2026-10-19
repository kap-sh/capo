"""Generated from Smithy shape ``com.amazonaws.iot#UpdateThingGroupsForThingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.override_dynamic_groups
    import capo_iot.types.thing_group_list
    import capo_iot.types.thing_name


class UpdateThingGroupsForThingRequest(TypedDict, closed=True):
    thing_name: NotRequired["capo_iot.types.thing_name.ThingName"]
    """<p>The thing whose group memberships will be updated.</p>"""
    thing_groups_to_add: NotRequired["capo_iot.types.thing_group_list.ThingGroupList"]
    """<p>The groups to which the thing will be added.</p>"""
    thing_groups_to_remove: NotRequired[
        "capo_iot.types.thing_group_list.ThingGroupList"
    ]
    """<p>The groups from which the thing will be removed.</p>"""
    override_dynamic_groups: NotRequired[
        "capo_iot.types.override_dynamic_groups.OverrideDynamicGroups"
    ]
    """<p>Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingGroupsForThingRequest) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_groups_to_add" in value:
        import capo_iot.types.thing_group_list

        out["thingGroupsToAdd"] = capo_iot.types.thing_group_list.serialize_json(
            value["thing_groups_to_add"]
        )
    if "thing_groups_to_remove" in value:
        import capo_iot.types.thing_group_list

        out["thingGroupsToRemove"] = capo_iot.types.thing_group_list.serialize_json(
            value["thing_groups_to_remove"]
        )
    if "override_dynamic_groups" in value:
        out["overrideDynamicGroups"] = value["override_dynamic_groups"]
    return out


def deserialize_json(data: dict) -> UpdateThingGroupsForThingRequest:
    out: UpdateThingGroupsForThingRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    if data.get("thingGroupsToAdd") is not None:
        import capo_iot.types.thing_group_list

        out["thing_groups_to_add"] = capo_iot.types.thing_group_list.deserialize_json(
            data["thingGroupsToAdd"]
        )
    if data.get("thingGroupsToRemove") is not None:
        import capo_iot.types.thing_group_list

        out["thing_groups_to_remove"] = (
            capo_iot.types.thing_group_list.deserialize_json(
                data["thingGroupsToRemove"]
            )
        )
    if data.get("overrideDynamicGroups") is not None:
        out["override_dynamic_groups"] = data["overrideDynamicGroups"]
    return out
