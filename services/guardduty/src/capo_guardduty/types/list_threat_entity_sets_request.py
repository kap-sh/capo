"""Generated from Smithy shape ``com.amazonaws.guardduty#ListThreatEntitySetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.max_results
    import capo_guardduty.types.string


class ListThreatEntitySetsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector that is associated with this threat entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatEntitySetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThreatEntitySetsRequest:
    out: ListThreatEntitySetsRequest = {}  # type: ignore[typeddict-item]
    return out
