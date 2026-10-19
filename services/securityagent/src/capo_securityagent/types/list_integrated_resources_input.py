"""Generated from Smithy shape ``com.amazonaws.securityagent#ListIntegratedResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.integration_id
    import capo_securityagent.types.max_results
    import capo_securityagent.types.next_token
    import capo_securityagent.types.resource_type


class ListIntegratedResourcesInput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to list integrated resources for.</p>"""
    integration_id: NotRequired["capo_securityagent.types.integration_id.IntegrationId"]
    """<p>The unique identifier of the integration to filter by.</p>"""
    resource_type: NotRequired["capo_securityagent.types.resource_type.ResourceType"]
    """<p>The type of resource to filter by.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""
    max_results: NotRequired["capo_securityagent.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegratedResourcesInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    if "integration_id" in value:
        out["integrationId"] = value["integration_id"]
    if "resource_type" in value:
        import capo_securityagent.types.resource_type

        out["resourceType"] = capo_securityagent.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListIntegratedResourcesInput:
    out: ListIntegratedResourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    if data.get("resourceType") is not None:
        import capo_securityagent.types.resource_type

        out["resource_type"] = capo_securityagent.types.resource_type.deserialize_json(
            data["resourceType"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
