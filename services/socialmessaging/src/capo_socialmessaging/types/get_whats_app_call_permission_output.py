"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppCallPermissionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_permission
    import capo_socialmessaging.types.whats_app_call_permission_action_list


class GetWhatsAppCallPermissionOutput(TypedDict, closed=True):
    permission: (
        "capo_socialmessaging.types.whats_app_call_permission.WhatsAppCallPermission"
    )
    """<p>The current calling permission state for the end user.</p>"""
    actions: "capo_socialmessaging.types.whats_app_call_permission_action_list.WhatsAppCallPermissionActionList"
    """<p>The calling actions the business can take with the end user, and any limits that apply to each action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppCallPermissionOutput) -> dict:
    out: dict = {}
    import capo_socialmessaging.types.whats_app_call_permission

    out["permission"] = (
        capo_socialmessaging.types.whats_app_call_permission.serialize_json(
            value["permission"]
        )
    )
    import capo_socialmessaging.types.whats_app_call_permission_action_list

    out["actions"] = (
        capo_socialmessaging.types.whats_app_call_permission_action_list.serialize_json(
            value["actions"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetWhatsAppCallPermissionOutput:
    out: GetWhatsAppCallPermissionOutput = {}  # type: ignore[typeddict-item]
    if data.get("permission") is not None:
        import capo_socialmessaging.types.whats_app_call_permission

        out["permission"] = (
            capo_socialmessaging.types.whats_app_call_permission.deserialize_json(
                data["permission"]
            )
        )
    else:
        raise DeserializationError(
            "GetWhatsAppCallPermissionOutput.permission required"
        )
    if data.get("actions") is not None:
        import capo_socialmessaging.types.whats_app_call_permission_action_list

        out["actions"] = (
            capo_socialmessaging.types.whats_app_call_permission_action_list.deserialize_json(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    return out
