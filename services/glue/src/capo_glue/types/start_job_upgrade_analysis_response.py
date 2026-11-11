"""Generated from Smithy shape ``com.amazonaws.glue#StartJobUpgradeAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id
    import capo_glue.types.name


class StartJobUpgradeAnalysisResponse(TypedDict, closed=True):
    analysis_id: NotRequired["capo_glue.types.id.Id"]
    """<p>The unique identifier of the upgrade analysis.</p>"""
    job_name: NotRequired["capo_glue.types.name.Name"]
    """<p>The name of the job associated with this analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartJobUpgradeAnalysisResponse) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["analysisId"] = value["analysis_id"]
    if "job_name" in value:
        out["jobName"] = value["job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartJobUpgradeAnalysisResponse:
    out: StartJobUpgradeAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    return out
