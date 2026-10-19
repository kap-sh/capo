"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentGoalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token


class ListAgentGoalsRequest(TypedDict, closed=True):
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the optimization profile to list goals for.</p>"""
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    """<p>The maximum number of goals to return in a single response.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to continue retrieving results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentGoalsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentGoalsRequest:
    out: ListAgentGoalsRequest = {}  # type: ignore[typeddict-item]
    return out
