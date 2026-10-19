"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.data_set_import_summary
    import capo_m2.types.data_set_task_lifecycle
    import capo_m2.types.identifier


class DataSetImportTask(TypedDict, closed=True):
    task_id: "capo_m2.types.identifier.Identifier"
    """<p>The identifier of the data set import task.</p>"""
    status: "capo_m2.types.data_set_task_lifecycle.DataSetTaskLifecycle"
    """<p>The status of the data set import task.</p>"""
    summary: "capo_m2.types.data_set_import_summary.DataSetImportSummary"
    """<p>A summary of the data set import task.</p>"""
    status_reason: NotRequired["str"]
    """<p>If dataset import failed, the failure reason will show here.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportTask) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    out["status"] = value["status"]
    import capo_m2.types.data_set_import_summary

    out["summary"] = capo_m2.types.data_set_import_summary.serialize_json(
        value["summary"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> DataSetImportTask:
    out: DataSetImportTask = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("summary") is not None:
        import capo_m2.types.data_set_import_summary

        out["summary"] = capo_m2.types.data_set_import_summary.deserialize_json(
            data["summary"]
        )
    else:
        raise DeserializationError("DataSetImportTask.summary required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    return out
