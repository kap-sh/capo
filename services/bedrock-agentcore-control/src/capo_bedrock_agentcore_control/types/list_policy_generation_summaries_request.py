"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyGenerationSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.resource_id


class ListPolicyGenerationSummariesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationSummaries.html">ListPolicyGenerationSummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of policy generation summaries to return in a single response.</p>"""
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine whose policy generation summaries to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationSummariesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationSummariesRequest:
    out: ListPolicyGenerationSummariesRequest = {}  # type: ignore[typeddict-item]
    return out
