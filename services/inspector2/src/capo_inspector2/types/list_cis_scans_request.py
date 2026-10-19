"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_sort_order
    import capo_inspector2.types.list_cis_scans_detail_level
    import capo_inspector2.types.list_cis_scans_filter_criteria
    import capo_inspector2.types.list_cis_scans_max_results
    import capo_inspector2.types.list_cis_scans_sort_by
    import capo_inspector2.types.next_token


class ListCisScansRequest(TypedDict, closed=True):
    filter_criteria: NotRequired[
        "capo_inspector2.types.list_cis_scans_filter_criteria.ListCisScansFilterCriteria"
    ]
    """<p>The CIS scan filter criteria.</p>"""
    detail_level: NotRequired[
        "capo_inspector2.types.list_cis_scans_detail_level.ListCisScansDetailLevel"
    ]
    """<p>The detail applied to the CIS scan.</p>"""
    sort_by: NotRequired[
        "capo_inspector2.types.list_cis_scans_sort_by.ListCisScansSortBy"
    ]
    """<p>The CIS scans sort by order.</p>"""
    sort_order: NotRequired["capo_inspector2.types.cis_sort_order.CisSortOrder"]
    """<p>The CIS scans sort order.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_inspector2.types.list_cis_scans_max_results.ListCisScansMaxResults"
    ]
    """<p>The maximum number of results to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScansRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import capo_inspector2.types.list_cis_scans_filter_criteria

        out["filterCriteria"] = (
            capo_inspector2.types.list_cis_scans_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "detail_level" in value:
        import capo_inspector2.types.list_cis_scans_detail_level

        out["detailLevel"] = (
            capo_inspector2.types.list_cis_scans_detail_level.serialize_json(
                value["detail_level"]
            )
        )
    if "sort_by" in value:
        import capo_inspector2.types.list_cis_scans_sort_by

        out["sortBy"] = capo_inspector2.types.list_cis_scans_sort_by.serialize_json(
            value["sort_by"]
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


def deserialize_json(data: dict) -> ListCisScansRequest:
    out: ListCisScansRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.list_cis_scans_filter_criteria

        out["filter_criteria"] = (
            capo_inspector2.types.list_cis_scans_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if data.get("detailLevel") is not None:
        import capo_inspector2.types.list_cis_scans_detail_level

        out["detail_level"] = (
            capo_inspector2.types.list_cis_scans_detail_level.deserialize_json(
                data["detailLevel"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_inspector2.types.list_cis_scans_sort_by

        out["sort_by"] = capo_inspector2.types.list_cis_scans_sort_by.deserialize_json(
            data["sortBy"]
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
