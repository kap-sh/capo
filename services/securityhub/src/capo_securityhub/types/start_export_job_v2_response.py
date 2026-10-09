"""Generated from Smithy shape ``com.amazonaws.securityhub#StartExportJobV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_job_id


class StartExportJobV2Response(TypedDict, closed=True):
    export_job_id: NotRequired["capo_securityhub.types.export_job_id.ExportJobId"]
    """<p>The unique identifier of the export job that Security Hub started. Use this value with <code>GetExportJobV2</code> or <code>CancelExportJobV2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportJobV2Response) -> dict:
    out: dict = {}
    if "export_job_id" in value:
        out["ExportJobId"] = value["export_job_id"]
    return out


def deserialize_json(data: dict) -> StartExportJobV2Response:
    out: StartExportJobV2Response = {}  # type: ignore[typeddict-item]
    if data.get("ExportJobId") is not None:
        out["export_job_id"] = data["ExportJobId"]
    return out
