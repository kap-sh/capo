"""Generated from Smithy shape ``com.amazonaws.iot#AddThingToThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.override_dynamic_groups
    import capo_iot.types.thing_arn
    import capo_iot.types.thing_group_arn
    import capo_iot.types.thing_group_name
    import capo_iot.types.thing_name


class AddThingToThingGroupRequest(TypedDict, closed=True):
    thing_group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>The name of the group to which you are adding a thing.</p>"""
    thing_group_arn: NotRequired["capo_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The ARN of the group to which you are adding a thing.</p>"""
    thing_name: NotRequired["capo_iot.types.thing_name.ThingName"]
    """<p>The name of the thing to add to a group.</p>"""
    thing_arn: NotRequired["capo_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing to add to a group.</p>"""
    override_dynamic_groups: NotRequired[
        "capo_iot.types.override_dynamic_groups.OverrideDynamicGroups"
    ]
    """<p>Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddThingToThingGroupRequest) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_arn" in value:
        out["thingGroupArn"] = value["thing_group_arn"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    if "override_dynamic_groups" in value:
        out["overrideDynamicGroups"] = value["override_dynamic_groups"]
    return out


def deserialize_json(data: dict) -> AddThingToThingGroupRequest:
    out: AddThingToThingGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("thingGroupName") is not None:
        out["thing_group_name"] = data["thingGroupName"]
    if data.get("thingGroupArn") is not None:
        out["thing_group_arn"] = data["thingGroupArn"]
    if data.get("thingName") is not None:
        out["thing_name"] = data["thingName"]
    if data.get("thingArn") is not None:
        out["thing_arn"] = data["thingArn"]
    if data.get("overrideDynamicGroups") is not None:
        out["override_dynamic_groups"] = data["overrideDynamicGroups"]
    return out
