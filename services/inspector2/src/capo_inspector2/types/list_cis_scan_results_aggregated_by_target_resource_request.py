"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanResultsAggregatedByTargetResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria
    import capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by
    import capo_inspector2.types.cis_scan_results_max_results
    import capo_inspector2.types.cis_sort_order
    import capo_inspector2.types.next_token


class ListCisScanResultsAggregatedByTargetResourceRequest(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN.</p>"""
    filter_criteria: NotRequired[
        "capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.CisScanResultsAggregatedByTargetResourceFilterCriteria"
    ]
    """<p>The filter criteria.</p>"""
    sort_by: NotRequired[
        "capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.CisScanResultsAggregatedByTargetResourceSortBy"
    ]
    """<p>The sort by order.</p>"""
    sort_order: NotRequired["capo_inspector2.types.cis_sort_order.CisSortOrder"]
    """<p>The sort order.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_inspector2.types.cis_scan_results_max_results.CisScanResultsMaxResults"
    ]
    """<p>The maximum number of scan results aggregated by a target resource to be returned in a single page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanResultsAggregatedByTargetResourceRequest) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "filter_criteria" in value:
        import capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria

        out["filterCriteria"] = (
            capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "sort_by" in value:
        import capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by

        out["sortBy"] = (
            capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_inspector2.types.cis_sort_order

        out["sortOrder"] = capo_inspector2.types.cis_sort_order.serialize_json(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListCisScanResultsAggregatedByTargetResourceRequest:
    out: ListCisScanResultsAggregatedByTargetResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanArn") is not None:
        out["scan_arn"] = data["scanArn"]
    else:
        out["scan_arn"] = ""
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria

        out["filter_criteria"] = (
            capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by

        out["sort_by"] = (
            capo_inspector2.types.cis_scan_results_aggregated_by_target_resource_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_inspector2.types.cis_sort_order

        out["sort_order"] = capo_inspector2.types.cis_sort_order.deserialize_json(
            data["sortOrder"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
