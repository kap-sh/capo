"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.next_token
    import capo_application_discovery_service.types.tag_filters


class DescribeTagsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_application_discovery_service.types.tag_filters.TagFilters"
    ]
    """<p>You can filter the list using a <i>key</i>-<i>value</i> format. You can separate these items by using logical operators. Allowed filters include <code>tagKey</code>, <code>tagValue</code>, and <code>configurationId</code>. </p>"""
    max_results: NotRequired["capo_application_discovery_service.types.integer.Integer"]
    """<p>The total number of items to return in a single page of output. The maximum value is 100.</p>"""
    next_token: NotRequired[
        "capo_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_application_discovery_service.types.tag_filters

        out["filters"] = (
            capo_application_discovery_service.types.tag_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsRequest:
    out: DescribeTagsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_application_discovery_service.types.tag_filters

        out["filters"] = (
            capo_application_discovery_service.types.tag_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
