"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DNISEmergencyCallingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.alpha2_country_code
    import capo_chime_sdk_voice.types.e164_phone_number


class DNISEmergencyCallingConfiguration(TypedDict, closed=True):
    emergency_phone_number: (
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    )
    """<p>The DNIS phone number that you route emergency calls to, in E.164 format.</p>"""
    test_phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The DNIS phone number for routing test emergency calls to, in E.164 format.</p>"""
    calling_country: "capo_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
    """<p>The country from which emergency calls are allowed, in ISO 3166-1 alpha-2 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DNISEmergencyCallingConfiguration) -> dict:
    out: dict = {}
    out["EmergencyPhoneNumber"] = value["emergency_phone_number"]
    if "test_phone_number" in value:
        out["TestPhoneNumber"] = value["test_phone_number"]
    out["CallingCountry"] = value["calling_country"]
    return out


def deserialize_json(data: dict) -> DNISEmergencyCallingConfiguration:
    out: DNISEmergencyCallingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EmergencyPhoneNumber") is not None:
        out["emergency_phone_number"] = data["EmergencyPhoneNumber"]
    else:
        out["emergency_phone_number"] = ""
    if data.get("TestPhoneNumber") is not None:
        out["test_phone_number"] = data["TestPhoneNumber"]
    if data.get("CallingCountry") is not None:
        out["calling_country"] = data["CallingCountry"]
    else:
        out["calling_country"] = ""
    return out


def redact_sensitive(value: DNISEmergencyCallingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "emergency_phone_number" in value:
        out["emergency_phone_number"] = "*** Sensitive Data Redacted ***"
    if "test_phone_number" in value:
        out["test_phone_number"] = "*** Sensitive Data Redacted ***"
    return out
