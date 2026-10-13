"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Participant``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.e164_phone_number


class Participant(TypedDict, closed=True):
    phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The participant's phone number.</p>"""
    proxy_phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The participant's proxy phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Participant) -> dict:
    out: dict = {}
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "proxy_phone_number" in value:
        out["ProxyPhoneNumber"] = value["proxy_phone_number"]
    return out


def deserialize_json(data: dict) -> Participant:
    out: Participant = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("ProxyPhoneNumber") is not None:
        out["proxy_phone_number"] = data["ProxyPhoneNumber"]
    return out


def redact_sensitive(value: Participant) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number" in value:
        out["phone_number"] = "*** Sensitive Data Redacted ***"
    if "proxy_phone_number" in value:
        out["proxy_phone_number"] = "*** Sensitive Data Redacted ***"
    return out
