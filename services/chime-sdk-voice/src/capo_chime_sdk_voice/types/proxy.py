"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Proxy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.e164_phone_number
    import capo_chime_sdk_voice.types.integer
    import capo_chime_sdk_voice.types.string_list


class Proxy(TypedDict, closed=True):
    default_session_expiry_minutes: NotRequired[
        "capo_chime_sdk_voice.types.integer.Integer"
    ]
    """<p>The default number of minutes allowed for proxy sessions.</p>"""
    disabled: NotRequired["capo_chime_sdk_voice.types.boolean.Boolean"]
    """<p>When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.</p>"""
    fall_back_phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The phone number to route calls to after a proxy session expires.</p>"""
    phone_number_countries: NotRequired[
        "capo_chime_sdk_voice.types.string_list.StringList"
    ]
    """<p>The countries for proxy phone numbers to be selected from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Proxy) -> dict:
    out: dict = {}
    if "default_session_expiry_minutes" in value:
        out["DefaultSessionExpiryMinutes"] = value["default_session_expiry_minutes"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    if "fall_back_phone_number" in value:
        out["FallBackPhoneNumber"] = value["fall_back_phone_number"]
    if "phone_number_countries" in value:
        import capo_chime_sdk_voice.types.string_list

        out["PhoneNumberCountries"] = (
            capo_chime_sdk_voice.types.string_list.serialize_json(
                value["phone_number_countries"]
            )
        )
    return out


def deserialize_json(data: dict) -> Proxy:
    out: Proxy = {}  # type: ignore[typeddict-item]
    if data.get("DefaultSessionExpiryMinutes") is not None:
        out["default_session_expiry_minutes"] = data["DefaultSessionExpiryMinutes"]
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    if data.get("FallBackPhoneNumber") is not None:
        out["fall_back_phone_number"] = data["FallBackPhoneNumber"]
    if data.get("PhoneNumberCountries") is not None:
        import capo_chime_sdk_voice.types.string_list

        out["phone_number_countries"] = (
            capo_chime_sdk_voice.types.string_list.deserialize_json(
                data["PhoneNumberCountries"]
            )
        )
    return out


def redact_sensitive(value: Proxy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fall_back_phone_number" in value:
        out["fall_back_phone_number"] = "*** Sensitive Data Redacted ***"
    return out
