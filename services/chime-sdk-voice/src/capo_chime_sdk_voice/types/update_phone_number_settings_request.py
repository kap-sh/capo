"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdatePhoneNumberSettingsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.calling_name


class UpdatePhoneNumberSettingsRequest(TypedDict, closed=True):
    calling_name: "capo_chime_sdk_voice.types.calling_name.CallingName"
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
        out["calling_name"] = ""
    return out


def redact_sensitive(value: UpdatePhoneNumberSettingsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "calling_name" in value:
        out["calling_name"] = "*** Sensitive Data Redacted ***"
    return out
