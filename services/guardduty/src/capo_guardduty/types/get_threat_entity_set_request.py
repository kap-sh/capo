"""Generated from Smithy shape ``com.amazonaws.guardduty#GetThreatEntitySetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.string


class GetThreatEntitySetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector associated with the threat entity set resource.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    threat_entity_set_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID that helps GuardDuty identify the threat entity set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetThreatEntitySetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetThreatEntitySetRequest:
    out: GetThreatEntitySetRequest = {}  # type: ignore[typeddict-item]
    return out
