"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentContextsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token


class ListAgentContextsRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile to list contexts for.</p>"""
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentContextsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentContextsRequest:
    out: ListAgentContextsRequest = {}  # type: ignore[typeddict-item]
    return out
