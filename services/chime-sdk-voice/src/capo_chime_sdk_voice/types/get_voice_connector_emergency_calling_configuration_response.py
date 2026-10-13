"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetVoiceConnectorEmergencyCallingConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.emergency_calling_configuration


class GetVoiceConnectorEmergencyCallingConfigurationResponse(TypedDict, closed=True):
    emergency_calling_configuration: NotRequired[
        "capo_chime_sdk_voice.types.emergency_calling_configuration.EmergencyCallingConfiguration"
    ]
    """<p>The details of the emergency calling configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetVoiceConnectorEmergencyCallingConfigurationResponse,
) -> dict:
    out: dict = {}
    if "emergency_calling_configuration" in value:
        import capo_chime_sdk_voice.types.emergency_calling_configuration

        out["EmergencyCallingConfiguration"] = (
            capo_chime_sdk_voice.types.emergency_calling_configuration.serialize_json(
                value["emergency_calling_configuration"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> GetVoiceConnectorEmergencyCallingConfigurationResponse:
    out: GetVoiceConnectorEmergencyCallingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("EmergencyCallingConfiguration") is not None:
        import capo_chime_sdk_voice.types.emergency_calling_configuration

        out["emergency_calling_configuration"] = (
            capo_chime_sdk_voice.types.emergency_calling_configuration.deserialize_json(
                data["EmergencyCallingConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: GetVoiceConnectorEmergencyCallingConfigurationResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "emergency_calling_configuration" in value:
        import capo_chime_sdk_voice.types.emergency_calling_configuration

        out["emergency_calling_configuration"] = (
            capo_chime_sdk_voice.types.emergency_calling_configuration.redact_sensitive(
                value["emergency_calling_configuration"]
            )
        )
    return out
