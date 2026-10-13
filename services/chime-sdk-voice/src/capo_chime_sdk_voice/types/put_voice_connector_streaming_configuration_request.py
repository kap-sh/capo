"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorStreamingConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.streaming_configuration
    import capo_chime_sdk_voice.types.voice_connector_id


class PutVoiceConnectorStreamingConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    streaming_configuration: (
        "capo_chime_sdk_voice.types.streaming_configuration.StreamingConfiguration"
    )
    """<p>The streaming settings being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorStreamingConfigurationRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.streaming_configuration

    out["StreamingConfiguration"] = (
        capo_chime_sdk_voice.types.streaming_configuration.serialize_json(
            value["streaming_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorStreamingConfigurationRequest:
    out: PutVoiceConnectorStreamingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("StreamingConfiguration") is not None:
        import capo_chime_sdk_voice.types.streaming_configuration

        out["streaming_configuration"] = (
            capo_chime_sdk_voice.types.streaming_configuration.deserialize_json(
                data["StreamingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorStreamingConfigurationRequest.streaming_configuration required"
        )
    return out


def redact_sensitive(
    value: PutVoiceConnectorStreamingConfigurationRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "streaming_configuration" in value:
        import capo_chime_sdk_voice.types.streaming_configuration

        out["streaming_configuration"] = (
            capo_chime_sdk_voice.types.streaming_configuration.redact_sensitive(
                value["streaming_configuration"]
            )
        )
    return out
