"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorEmergencyCallingConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.emergency_calling_configuration
    import capo_chime_sdk_voice.types.voice_connector_id


class PutVoiceConnectorEmergencyCallingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    emergency_calling_configuration: "capo_chime_sdk_voice.types.emergency_calling_configuration.EmergencyCallingConfiguration"
    """<p>The configuration being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PutVoiceConnectorEmergencyCallingConfigurationRequest,
) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.emergency_calling_configuration

    out["EmergencyCallingConfiguration"] = (
        capo_chime_sdk_voice.types.emergency_calling_configuration.serialize_json(
            value["emergency_calling_configuration"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> PutVoiceConnectorEmergencyCallingConfigurationRequest:
    out: PutVoiceConnectorEmergencyCallingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmergencyCallingConfiguration") is not None:
        import capo_chime_sdk_voice.types.emergency_calling_configuration

        out["emergency_calling_configuration"] = (
            capo_chime_sdk_voice.types.emergency_calling_configuration.deserialize_json(
                data["EmergencyCallingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorEmergencyCallingConfigurationRequest.emergency_calling_configuration required"
        )
    return out


def redact_sensitive(
    value: PutVoiceConnectorEmergencyCallingConfigurationRequest,
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
