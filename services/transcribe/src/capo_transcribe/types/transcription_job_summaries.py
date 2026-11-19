"""Generated from Smithy shape ``com.amazonaws.transcribe#TranscriptionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.transcription_job_summary

TranscriptionJobSummaries: TypeAlias = list[
    "capo_transcribe.types.transcription_job_summary.TranscriptionJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranscriptionJobSummaries) -> list:
    import capo_transcribe.types.transcription_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.transcription_job_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TranscriptionJobSummaries:
    import capo_transcribe.types.transcription_job_summary

    out: TranscriptionJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.transcription_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TranscriptionJobSummaries) -> list:
    import capo_transcribe.types.transcription_job_summary

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.transcription_job_summary.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TranscriptionJobSummaries:
    import capo_transcribe.types.transcription_job_summary

    out: TranscriptionJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.transcription_job_summary.deserialize_cbor(item)
        )
    return out
