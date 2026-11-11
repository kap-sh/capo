"""Generated from Smithy shape ``com.amazonaws.glue#StartJobUpgradeAnalysisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id
    import capo_glue.types.name
    import capo_glue.types.upgrade_consent


class StartJobUpgradeAnalysisRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name.Name"
    """<p>The name of the job associated with the analysis to resume.</p>"""
    analysis_id: NotRequired["capo_glue.types.id.Id"]
    """<p>The unique identifier of the upgrade analysis. The analysis must be in <code>WAITING_FOR_CONSENT</code> status.</p>"""
    upgrade_consent: NotRequired["capo_glue.types.upgrade_consent.UpgradeConsent"]
    """<p>The customer's decision on whether to proceed with the upgrade.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartJobUpgradeAnalysisRequest) -> dict:
    out: dict = {}
    out["jobName"] = value["job_name"]
    if "analysis_id" in value:
        out["analysisId"] = value["analysis_id"]
    if "upgrade_consent" in value:
        import capo_glue.types.upgrade_consent

        out["upgradeConsent"] = capo_glue.types.upgrade_consent.serialize_aws_json_1_1(
            value["upgrade_consent"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartJobUpgradeAnalysisRequest:
    out: StartJobUpgradeAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("jobName") is not None:
        out["job_name"] = data["jobName"]
    else:
        out["job_name"] = ""
    if data.get("analysisId") is not None:
        out["analysis_id"] = data["analysisId"]
    if data.get("upgradeConsent") is not None:
        import capo_glue.types.upgrade_consent

        out["upgrade_consent"] = (
            capo_glue.types.upgrade_consent.deserialize_aws_json_1_1(
                data["upgradeConsent"]
            )
        )
    return out
