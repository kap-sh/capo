"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.error_code
    import capo_chime_sdk_voice.types.sensitive_non_empty_string
    import capo_chime_sdk_voice.types.string


class PhoneNumberError(TypedDict, closed=True):
    phone_number_id: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The phone number ID for which the action failed.</p>"""
    error_code: NotRequired["capo_chime_sdk_voice.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberError) -> dict:
    out: dict = {}
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    if "error_code" in value:
        import capo_chime_sdk_voice.types.error_code

        out["ErrorCode"] = capo_chime_sdk_voice.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> PhoneNumberError:
    out: PhoneNumberError = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    if data.get("ErrorCode") is not None:
        import capo_chime_sdk_voice.types.error_code

        out["error_code"] = capo_chime_sdk_voice.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


def redact_sensitive(value: PhoneNumberError) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number_id" in value:
        out["phone_number_id"] = "*** Sensitive Data Redacted ***"
    return out
