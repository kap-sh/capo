"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCoverageStatisticsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.coverage_filter_criteria
    import capo_inspector2.types.group_key
    import capo_inspector2.types.next_token


class ListCoverageStatisticsRequest(TypedDict, closed=True):
    filter_criteria: NotRequired[
        "capo_inspector2.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>An object that contains details on the filters to apply to the coverage data for your environment.</p>"""
    group_by: NotRequired["capo_inspector2.types.group_key.GroupKey"]
    """<p>The value to group the results by. For multi-cloud resources, use <code>PROVIDER</code>, <code>PROVIDER_ACCOUNT_ID</code> (Azure subscription ID or Google Cloud Platform (GCP) project ID), <code>PROVIDER_ORG_ID</code> (Azure tenant ID or Google Cloud Platform (GCP) organization ID), or <code>PROVIDER_REGION</code>.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the <code>NextToken</code> value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageStatisticsRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import capo_inspector2.types.coverage_filter_criteria

        out["filterCriteria"] = (
            capo_inspector2.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "group_by" in value:
        out["groupBy"] = value["group_by"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCoverageStatisticsRequest:
    out: ListCoverageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filterCriteria") is not None:
        import capo_inspector2.types.coverage_filter_criteria

        out["filter_criteria"] = (
            capo_inspector2.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if data.get("groupBy") is not None:
        out["group_by"] = data["groupBy"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
