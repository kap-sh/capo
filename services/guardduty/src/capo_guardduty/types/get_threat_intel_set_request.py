"""Generated from Smithy shape ``com.amazonaws.guardduty#GetThreatIntelSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class GetThreatIntelSetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    threat_intel_set_id: "capo_guardduty.types.string.String"
    """<p>The unique ID of the threatIntelSet that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThreatIntelSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetThreatIntelSetRequest:
    out: GetThreatIntelSetRequest = {}  # type: ignore[typeddict-item]
    return out
