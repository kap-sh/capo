"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorTerminationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.termination
    import capo_chime_sdk_voice.types.voice_connector_id


class PutVoiceConnectorTerminationRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    termination: "capo_chime_sdk_voice.types.termination.Termination"
    """<p>The termination settings to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorTerminationRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_voice.types.termination

    out["Termination"] = capo_chime_sdk_voice.types.termination.serialize_json(
        value["termination"]
    )
    return out


def deserialize_json(data: dict) -> PutVoiceConnectorTerminationRequest:
    out: PutVoiceConnectorTerminationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Termination") is not None:
        import capo_chime_sdk_voice.types.termination

        out["termination"] = capo_chime_sdk_voice.types.termination.deserialize_json(
            data["Termination"]
        )
    else:
        raise DeserializationError(
            "PutVoiceConnectorTerminationRequest.termination required"
        )
    return out


def redact_sensitive(value: PutVoiceConnectorTerminationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "termination" in value:
        import capo_chime_sdk_voice.types.termination

        out["termination"] = capo_chime_sdk_voice.types.termination.redact_sensitive(
            value["termination"]
        )
    return out
