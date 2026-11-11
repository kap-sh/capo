"""Generated from Smithy shape ``com.amazonaws.opensearch#ClonedBlueGreenScheduledAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cloned_blue_green_scheduled_action_type
    import capo_opensearch.types.update_timestamp


class ClonedBlueGreenScheduledAction(TypedDict, closed=True):
    action: NotRequired[
        "capo_opensearch.types.cloned_blue_green_scheduled_action_type.ClonedBlueGreenScheduledActionType"
    ]
    """<p>The action that the service takes.</p>"""
    scheduled_time: NotRequired[
        "capo_opensearch.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The time at which the service takes the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClonedBlueGreenScheduledAction) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_opensearch.types.cloned_blue_green_scheduled_action_type

        out["Action"] = (
            capo_opensearch.types.cloned_blue_green_scheduled_action_type.serialize_json(
                value["action"]
            )
        )
    if "scheduled_time" in value:
        import capo_opensearch.types.update_timestamp

        out["ScheduledTime"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["scheduled_time"]
        )
    return out


def deserialize_json(data: dict) -> ClonedBlueGreenScheduledAction:
    out: ClonedBlueGreenScheduledAction = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_opensearch.types.cloned_blue_green_scheduled_action_type

        out["action"] = (
            capo_opensearch.types.cloned_blue_green_scheduled_action_type.deserialize_json(
                data["Action"]
            )
        )
    if data.get("ScheduledTime") is not None:
        import capo_opensearch.types.update_timestamp

        out["scheduled_time"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["ScheduledTime"]
        )
    return out
