"""Generated from Smithy shape ``com.amazonaws.inspector2#GetSbomExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.report_id


class GetSbomExportRequest(TypedDict, closed=True):
    report_id: "capo_inspector2.types.report_id.ReportId"
    """<p>The report ID of the SBOM export to get details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSbomExportRequest) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> GetSbomExportRequest:
    out: GetSbomExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    return out
