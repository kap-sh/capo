"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateDiscoveredResourceCountsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.group_by_api_limit
    import capo_config_service.types.next_token
    import capo_config_service.types.resource_count_filters
    import capo_config_service.types.resource_count_group_key


class GetAggregateDiscoveredResourceCountsRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    filters: NotRequired[
        "capo_config_service.types.resource_count_filters.ResourceCountFilters"
    ]
    """<p>Filters the results based on the <code>ResourceCountFilters</code> object.</p>"""
    group_by_key: NotRequired[
        "capo_config_service.types.resource_count_group_key.ResourceCountGroupKey"
    ]
    """<p>The key to group the resource counts.</p>"""
    limit: NotRequired["capo_config_service.types.group_by_api_limit.GroupByAPILimit"]
    """<p>The maximum number of <a>GroupedResourceCount</a> objects returned on each page. The default is 1000. You cannot specify a number greater than 1000. If you specify 0, Config uses the default.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAggregateDiscoveredResourceCountsRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "filters" in value:
        import capo_config_service.types.resource_count_filters

        out["Filters"] = (
            capo_config_service.types.resource_count_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "group_by_key" in value:
        import capo_config_service.types.resource_count_group_key

        out["GroupByKey"] = (
            capo_config_service.types.resource_count_group_key.serialize_aws_json_1_1(
                value["group_by_key"]
            )
        )
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAggregateDiscoveredResourceCountsRequest:
    out: GetAggregateDiscoveredResourceCountsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "GetAggregateDiscoveredResourceCountsRequest.configuration_aggregator_name required"
        )
    if data.get("Filters") is not None:
        import capo_config_service.types.resource_count_filters

        out["filters"] = (
            capo_config_service.types.resource_count_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if data.get("GroupByKey") is not None:
        import capo_config_service.types.resource_count_group_key

        out["group_by_key"] = (
            capo_config_service.types.resource_count_group_key.deserialize_aws_json_1_1(
                data["GroupByKey"]
            )
        )
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
