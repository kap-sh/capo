"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.voice_connector_id
    import capo_chime_sdk_voice.types.voice_connector_name


class UpdateVoiceConnectorRequest(TypedDict, closed=True):
    voice_connector_id: "capo_chime_sdk_voice.types.voice_connector_id.VoiceConnectorId"
    """<p>The Voice Connector ID.</p>"""
    name: "capo_chime_sdk_voice.types.voice_connector_name.VoiceConnectorName"
    """<p>The name of the Voice Connector.</p>"""
    require_encryption: "capo_chime_sdk_voice.types.boolean.Boolean"
    """<p>When enabled, requires encryption for the Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["RequireEncryption"] = value["require_encryption"]
    return out


def deserialize_json(data: dict) -> UpdateVoiceConnectorRequest:
    out: UpdateVoiceConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("RequireEncryption") is not None:
        out["require_encryption"] = data["RequireEncryption"]
    else:
        out["require_encryption"] = False
    return out
