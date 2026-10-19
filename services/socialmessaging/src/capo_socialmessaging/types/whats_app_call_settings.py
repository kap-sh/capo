"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.whats_app_call_hours
    import capo_socialmessaging.types.whats_app_call_icon_visibility
    import capo_socialmessaging.types.whats_app_callback_permission_status


class WhatsAppCallSettings(TypedDict, closed=True):
    call_enabled: "bool"
    """<p>Specifies whether calling is enabled for the phone number.</p>"""
    call_hours: NotRequired[
        "capo_socialmessaging.types.whats_app_call_hours.WhatsAppCallHours"
    ]
    """<p>The hours during which the business accepts calls on the phone number.</p>"""
    call_icon_visibility: NotRequired[
        "capo_socialmessaging.types.whats_app_call_icon_visibility.WhatsAppCallIconVisibility"
    ]
    """<p>The visibility setting for the call icon shown to end users in WhatsApp.</p>"""
    callback_permission_status: NotRequired[
        "capo_socialmessaging.types.whats_app_callback_permission_status.WhatsAppCallbackPermissionStatus"
    ]
    """<p>The callback permission status for the phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallSettings) -> dict:
    out: dict = {}
    out["callEnabled"] = value["call_enabled"]
    if "call_hours" in value:
        import capo_socialmessaging.types.whats_app_call_hours

        out["callHours"] = (
            capo_socialmessaging.types.whats_app_call_hours.serialize_json(
                value["call_hours"]
            )
        )
    if "call_icon_visibility" in value:
        out["callIconVisibility"] = value["call_icon_visibility"]
    if "callback_permission_status" in value:
        out["callbackPermissionStatus"] = value["callback_permission_status"]
    return out


def deserialize_json(data: dict) -> WhatsAppCallSettings:
    out: WhatsAppCallSettings = {}  # type: ignore[typeddict-item]
    if data.get("callEnabled") is not None:
        out["call_enabled"] = data["callEnabled"]
    else:
        out["call_enabled"] = False
    if data.get("callHours") is not None:
        import capo_socialmessaging.types.whats_app_call_hours

        out["call_hours"] = (
            capo_socialmessaging.types.whats_app_call_hours.deserialize_json(
                data["callHours"]
            )
        )
    if data.get("callIconVisibility") is not None:
        out["call_icon_visibility"] = data["callIconVisibility"]
    if data.get("callbackPermissionStatus") is not None:
        out["callback_permission_status"] = data["callbackPermissionStatus"]
    return out
