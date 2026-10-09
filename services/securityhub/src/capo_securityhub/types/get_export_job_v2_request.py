"""Generated from Smithy shape ``com.amazonaws.securityhub#GetExportJobV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_job_id


class GetExportJobV2Request(TypedDict, closed=True):
    export_job_id: "capo_securityhub.types.export_job_id.ExportJobId"
    """<p>The unique identifier of the export job to retrieve. This is the value returned by <code>StartExportJobV2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExportJobV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExportJobV2Request:
    out: GetExportJobV2Request = {}  # type: ignore[typeddict-item]
    return out
