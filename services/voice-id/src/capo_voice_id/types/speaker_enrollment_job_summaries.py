"""Generated from Smithy shape ``com.amazonaws.voiceid#SpeakerEnrollmentJobSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.speaker_enrollment_job_summary

SpeakerEnrollmentJobSummaries: TypeAlias = list[
    "capo_voice_id.types.speaker_enrollment_job_summary.SpeakerEnrollmentJobSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpeakerEnrollmentJobSummaries) -> list:
    import capo_voice_id.types.speaker_enrollment_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_voice_id.types.speaker_enrollment_job_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SpeakerEnrollmentJobSummaries:
    import capo_voice_id.types.speaker_enrollment_job_summary

    out: SpeakerEnrollmentJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_voice_id.types.speaker_enrollment_job_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: SpeakerEnrollmentJobSummaries) -> list[Any]:
    import capo_voice_id.types.speaker_enrollment_job_summary

    return [
        capo_voice_id.types.speaker_enrollment_job_summary.redact_sensitive(item)
        for item in value
    ]
