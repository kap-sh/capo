"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppCallPermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_socialmessaging.types.whats_app_call_permission_status


class WhatsAppCallPermission(TypedDict, closed=True):
    status: "capo_socialmessaging.types.whats_app_call_permission_status.WhatsAppCallPermissionStatus"
    """<p>The permission status for the end user.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>The time when a temporary permission expires. This value is absent for permanent permissions and when there is no permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppCallPermission) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "expiration_time" in value:
        import capo_socialmessaging.types._prelude.timestamp

        out["expirationTime"] = (
            capo_socialmessaging.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> WhatsAppCallPermission:
    out: WhatsAppCallPermission = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("expirationTime") is not None:
        import capo_socialmessaging.types._prelude.timestamp

        out["expiration_time"] = (
            capo_socialmessaging.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    return out
