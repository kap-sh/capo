"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorProxyRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.country_list
    import capo_chime_sdk_voice.types.e164_phone_number
    import capo_chime_sdk_voice.types.integer
    import capo_chime_sdk_voice.types.voice_connector_id


class PutVoiceConnectorProxyRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    default_session_expiry_minutes: "capo_chime_sdk_voice.types.integer.Integer"
    """<p>The default number of minutes allowed for proxy session.</p>"""
    phone_number_pool_countries: "capo_chime_sdk_voice.types.country_list.CountryList"
    """<p>The countries for proxy phone numbers to be selected from.</p>"""
    fall_back_phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The phone number to route calls to after a proxy session expires.</p>"""
    disabled: NotRequired["capo_chime_sdk_voice.types.boolean.Boolean"]
    """<p>When true, stops proxy sessions from being created on the specified Amazon Chime SDK Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorProxyRequest) -> dict:
    out: dict = {}
    out["DefaultSessionExpiryMinutes"] = value["default_session_expiry_minutes"]
    import capo_chime_sdk_voice.types.country_list

    out["PhoneNumberPoolCountries"] = (
        capo_chime_sdk_voice.types.country_list.serialize_json(
            value["phone_number_pool_countries"]
        )
    )
    if "fall_back_phone_number" in value:
        out["FallBackPhoneNumber"] = value["fall_back_phone_number"]
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorProxyRequest:
    out: PutVoiceConnectorProxyRequest = {}  # type: ignore[typeddict-item]
    if data.get("DefaultSessionExpiryMinutes") is not None:
        out["default_session_expiry_minutes"] = data["DefaultSessionExpiryMinutes"]
    else:
        out["default_session_expiry_minutes"] = 0
    if data.get("PhoneNumberPoolCountries") is not None:
        import capo_chime_sdk_voice.types.country_list

        out["phone_number_pool_countries"] = (
            capo_chime_sdk_voice.types.country_list.deserialize_json(
                data["PhoneNumberPoolCountries"]
            )
        )
    else:
        out["phone_number_pool_countries"] = []
    if data.get("FallBackPhoneNumber") is not None:
        out["fall_back_phone_number"] = data["FallBackPhoneNumber"]
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    return out


def redact_sensitive(value: PutVoiceConnectorProxyRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fall_back_phone_number" in value:
        out["fall_back_phone_number"] = "*** Sensitive Data Redacted ***"
    return out
