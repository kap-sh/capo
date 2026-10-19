"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetExportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.data_set_export_summary
    import capo_m2.types.data_set_task_lifecycle
    import capo_m2.types.identifier


class GetDataSetExportTaskResponse(TypedDict, closed=True):
    task_id: "capo_m2.types.identifier.Identifier"
    """<p>The task identifier.</p>"""
    status: "capo_m2.types.data_set_task_lifecycle.DataSetTaskLifecycle"
    """<p>The status of the task.</p>"""
    summary: NotRequired["capo_m2.types.data_set_export_summary.DataSetExportSummary"]
    """<p>A summary of the status of the task.</p>"""
    status_reason: NotRequired["str"]
    """<p>If dataset export failed, the failure reason will show here.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The identifier of a customer managed key used for exported data set encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetExportTaskResponse) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    out["status"] = value["status"]
    if "summary" in value:
        import capo_m2.types.data_set_export_summary

        out["summary"] = capo_m2.types.data_set_export_summary.serialize_json(
            value["summary"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetDataSetExportTaskResponse:
    out: GetDataSetExportTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("summary") is not None:
        import capo_m2.types.data_set_export_summary

        out["summary"] = capo_m2.types.data_set_export_summary.deserialize_json(
            data["summary"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
