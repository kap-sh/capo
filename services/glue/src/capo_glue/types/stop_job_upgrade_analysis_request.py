"""Generated from Smithy shape ``com.amazonaws.glue#StopJobUpgradeAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id
    import capo_glue.types.name


class StopJobUpgradeAnalysisRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name.Name"
    """<p>The name of the job associated with the analysis.</p>"""
    analysis_id: "capo_glue.types.id.Id"
    """<p>The unique identifier of the analysis to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopJobUpgradeAnalysisRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["analysisId"] = value["analysis_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopJobUpgradeAnalysisRequest:
    out: StopJobUpgradeAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    else:
        out["analysis_id"] = ""
    return out
