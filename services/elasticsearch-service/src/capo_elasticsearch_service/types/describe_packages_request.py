"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.describe_packages_filter_list
    import capo_elasticsearch_service.types.max_results
    import capo_elasticsearch_service.types.next_token


class DescribePackagesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_elasticsearch_service.types.describe_packages_filter_list.DescribePackagesFilterList"
    ]
    """<p>Only returns packages that match the <code>DescribePackagesFilterList</code> values.</p>"""
    max_results: NotRequired["capo_elasticsearch_service.types.max_results.MaxResults"]
    """<p>Limits results to a maximum number of packages.</p>"""
    next_token: NotRequired["capo_elasticsearch_service.types.next_token.NextToken"]
    """<p>Used for pagination. Only necessary if a previous API call includes a non-null NextToken value. If provided, returns results for the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_elasticsearch_service.types.describe_packages_filter_list

        out["Filters"] = (
            capo_elasticsearch_service.types.describe_packages_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribePackagesRequest:
    out: DescribePackagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_elasticsearch_service.types.describe_packages_filter_list

        out["filters"] = (
            capo_elasticsearch_service.types.describe_packages_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
