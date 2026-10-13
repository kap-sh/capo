"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#EndpointAttributes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.non_empty_sensitive_string1600


class EndpointAttributes(TypedDict, closed=True):
    device_token: "capo_chime_sdk_identity.types.non_empty_sensitive_string1600.NonEmptySensitiveString1600"
    """<p>The device token for the GCM, APNS, and APNS_SANDBOX endpoint types.</p>"""
    voip_device_token: NotRequired[
        "capo_chime_sdk_identity.types.non_empty_sensitive_string1600.NonEmptySensitiveString1600"
    ]
    """<p>The VOIP device token for the APNS and APNS_SANDBOX endpoint types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointAttributes) -> dict:
    out: dict = {}
    out["DeviceToken"] = value["device_token"]
    if "voip_device_token" in value:
        out["VoipDeviceToken"] = value["voip_device_token"]
    return out


def deserialize_json(data: dict) -> EndpointAttributes:
    out: EndpointAttributes = {}  # type: ignore[typeddict-item]
    if data.get("DeviceToken") is not None:
        out["device_token"] = data["DeviceToken"]
    else:
        raise DeserializationError("EndpointAttributes.device_token required")
    if data.get("VoipDeviceToken") is not None:
        out["voip_device_token"] = data["VoipDeviceToken"]
    return out


def redact_sensitive(value: EndpointAttributes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "device_token" in value:
        out["device_token"] = "*** Sensitive Data Redacted ***"
    if "voip_device_token" in value:
        out["voip_device_token"] = "*** Sensitive Data Redacted ***"
    return out
