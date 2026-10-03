"""Generated from Smithy shape ``com.amazonaws.guardduty#ListThreatIntelSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.max_results
    import capo_guardduty.types.string


class ListThreatIntelSetsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector that is associated with the threatIntelSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>You can use this parameter to paginate results in the response. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatIntelSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThreatIntelSetsRequest:
    out: ListThreatIntelSetsRequest = {}  # type: ignore[typeddict-item]
    return out
