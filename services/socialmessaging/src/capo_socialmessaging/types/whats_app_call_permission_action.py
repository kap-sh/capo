"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallPermissionAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_permission_action_name
    import capo_socialmessaging.types.whats_app_call_permission_limit_list


class WhatsAppCallPermissionAction(TypedDict, closed=True):
    action_name: "capo_socialmessaging.types.whats_app_call_permission_action_name.WhatsAppCallPermissionActionName"
    """<p>The name of the calling action.</p>"""
    can_perform_action: "bool"
    """<p>Specifies whether the business can currently perform the action.</p>"""
    limits: "capo_socialmessaging.types.whats_app_call_permission_limit_list.WhatsAppCallPermissionLimitList"
    """<p>The time-bound limits that apply to the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallPermissionAction) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    out["canPerformAction"] = value["can_perform_action"]
    import capo_socialmessaging.types.whats_app_call_permission_limit_list

    out["limits"] = (
        capo_socialmessaging.types.whats_app_call_permission_limit_list.serialize_json(
            value["limits"]
        )
    )
    return out


def deserialize_json(data: dict) -> WhatsAppCallPermissionAction:
    out: WhatsAppCallPermissionAction = {}  # type: ignore[typeddict-item]
    if data.get("actionName") is not None:
        out["action_name"] = data["actionName"]
    else:
        out["action_name"] = ""
    if data.get("canPerformAction") is not None:
        out["can_perform_action"] = data["canPerformAction"]
    else:
        out["can_perform_action"] = False
    if data.get("limits") is not None:
        import capo_socialmessaging.types.whats_app_call_permission_limit_list

        out["limits"] = (
            capo_socialmessaging.types.whats_app_call_permission_limit_list.deserialize_json(
                data["limits"]
            )
        )
    else:
        out["limits"] = []
    return out
