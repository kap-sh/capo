"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#VoiceProfileDomainSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.voice_profile_domain_summary

VoiceProfileDomainSummaryList: TypeAlias = list[
    "capo_chime_sdk_voice.types.voice_profile_domain_summary.VoiceProfileDomainSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VoiceProfileDomainSummaryList) -> list:
    import capo_chime_sdk_voice.types.voice_profile_domain_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.voice_profile_domain_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> VoiceProfileDomainSummaryList:
    import capo_chime_sdk_voice.types.voice_profile_domain_summary

    out: VoiceProfileDomainSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_voice.types.voice_profile_domain_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: VoiceProfileDomainSummaryList) -> list[Any]:
    import capo_chime_sdk_voice.types.voice_profile_domain_summary

    return [
        capo_chime_sdk_voice.types.voice_profile_domain_summary.redact_sensitive(item)
        for item in value
    ]
