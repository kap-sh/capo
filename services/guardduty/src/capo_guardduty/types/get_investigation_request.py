"""Generated from Smithy shape ``com.amazonaws.guardduty#GetInvestigationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.investigation_id


class GetInvestigationRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector associated with the investigation.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    investigation_id: "capo_guardduty.types.investigation_id.InvestigationId"
    """<p>The unique identifier of the investigation to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvestigationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetInvestigationRequest:
    out: GetInvestigationRequest = {}  # type: ignore[typeddict-item]
    return out
