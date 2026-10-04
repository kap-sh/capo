"""Generated from Smithy shape ``com.amazonaws.health#DescribeServiceLifecycleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.lifecycle_max_results
    import capo_health.types.next_token
    import capo_health.types.service_lifecycle_filter


class DescribeServiceLifecycleRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_health.types.service_lifecycle_filter.ServiceLifecycleFilter"
    ]
    """<p>Values to narrow the results returned.</p>"""
    next_token: NotRequired["capo_health.types.next_token.nextToken"]
    """<p>If the results of a search are large, only a portion of the results are returned, and a <code>nextToken</code> pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.</p>"""
    max_results: NotRequired[
        "capo_health.types.lifecycle_max_results.LifecycleMaxResults"
    ]
    """<p>The maximum number of items to return in one batch, between 1 and 20, inclusive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServiceLifecycleRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_health.types.service_lifecycle_filter

        out["filter"] = (
            capo_health.types.service_lifecycle_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServiceLifecycleRequest:
    out: DescribeServiceLifecycleRequest = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_health.types.service_lifecycle_filter

        out["filter"] = (
            capo_health.types.service_lifecycle_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
