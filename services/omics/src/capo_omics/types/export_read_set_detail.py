"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.job_status_message
    import capo_omics.types.read_set_export_job_item_status
    import capo_omics.types.read_set_id


class ExportReadSetDetail(TypedDict, closed=True):
    id: "capo_omics.types.read_set_id.ReadSetId"
    """<p>The set's ID.</p>"""
    status: (
        "capo_omics.types.read_set_export_job_item_status.ReadSetExportJobItemStatus"
    )
    """<p>The set's status.</p>"""
    status_message: NotRequired["capo_omics.types.job_status_message.JobStatusMessage"]
    """<p>The set's status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetDetail) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ExportReadSetDetail:
    out: ExportReadSetDetail = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    return out
