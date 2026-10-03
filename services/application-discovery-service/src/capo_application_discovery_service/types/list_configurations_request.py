"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ListConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_discovery_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_application_discovery_service.types.configuration_item_type
    import capo_application_discovery_service.types.filters
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.next_token
    import capo_application_discovery_service.types.order_by_list


class ListConfigurationsRequest(TypedDict, closed=True):
    configuration_type: "capo_application_discovery_service.types.configuration_item_type.ConfigurationItemType"
    """<p>A valid configuration identified by Application Discovery Service. </p>"""
    filters: NotRequired["capo_application_discovery_service.types.filters.Filters"]
    """<p>You can filter the request using various logical operators and a <i>key</i>-<i>value</i> format. For example: </p> <p> <code>{"key": "serverType", "value": "webServer"}</code> </p> <p>For a complete list of filter options and guidance about using them with this action, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations">Using the ListConfigurations Action</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p>"""
    max_results: "capo_application_discovery_service.types.integer.Integer"
    """<p>The total number of items to return. The maximum value is 100.</p>"""
    next_token: NotRequired[
        "capo_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>Token to retrieve the next set of results. For example, if a previous call to ListConfigurations returned 100 items, but you set <code>ListConfigurationsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>"""
    order_by: NotRequired[
        "capo_application_discovery_service.types.order_by_list.OrderByList"
    ]
    """<p>Certain filter criteria return output that can be sorted in ascending or descending order. For a list of output characteristics for each filter, see <a href="https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-api-queries.html#ListConfigurations">Using the ListConfigurations Action</a> in the <i>Amazon Web Services Application Discovery Service User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_application_discovery_service.types.configuration_item_type

    out["configurationType"] = (
        capo_application_discovery_service.types.configuration_item_type.serialize_aws_json_1_1(
            value["configuration_type"]
        )
    )
    if "filters" in value:
        import capo_application_discovery_service.types.filters

        out["filters"] = (
            capo_application_discovery_service.types.filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["maxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "order_by" in value:
        import capo_application_discovery_service.types.order_by_list

        out["orderBy"] = (
            capo_application_discovery_service.types.order_by_list.serialize_aws_json_1_1(
                value["order_by"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListConfigurationsRequest:
    out: ListConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("configurationType") is not None:
        import capo_application_discovery_service.types.configuration_item_type

        out["configuration_type"] = (
            capo_application_discovery_service.types.configuration_item_type.deserialize_aws_json_1_1(
                data["configurationType"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfigurationsRequest.configuration_type required"
        )
    if data.get("filters") is not None:
        import capo_application_discovery_service.types.filters

        out["filters"] = (
            capo_application_discovery_service.types.filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("orderBy") is not None:
        import capo_application_discovery_service.types.order_by_list

        out["order_by"] = (
            capo_application_discovery_service.types.order_by_list.deserialize_aws_json_1_1(
                data["orderBy"]
            )
        )
    return out
