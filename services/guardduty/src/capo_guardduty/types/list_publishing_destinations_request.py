"""Generated from Smithy shape ``com.amazonaws.guardduty#ListPublishingDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.max_results
    import capo_guardduty.types.string


class ListPublishingDestinationsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The detector ID for which you want to retrieve the publishing destination.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPublishingDestinationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPublishingDestinationsRequest:
    out: ListPublishingDestinationsRequest = {}  # type: ignore[typeddict-item]
    return out
