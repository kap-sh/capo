"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdateVoiceProfileDomainResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_profile_domain


class UpdateVoiceProfileDomainResponse(TypedDict, closed=True):
    voice_profile_domain: NotRequired[
        "capo_chime_sdk_voice.types.voice_profile_domain.VoiceProfileDomain"
    ]
    """<p>The updated details of the voice profile domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVoiceProfileDomainResponse) -> dict:
    out: dict = {}
    if "voice_profile_domain" in value:
        import capo_chime_sdk_voice.types.voice_profile_domain

        out["VoiceProfileDomain"] = (
            capo_chime_sdk_voice.types.voice_profile_domain.serialize_json(
                value["voice_profile_domain"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateVoiceProfileDomainResponse:
    out: UpdateVoiceProfileDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("VoiceProfileDomain") is not None:
        import capo_chime_sdk_voice.types.voice_profile_domain

        out["voice_profile_domain"] = (
            capo_chime_sdk_voice.types.voice_profile_domain.deserialize_json(
                data["VoiceProfileDomain"]
            )
        )
    return out


def redact_sensitive(value: UpdateVoiceProfileDomainResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "voice_profile_domain" in value:
        import capo_chime_sdk_voice.types.voice_profile_domain

        out["voice_profile_domain"] = (
            capo_chime_sdk_voice.types.voice_profile_domain.redact_sensitive(
                value["voice_profile_domain"]
            )
        )
    return out
