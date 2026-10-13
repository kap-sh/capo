"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_profile


class UpdateVoiceProfileResponse(TypedDict, closed=True):
    voice_profile: NotRequired["capo_chime_sdk_voice.types.voice_profile.VoiceProfile"]
    """<p>The updated voice profile settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceProfileResponse) -> dict:
    out: dict = {}
    if "voice_profile" in value:
        import capo_chime_sdk_voice.types.voice_profile

        out["VoiceProfile"] = capo_chime_sdk_voice.types.voice_profile.serialize_json(
            value["voice_profile"]
        )
    return out


def deserialize_json(data: dict) -> UpdateVoiceProfileResponse:
    out: UpdateVoiceProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfile") is not None:
        import capo_chime_sdk_voice.types.voice_profile

        out["voice_profile"] = (
            capo_chime_sdk_voice.types.voice_profile.deserialize_json(
                data["VoiceProfile"]
            )
        )
    return out


def redact_sensitive(value: UpdateVoiceProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profile" in value:
        import capo_chime_sdk_voice.types.voice_profile

        out["voice_profile"] = (
            capo_chime_sdk_voice.types.voice_profile.redact_sensitive(
                value["voice_profile"]
            )
        )
    return out
