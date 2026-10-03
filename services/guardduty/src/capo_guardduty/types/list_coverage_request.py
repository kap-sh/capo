"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCoverageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.coverage_filter_criteria
    import capo_guardduty.types.coverage_sort_criteria
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.max_results
    import capo_guardduty.types.string


class ListCoverageRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector whose coverage details you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    filter_criteria: NotRequired[
        "capo_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>Represents the criteria used to filter the coverage details.</p>"""
    sort_criteria: NotRequired[
        "capo_guardduty.types.coverage_sort_criteria.CoverageSortCriteria"
    ]
    """<p>Represents the criteria used to sort the coverage details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter_criteria" in value:
        import capo_guardduty.types.coverage_filter_criteria

        out["filterCriteria"] = (
            capo_guardduty.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "sort_criteria" in value:
        import capo_guardduty.types.coverage_sort_criteria

        out["sortCriteria"] = (
            capo_guardduty.types.coverage_sort_criteria.serialize_json(
                value["sort_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCoverageRequest:
    out: ListCoverageRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filterCriteria") is not None:
        import capo_guardduty.types.coverage_filter_criteria

        out["filter_criteria"] = (
            capo_guardduty.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if data.get("sortCriteria") is not None:
        import capo_guardduty.types.coverage_sort_criteria

        out["sort_criteria"] = (
            capo_guardduty.types.coverage_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    return out
