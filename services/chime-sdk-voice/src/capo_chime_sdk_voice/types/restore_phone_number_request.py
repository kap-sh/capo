"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#RestorePhoneNumberRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class RestorePhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The ID of the phone number being restored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestorePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestorePhoneNumberRequest:
    out: RestorePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: RestorePhoneNumberRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number_id" in value:
        out["phone_number_id"] = "*** Sensitive Data Redacted ***"
    return out
