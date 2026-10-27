"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateScheduleActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.schedule_action_operations
    import capo_elementalinference.types.schedule_action_start_configuration


class CreateScheduleActionRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>Specifies the ID of the feed that you want to add the schedule action to.</p>"""
    action_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A name for the schedule action. The name must be unique within the feed. You can reuse the name of an action that you deleted. </p>"""
    start_configuration: "capo_elementalinference.types.schedule_action_start_configuration.ScheduleActionStartConfiguration"
    """<p>Specifies when the action runs.</p>"""
    operations: "capo_elementalinference.types.schedule_action_operations.ScheduleActionOperations"
    """<p>Specifies the list of configuration changes that you want to make to the feed. Elemental Inference applies all the operations in an action together, in the order that you specify them. If any operation fails, Elemental Inference doesn't apply any of them. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleActionRequest) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    import capo_elementalinference.types.schedule_action_start_configuration

    out["startConfiguration"] = (
        capo_elementalinference.types.schedule_action_start_configuration.serialize_json(
            value["start_configuration"]
        )
    )
    import capo_elementalinference.types.schedule_action_operations

    out["operations"] = (
        capo_elementalinference.types.schedule_action_operations.serialize_json(
            value["operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateScheduleActionRequest:
    out: CreateScheduleActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("startConfiguration") is not None:
        import capo_elementalinference.types.schedule_action_start_configuration

        out["start_configuration"] = (
            capo_elementalinference.types.schedule_action_start_configuration.deserialize_json(
                data["startConfiguration"]
            )
        )
    else:
        out["start_configuration"] = {"$unknown": {"name": ""}}
    if data.get("operations") is not None:
        import capo_elementalinference.types.schedule_action_operations

        out["operations"] = (
            capo_elementalinference.types.schedule_action_operations.deserialize_json(
                data["operations"]
            )
        )
    else:
        out["operations"] = []
    return out
