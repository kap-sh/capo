"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_job


class GetCallAnalyticsJobResponse(TypedDict, closed=True):
    call_analytics_job: NotRequired[
        "capo_transcribe.types.call_analytics_job.CallAnalyticsJob"
    ]
    """<p>Provides detailed information about the specified Call Analytics job, including job status and, if applicable, failure reason.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsJobResponse) -> dict:
    out: dict = {}
    if "call_analytics_job" in value:
        import capo_transcribe.types.call_analytics_job

        out["CallAnalyticsJob"] = (
            capo_transcribe.types.call_analytics_job.serialize_aws_json_1_1(
                value["call_analytics_job"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsJobResponse:
    out: GetCallAnalyticsJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("CallAnalyticsJob") is not None:
        import capo_transcribe.types.call_analytics_job

        out["call_analytics_job"] = (
            capo_transcribe.types.call_analytics_job.deserialize_aws_json_1_1(
                data["CallAnalyticsJob"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCallAnalyticsJobResponse) -> dict:
    out: dict = {}
    if "call_analytics_job" in value:
        import capo_transcribe.types.call_analytics_job

        out["CallAnalyticsJob"] = (
            capo_transcribe.types.call_analytics_job.serialize_cbor(
                value["call_analytics_job"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetCallAnalyticsJobResponse:
    out: GetCallAnalyticsJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("CallAnalyticsJob") is not None:
        import capo_transcribe.types.call_analytics_job

        out["call_analytics_job"] = (
            capo_transcribe.types.call_analytics_job.deserialize_cbor(
                data["CallAnalyticsJob"]
            )
        )
    return out
