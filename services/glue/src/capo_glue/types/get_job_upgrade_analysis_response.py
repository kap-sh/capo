"""Generated from Smithy shape ``com.amazonaws.glue#GetJobUpgradeAnalysisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.analysis_type
    import capo_glue.types.id
    import capo_glue.types.name
    import capo_glue.types.status


class GetJobUpgradeAnalysisResponse(TypedDict, closed=True):
    job_name: "capo_glue.types.name.Name"
    """<p>The name of the job associated with this analysis.</p>"""
    analysis_id: "capo_glue.types.id.Id"
    """<p>The unique identifier of the upgrade analysis.</p>"""
    status: "capo_glue.types.status.Status"
    """<p>The current status of the analysis.</p>"""
    source_version: NotRequired["str"]
    """<p>The Glue version the job was running before the upgrade, for example <code>4.0</code>.</p>"""
    target_version: "str"
    """<p>The Glue version the job will be upgraded to, for example <code>6.0</code>.</p>"""
    analysis_type: NotRequired["capo_glue.types.analysis_type.AnalysisType"]
    """<p>The type of upgrade analysis. For auto-upgrade jobs, this value is <code>AUTO_UPGRADE</code>.</p>"""
    auto_upgrade_evaluation_summary: NotRequired["str"]
    """<p>The Amazon S3 URI of the terminal-state evaluation summary, available once the analysis reaches a terminal status (<code>SUCCEEDED</code> or <code>FAILED</code>).</p>"""
    error_message: NotRequired["str"]
    """<p>The reason the analysis did not complete.</p>"""
    auto_upgrade_eligibility_summary: NotRequired["str"]
    """<p>The Amazon S3 URI of the consent report summarizing upgrade assessment findings. Populated when the analysis reaches <code>WAITING_FOR_CONSENT</code> and remains available in all subsequent states.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobUpgradeAnalysisResponse) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    out["analysisId"] = value["analysis_id"]
    import capo_glue.types.status

    out["status"] = capo_glue.types.status.serialize_aws_json_1_1(value["status"])
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    out["targetVersion"] = value["target_version"]
    if "analysis_type" in value:
        import capo_glue.types.analysis_type

        out["analysisType"] = capo_glue.types.analysis_type.serialize_aws_json_1_1(
            value["analysis_type"]
        )
    if "auto_upgrade_evaluation_summary" in value:
        out["autoUpgradeEvaluationSummary"] = value["auto_upgrade_evaluation_summary"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "auto_upgrade_eligibility_summary" in value:
        out["autoUpgradeEligibilitySummary"] = value["auto_upgrade_eligibility_summary"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobUpgradeAnalysisResponse:
    out: GetJobUpgradeAnalysisResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    else:
        out["analysis_id"] = ""
    if data.get("status") is not None:
        import capo_glue.types.status

        out["status"] = capo_glue.types.status.deserialize_aws_json_1_1(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_glue.types.status.Status", "")
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("targetVersion") is not None:
        out["target_version"] = data["targetVersion"]
    else:
        out["target_version"] = ""
    if data.get("analysisType") is not None:
        import capo_glue.types.analysis_type

        out["analysis_type"] = capo_glue.types.analysis_type.deserialize_aws_json_1_1(
            data["analysisType"]
        )
    if data.get("autoUpgradeEvaluationSummary") is not None:
        out["auto_upgrade_evaluation_summary"] = data["autoUpgradeEvaluationSummary"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("autoUpgradeEligibilitySummary") is not None:
        out["auto_upgrade_eligibility_summary"] = data["autoUpgradeEligibilitySummary"]
    return out
