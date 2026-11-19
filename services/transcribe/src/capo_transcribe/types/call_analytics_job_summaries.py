"""Generated from Smithy shape ``com.amazonaws.transcribe#CallAnalyticsJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_job_summary

CallAnalyticsJobSummaries: TypeAlias = list[
    "capo_transcribe.types.call_analytics_job_summary.CallAnalyticsJobSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CallAnalyticsJobSummaries) -> list:
    import capo_transcribe.types.call_analytics_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.call_analytics_job_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CallAnalyticsJobSummaries:
    import capo_transcribe.types.call_analytics_job_summary

    out: CallAnalyticsJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.call_analytics_job_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CallAnalyticsJobSummaries) -> list:
    import capo_transcribe.types.call_analytics_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_transcribe.types.call_analytics_job_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> CallAnalyticsJobSummaries:
    import capo_transcribe.types.call_analytics_job_summary

    out: CallAnalyticsJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.call_analytics_job_summary.deserialize_cbor(item)
        )
    return out
