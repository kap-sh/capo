"""Generated from Smithy shape ``com.amazonaws.securityhub#CancelExportJobV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_job_id


class CancelExportJobV2Request(TypedDict, closed=True):
    export_job_id: "capo_securityhub.types.export_job_id.ExportJobId"
    """<p>The unique identifier of the export job to cancel. This is the value returned by <code>StartExportJobV2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelExportJobV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelExportJobV2Request:
    out: CancelExportJobV2Request = {}  # type: ignore[typeddict-item]
    return out
