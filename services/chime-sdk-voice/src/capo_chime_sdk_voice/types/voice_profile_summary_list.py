"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceProfileSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_profile_summary

VoiceProfileSummaryList: TypeAlias = list[
    "capo_chime_sdk_voice.types.voice_profile_summary.VoiceProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceProfileSummaryList) -> list:
    import capo_chime_sdk_voice.types.voice_profile_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.voice_profile_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VoiceProfileSummaryList:
    import capo_chime_sdk_voice.types.voice_profile_summary

    out: VoiceProfileSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_voice.types.voice_profile_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: VoiceProfileSummaryList) -> list[Any]:
    import capo_chime_sdk_voice.types.voice_profile_summary

    return [
        capo_chime_sdk_voice.types.voice_profile_summary.redact_sensitive(item)
        for item in value
    ]
