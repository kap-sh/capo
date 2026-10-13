"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.image_custom_action_name
    import capo_quicksight.types.image_custom_action_operation_list
    import capo_quicksight.types.image_custom_action_trigger
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.widget_status


class ImageCustomAction(TypedDict, closed=True):
    custom_action_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the custom action.</p>"""
    name: "capo_quicksight.types.image_custom_action_name.ImageCustomActionName"
    """<p>The name of the custom action.</p>"""
    status: NotRequired["capo_quicksight.types.widget_status.WidgetStatus"]
    """<p>The status of the custom action.</p>"""
    trigger: (
        "capo_quicksight.types.image_custom_action_trigger.ImageCustomActionTrigger"
    )
    """<p>The trigger of the <code>VisualCustomAction</code>.</p> <p>Valid values are defined as follows:</p> <ul> <li> <p> <code>CLICK</code>: Initiates a custom action by a left pointer click on a data point.</p> </li> <li> <p> <code>MENU</code>: Initiates a custom action by right pointer click from the menu.</p> </li> </ul>"""
    action_operations: "capo_quicksight.types.image_custom_action_operation_list.ImageCustomActionOperationList"
    """<p>A list of <code>ImageCustomActionOperations</code>.</p> <p>This is a union type structure. For this structure to be valid, only one of the attributes can be defined.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageCustomAction) -> dict:
    out: dict = {}
    out["CustomActionId"] = value["custom_action_id"]
    out["Name"] = value["name"]
    if "status" in value:
        import capo_quicksight.types.widget_status

        out["Status"] = capo_quicksight.types.widget_status.serialize_json(
            value["status"]
        )
    import capo_quicksight.types.image_custom_action_trigger

    out["Trigger"] = capo_quicksight.types.image_custom_action_trigger.serialize_json(
        value["trigger"]
    )
    import capo_quicksight.types.image_custom_action_operation_list

    out["ActionOperations"] = (
        capo_quicksight.types.image_custom_action_operation_list.serialize_json(
            value["action_operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ImageCustomAction:
    out: ImageCustomAction = {}  # type: ignore[typeddict-item]
    if data.get("CustomActionId") is not None:
        out["custom_action_id"] = data["CustomActionId"]
    else:
        raise DeserializationError("ImageCustomAction.custom_action_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ImageCustomAction.name required")
    if data.get("Status") is not None:
        import capo_quicksight.types.widget_status

        out["status"] = capo_quicksight.types.widget_status.deserialize_json(
            data["Status"]
        )
    if data.get("Trigger") is not None:
        import capo_quicksight.types.image_custom_action_trigger

        out["trigger"] = (
            capo_quicksight.types.image_custom_action_trigger.deserialize_json(
                data["Trigger"]
            )
        )
    else:
        raise DeserializationError("ImageCustomAction.trigger required")
    if data.get("ActionOperations") is not None:
        import capo_quicksight.types.image_custom_action_operation_list

        out["action_operations"] = (
            capo_quicksight.types.image_custom_action_operation_list.deserialize_json(
                data["ActionOperations"]
            )
        )
    else:
        raise DeserializationError("ImageCustomAction.action_operations required")
    return out


def redact_sensitive(value: ImageCustomAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action_operations" in value:
        import capo_quicksight.types.image_custom_action_operation_list

        out["action_operations"] = (
            capo_quicksight.types.image_custom_action_operation_list.redact_sensitive(
                value["action_operations"]
            )
        )
    return out
