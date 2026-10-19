"""Generated from Smithy shape ``com.amazonaws.freetier#GetFreeTierUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.expression
    import capo_freetier.types.max_results
    import capo_freetier.types.next_page_token


class GetFreeTierUsageRequest(TypedDict, closed=True):
    filter: NotRequired["capo_freetier.types.expression.Expression"]
    """<p>An expression that specifies the conditions that you want each <code>FreeTierUsage</code> object to meet.</p>"""
    max_results: NotRequired["capo_freetier.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. <code>MaxResults</code> means that there can be up to the specified number of values, but there might be fewer results based on your filters.</p>"""
    next_token: NotRequired["capo_freetier.types.next_page_token.NextPageToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetFreeTierUsageRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_freetier.types.expression

        out["filter"] = capo_freetier.types.expression.serialize_aws_json_1_0(
            value["filter"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetFreeTierUsageRequest:
    out: GetFreeTierUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_freetier.types.expression

        out["filter"] = capo_freetier.types.expression.deserialize_aws_json_1_0(
            data["filter"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
