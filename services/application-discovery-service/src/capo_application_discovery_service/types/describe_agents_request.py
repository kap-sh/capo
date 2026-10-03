"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeAgentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_ids
    import capo_application_discovery_service.types.filters
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.next_token


class DescribeAgentsRequest(TypedDict, closed=True):
    agent_ids: NotRequired[
        "capo_application_discovery_service.types.agent_ids.AgentIds"
    ]
    """<p>The agent or the collector IDs for which you want information. If you specify no IDs, the system returns information about all agents/collectors associated with your user.</p>"""
    filters: NotRequired["capo_application_discovery_service.types.filters.Filters"]
    """<p>You can filter the request using various logical operators and a <i>key</i>-<i>value</i> format. For example: </p> <p> <code>{"key": "collectionStatus", "value": "STARTED"}</code> </p>"""
    max_results: "capo_application_discovery_service.types.integer.Integer"
    """<p>The total number of agents/collectors to return in a single page of output. The maximum value is 100.</p>"""
    next_token: NotRequired[
        "capo_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>Token to retrieve the next set of results. For example, if you previously specified 100 IDs for <code>DescribeAgentsRequest$agentIds</code> but set <code>DescribeAgentsRequest$maxResults</code> to 10, you received a set of 10 results along with a token. Use that token in this query to get the next set of 10.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAgentsRequest) -> dict:
    out: dict = {}
    if "agent_ids" in value:
        import capo_application_discovery_service.types.agent_ids

        out["agentIds"] = (
            capo_application_discovery_service.types.agent_ids.serialize_aws_json_1_1(
                value["agent_ids"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAgentsRequest:
    out: DescribeAgentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("agentIds") is not None:
        import capo_application_discovery_service.types.agent_ids

        out["agent_ids"] = (
            capo_application_discovery_service.types.agent_ids.deserialize_aws_json_1_1(
                data["agentIds"]
            )
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
    return out
