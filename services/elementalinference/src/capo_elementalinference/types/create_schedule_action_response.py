"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateScheduleActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.schedule_action_error
    import capo_elementalinference.types.schedule_action_operations
    import capo_elementalinference.types.schedule_action_start_configuration
    import capo_elementalinference.types.schedule_action_status


class CreateScheduleActionResponse(TypedDict, closed=True):
    action_name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>The name that you specified.</p>"""
    start_configuration: "capo_elementalinference.types.schedule_action_start_configuration.ScheduleActionStartConfiguration"
    """<p>Specifies when the action runs.</p>"""
    operations: "capo_elementalinference.types.schedule_action_operations.ScheduleActionOperations"
    """<p>The configuration changes that the action makes to the feed.</p>"""
    status: "capo_elementalinference.types.schedule_action_status.ScheduleActionStatus"
    """<p>The status of the action. After you create the action successfully, Elemental Inference sets the status to PENDING. </p>"""
    error: NotRequired[
        "capo_elementalinference.types.schedule_action_error.ScheduleActionError"
    ]
    """<p>A description of why the action failed. Elemental Inference returns this property only when the status is FAILED. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScheduleActionResponse) -> dict:
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
    import capo_elementalinference.types.schedule_action_status

    out["status"] = capo_elementalinference.types.schedule_action_status.serialize_json(
        value["status"]
    )
    if "error" in value:
        import capo_elementalinference.types.schedule_action_error

        out["error"] = (
            capo_elementalinference.types.schedule_action_error.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateScheduleActionResponse:
    out: CreateScheduleActionResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("status") is not None:
        import capo_elementalinference.types.schedule_action_status

        out["status"] = (
            capo_elementalinference.types.schedule_action_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.schedule_action_status.ScheduleActionStatus",
            "",
        )
    if data.get("error") is not None:
        import capo_elementalinference.types.schedule_action_error

        out["error"] = (
            capo_elementalinference.types.schedule_action_error.deserialize_json(
                data["error"]
            )
        )
    return out
