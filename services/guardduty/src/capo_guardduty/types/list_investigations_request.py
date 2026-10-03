"""Generated from Smithy shape ``com.amazonaws.guardduty#ListInvestigationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.investigation_sort_criteria
    import capo_guardduty.types.max_results
    import capo_guardduty.types.next_token


class ListInvestigationsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector whose investigations you want to list.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    sort_criteria: NotRequired[
        "capo_guardduty.types.investigation_sort_criteria.InvestigationSortCriteria"
    ]
    """<p>Represents the criteria used for sorting investigations.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 50.</p>"""
    next_token: NotRequired["capo_guardduty.types.next_token.NextToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationsRequest) -> dict:
    out: dict = {}
    if "sort_criteria" in value:
        import capo_guardduty.types.investigation_sort_criteria

        out["sortCriteria"] = (
            capo_guardduty.types.investigation_sort_criteria.serialize_json(
                value["sort_criteria"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvestigationsRequest:
    out: ListInvestigationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sortCriteria") is not None:
        import capo_guardduty.types.investigation_sort_criteria

        out["sort_criteria"] = (
            capo_guardduty.types.investigation_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
