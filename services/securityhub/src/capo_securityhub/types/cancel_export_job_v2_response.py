"""Generated from Smithy shape ``com.amazonaws.securityhub#CancelExportJobV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_job_id
    import capo_securityhub.types.export_status


class CancelExportJobV2Response(TypedDict, closed=True):
    export_job_id: NotRequired["capo_securityhub.types.export_job_id.ExportJobId"]
    """<p>The unique identifier of the export job.</p>"""
    status: NotRequired["capo_securityhub.types.export_status.ExportStatus"]
    """<p>The state of the export job after the cancel request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelExportJobV2Response) -> dict:
    out: dict = {}
    if "export_job_id" in value:
        out["ExportJobId"] = value["export_job_id"]
    if "status" in value:
        import capo_securityhub.types.export_status

        out["Status"] = capo_securityhub.types.export_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> CancelExportJobV2Response:
    out: CancelExportJobV2Response = {}  # type: ignore[typeddict-item]
    if data.get("ExportJobId") is not None:
        out["export_job_id"] = data["ExportJobId"]
    if data.get("Status") is not None:
        import capo_securityhub.types.export_status

        out["status"] = capo_securityhub.types.export_status.deserialize_json(
            data["Status"]
        )
    return out
