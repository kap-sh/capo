"""Generated from Smithy shape ``com.amazonaws.glue#AutoUpgradeMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.auto_upgrade_status
    import capo_glue.types.glue_version_string
    import capo_glue.types.id_string


class AutoUpgradeMetadata(TypedDict, closed=True):
    target_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<text>The target Glue runtime version the job is being upgraded to.</text>"""
    source_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<text>The source Glue runtime version the job was running before auto-version was enabled.</text>"""
    status: NotRequired["capo_glue.types.auto_upgrade_status.AutoUpgradeStatus"]
    """<text>The current auto-upgrade lifecycle status (OBSERVING, UPGRADING, UPGRADE_SUCCEEDED, UPGRADE_FAILED, STOPPED, WAITING_FOR_CONSENT).</text>"""
    analysis_id: NotRequired["capo_glue.types.id_string.IdString"]
    """<text>The unique identifier of the auto-upgrade assessment analysis.</text>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoUpgradeMetadata) -> dict:
    out: dict = {}
    if "target_version" in value:
        out["TargetVersion"] = value["target_version"]
    if "source_version" in value:
        out["SourceVersion"] = value["source_version"]
    if "status" in value:
        import capo_glue.types.auto_upgrade_status

        out["Status"] = capo_glue.types.auto_upgrade_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoUpgradeMetadata:
    out: AutoUpgradeMetadata = {}  # type: ignore[typeddict-item]
    if data.get("TargetVersion") is not None:
        out["target_version"] = data["TargetVersion"]
    if data.get("SourceVersion") is not None:
        out["source_version"] = data["SourceVersion"]
    if data.get("Status") is not None:
        import capo_glue.types.auto_upgrade_status

        out["status"] = capo_glue.types.auto_upgrade_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("AnalysisId") is not None:
        out["analysis_id"] = data["AnalysisId"]
    return out
