"""Generated from Smithy shape ``com.amazonaws.devopsguru#SearchOrganizationInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_guru.types.insight_type
    import capo_devops_guru.types.search_insights_account_id_list
    import capo_devops_guru.types.search_organization_insights_filters
    import capo_devops_guru.types.search_organization_insights_max_results
    import capo_devops_guru.types.start_time_range
    import capo_devops_guru.types.uuid_next_token


class SearchOrganizationInsightsRequest(TypedDict, closed=True):
    account_ids: "capo_devops_guru.types.search_insights_account_id_list.SearchInsightsAccountIdList"
    """<p>The ID of the Amazon Web Services account. </p>"""
    start_time_range: "capo_devops_guru.types.start_time_range.StartTimeRange"
    filters: NotRequired[
        "capo_devops_guru.types.search_organization_insights_filters.SearchOrganizationInsightsFilters"
    ]
    """<p> A <code>SearchOrganizationInsightsFilters</code> object that is used to set the severity and status filters on your insight search. </p>"""
    max_results: NotRequired[
        "capo_devops_guru.types.search_organization_insights_max_results.SearchOrganizationInsightsMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""
    type: "capo_devops_guru.types.insight_type.InsightType"
    """<p> The type of insights you are searching for (<code>REACTIVE</code> or <code>PROACTIVE</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchOrganizationInsightsRequest) -> dict:
    out: dict = {}
    import capo_devops_guru.types.search_insights_account_id_list

    out["AccountIds"] = (
        capo_devops_guru.types.search_insights_account_id_list.serialize_json(
            value["account_ids"]
        )
    )
    import capo_devops_guru.types.start_time_range

    out["StartTimeRange"] = capo_devops_guru.types.start_time_range.serialize_json(
        value["start_time_range"]
    )
    if "filters" in value:
        import capo_devops_guru.types.search_organization_insights_filters

        out["Filters"] = (
            capo_devops_guru.types.search_organization_insights_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_devops_guru.types.insight_type

    out["Type"] = capo_devops_guru.types.insight_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> SearchOrganizationInsightsRequest:
    out: SearchOrganizationInsightsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountIds") is not None:
        import capo_devops_guru.types.search_insights_account_id_list

        out["account_ids"] = (
            capo_devops_guru.types.search_insights_account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    else:
        out["account_ids"] = []
    if data.get("StartTimeRange") is not None:
        import capo_devops_guru.types.start_time_range

        out["start_time_range"] = (
            capo_devops_guru.types.start_time_range.deserialize_json(
                data["StartTimeRange"]
            )
        )
    else:
        raise DeserializationError(
            "SearchOrganizationInsightsRequest.start_time_range required"
        )
    if data.get("Filters") is not None:
        import capo_devops_guru.types.search_organization_insights_filters

        out["filters"] = (
            capo_devops_guru.types.search_organization_insights_filters.deserialize_json(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Type") is not None:
        import capo_devops_guru.types.insight_type

        out["type"] = capo_devops_guru.types.insight_type.deserialize_json(data["Type"])
    else:
        import typing

        out["type"] = typing.cast("capo_devops_guru.types.insight_type.InsightType", "")
    return out
