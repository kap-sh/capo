"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.visual_custom_action_name
    import capo_quicksight.types.visual_custom_action_operation_list
    import capo_quicksight.types.visual_custom_action_trigger
    import capo_quicksight.types.widget_status


class VisualCustomAction(TypedDict, closed=True):
    custom_action_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the <code>VisualCustomAction</code>.</p>"""
    name: "capo_quicksight.types.visual_custom_action_name.VisualCustomActionName"
    """<p>The name of the <code>VisualCustomAction</code>.</p>"""
    status: NotRequired["capo_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the <code>VisualCustomAction</code>.</p>"""
    trigger: (
        "capo_quicksight.types.visual_custom_action_trigger.VisualCustomActionTrigger"
    )
    """<p>The trigger of the <code>VisualCustomAction</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>DATA_POINT_CLICK</code>: Initiates a custom action by a left pointer click on a data point.</p> </li> <li> <p> <code>DATA_POINT_MENU</code>: Initiates a custom action by right pointer click from the menu.</p> </li> </ul>"""
    action_operations: "capo_quicksight.types.visual_custom_action_operation_list.VisualCustomActionOperationList"
    """<p>A list of <code>VisualCustomActionOperations</code>.</p> <p>This is a union type structure. For this structure to be valid, only one of the attributes can be defined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomAction) -> dict:
    out: dict = {}
    out["CustomActionId"] = value["custom_action_id"]
    out["Name"] = value["name"]
    if "status" in value:
        import capo_quicksight.types.widget_status

        out["Status"] = capo_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    import capo_quicksight.types.visual_custom_action_trigger

    out["Trigger"] = capo_quicksight.types.visual_custom_action_trigger.serialize_json(
        value["trigger"]
    )
    import capo_quicksight.types.visual_custom_action_operation_list

    out["ActionOperations"] = (
        capo_quicksight.types.visual_custom_action_operation_list.serialize_json(
            value["action_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> VisualCustomAction:
    out: VisualCustomAction = {}  # type: ignore[typeddict-item]
    if data.get("CustomActionId") is not None:
        out["custom_action_id"] = data["CustomActionId"]
    else:
        out["custom_action_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Status") is not None:
        import capo_quicksight.types.widget_status

        out["status"] = capo_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if data.get("Trigger") is not None:
        import capo_quicksight.types.visual_custom_action_trigger

        out["trigger"] = (
            capo_quicksight.types.visual_custom_action_trigger.deserialize_json(
                data["Trigger"]
            )
        )
    else:
        import typing

        out["trigger"] = typing.cast(
            "capo_quicksight.types.visual_custom_action_trigger.VisualCustomActionTrigger",
            "",
        )
    if data.get("ActionOperations") is not None:
        import capo_quicksight.types.visual_custom_action_operation_list

        out["action_operations"] = (
            capo_quicksight.types.visual_custom_action_operation_list.deserialize_json(
                data["ActionOperations"]
            )
        )
    else:
        out["action_operations"] = []
    return out


def redact_sensitive(value: VisualCustomAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action_operations" in value:
        import capo_quicksight.types.visual_custom_action_operation_list

        out["action_operations"] = (
            capo_quicksight.types.visual_custom_action_operation_list.redact_sensitive(
                value["action_operations"]
            )
        )
    return out
