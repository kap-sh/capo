"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.speaker_summary

SpeakerSummaries: TypeAlias = list["capo_voice_id.types.speaker_summary.SpeakerSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerSummaries) -> list:
    import capo_voice_id.types.speaker_summary

    out: list = []
    for item in value:
        out.append(capo_voice_id.types.speaker_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SpeakerSummaries:
    import capo_voice_id.types.speaker_summary

    out: SpeakerSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_voice_id.types.speaker_summary.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: SpeakerSummaries) -> list[Any]:
    import capo_voice_id.types.speaker_summary

    return [
        capo_voice_id.types.speaker_summary.redact_sensitive(item) for item in value
    ]
