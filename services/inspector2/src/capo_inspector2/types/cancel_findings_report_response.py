"""Generated from Smithy shape ``com.amazonaws.inspector2#CancelFindingsReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.report_id


class CancelFindingsReportResponse(TypedDict, closed=True):
    report_id: "capo_inspector2.types.report_id.ReportId"
    """<p>The ID of the canceled report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelFindingsReportResponse) -> dict:
    out: dict = {}
    out["reportId"] = value["report_id"]
    return out


def deserialize_json(data: dict) -> CancelFindingsReportResponse:
    out: CancelFindingsReportResponse = {}  # type: ignore[typeddict-item]
    if data.get("reportId") is not None:
        out["report_id"] = data["reportId"]
    else:
        out["report_id"] = ""
    return out
