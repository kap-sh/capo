"""Generated from Smithy shape ``com.amazonaws.chime#UpdatePhoneNumberSettingsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.calling_name


class UpdatePhoneNumberSettingsRequest(TypedDict, closed=True):
    calling_name: "capo_chime.types.calling_name.CallingName"
    """<p>The default outbound calling name for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberSettingsRequest) -> dict:
    out: dict = {}
    out["CallingName"] = value["calling_name"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberSettingsRequest:
    out: UpdatePhoneNumberSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CallingName") is not None:
        out["calling_name"] = data["CallingName"]
    else:
        raise DeserializationError(
            "UpdatePhoneNumberSettingsRequest.calling_name required"
        )
    return out


def redact_sensitive(value: UpdatePhoneNumberSettingsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "calling_name" in value:
        out["calling_name"] = "*** Sensitive Data Redacted ***"
    return out
