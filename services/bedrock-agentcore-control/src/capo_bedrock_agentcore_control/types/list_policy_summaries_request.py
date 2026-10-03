"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicySummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.resource_id


class ListPolicySummariesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicySummaries.html">ListPolicySummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of policy summaries to return in a single response.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine whose policy summaries to retrieve.</p>"""
    target_resource_scope: NotRequired[
        "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    ]
    """<p>Optional filter to list policy summaries that apply to a specific resource scope or resource type. This helps narrow down results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicySummariesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicySummariesRequest:
    out: ListPolicySummariesRequest = {}  # type: ignore[typeddict-item]
    return out
