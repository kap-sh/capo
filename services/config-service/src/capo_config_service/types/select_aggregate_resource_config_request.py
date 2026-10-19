"""Generated from Smithy shape ``com.amazonaws.configservice#SelectAggregateResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.expression
    import capo_config_service.types.limit
    import capo_config_service.types.next_token


class SelectAggregateResourceConfigRequest(TypedDict, closed=True):
    expression: "capo_config_service.types.expression.Expression"
    """<p>The SQL query SELECT command. </p>"""
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of query results returned on each page. </p>"""
    max_results: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of query results returned on each page. Config also allows the Limit request parameter.</p>"""
    next_token: NotRequired["capo_config_service.types.next_token.NextToken"]
    """<p>The nextToken string returned in a previous request that you use to request the next page of results in a paginated response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SelectAggregateResourceConfigRequest) -> dict:
    out: dict = {}
    out["Expression"] = value["expression"]
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SelectAggregateResourceConfigRequest:
    out: SelectAggregateResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    else:
        out["expression"] = ""
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        out["configuration_aggregator_name"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
