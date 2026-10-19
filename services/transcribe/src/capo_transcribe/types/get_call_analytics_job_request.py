"""Generated from Smithy shape ``com.amazonaws.transcribe#GetCallAnalyticsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.call_analytics_job_name


class GetCallAnalyticsJobRequest(TypedDict, closed=True):
    call_analytics_job_name: (
        "capo_transcribe.types.call_analytics_job_name.CallAnalyticsJobName"
    )
    """<p>The name of the Call Analytics job you want information about. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCallAnalyticsJobRequest) -> dict:
    out: dict = {}
    out["CallAnalyticsJobName"] = value["call_analytics_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCallAnalyticsJobRequest:
    out: GetCallAnalyticsJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("CallAnalyticsJobName") is not None:
        out["call_analytics_job_name"] = data["CallAnalyticsJobName"]
    else:
        out["call_analytics_job_name"] = ""
    return out
