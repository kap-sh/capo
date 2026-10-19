"""Generated from Smithy shape ``com.amazonaws.wafv2#GetTopPathStatisticsByTrafficResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.path_statistics_list
    import capo_wafv2.types.request_count


class GetTopPathStatisticsByTrafficResponse(TypedDict, closed=True):
    path_statistics: "capo_wafv2.types.path_statistics_list.PathStatisticsList"
    """<p>The list of path statistics, ordered by request count. Each entry includes the path, request count, percentage of total traffic, and the top bots accessing that path.</p>"""
    total_request_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The total number of requests that match the query criteria within the specified time window.</p>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    top_categories: NotRequired[
        "capo_wafv2.types.path_statistics_list.PathStatisticsList"
    ]
    """<p>Category-level aggregations for visualizing bot category to path relationships. This field is only populated when no bot filters are applied to the request. Each entry includes the bot category and the paths accessed by bots in that category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTopPathStatisticsByTrafficResponse) -> dict:
    out: dict = {}
    import capo_wafv2.types.path_statistics_list

    out["PathStatistics"] = (
        capo_wafv2.types.path_statistics_list.serialize_aws_json_1_1(
            value["path_statistics"]
        )
    )
    out["TotalRequestCount"] = value.get("total_request_count", 0)
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "top_categories" in value:
        import capo_wafv2.types.path_statistics_list

        out["TopCategories"] = (
            capo_wafv2.types.path_statistics_list.serialize_aws_json_1_1(
                value["top_categories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTopPathStatisticsByTrafficResponse:
    out: GetTopPathStatisticsByTrafficResponse = {}  # type: ignore[typeddict-item]
    if data.get("PathStatistics") is not None:
        import capo_wafv2.types.path_statistics_list

        out["path_statistics"] = (
            capo_wafv2.types.path_statistics_list.deserialize_aws_json_1_1(
                data["PathStatistics"]
            )
        )
    else:
        out["path_statistics"] = []
    if data.get("TotalRequestCount") is not None:
        out["total_request_count"] = data["TotalRequestCount"]
    else:
        out["total_request_count"] = 0
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("TopCategories") is not None:
        import capo_wafv2.types.path_statistics_list

        out["top_categories"] = (
            capo_wafv2.types.path_statistics_list.deserialize_aws_json_1_1(
                data["TopCategories"]
            )
        )
    return out
