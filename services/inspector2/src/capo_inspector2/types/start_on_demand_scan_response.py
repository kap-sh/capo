"""Generated from Smithy shape ``com.amazonaws.inspector2#StartOnDemandScanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.scan_id


class StartOnDemandScanResponse(TypedDict, closed=True):
    scan_id: "capo_inspector2.types.scan_id.ScanId"
    """<p>The unique identifier assigned to the on-demand scan that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOnDemandScanResponse) -> dict:
    out: dict = {}
    out["scanId"] = value["scan_id"]
    return out


def deserialize_json(data: dict) -> StartOnDemandScanResponse:
    out: StartOnDemandScanResponse = {}  # type: ignore[typeddict-item]
    if data.get("scanId") is not None:
        out["scan_id"] = data["scanId"]
    else:
        out["scan_id"] = ""
    return out
