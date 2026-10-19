"""Generated from Smithy shape ``com.amazonaws.connect#CreatePushNotificationRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.registration_id


class CreatePushNotificationRegistrationResponse(TypedDict, closed=True):
    registration_id: "capo_connect.types.registration_id.RegistrationId"
    """<p>The identifier for the registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePushNotificationRegistrationResponse) -> dict:
    out: dict = {}
    out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_json(data: dict) -> CreatePushNotificationRegistrationResponse:
    out: CreatePushNotificationRegistrationResponse = {}  # type: ignore[typeddict-item]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    return out
