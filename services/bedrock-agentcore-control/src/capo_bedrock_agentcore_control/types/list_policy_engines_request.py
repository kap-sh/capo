"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListPolicyEnginesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.next_token


class ListPolicyEnginesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngines.html">ListPolicyEngines</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>"""
    max_results: NotRequired[
        "capo_bedrock_agentcore_control.types.max_results.MaxResults"
    ]
    """<p>The maximum number of policy engines to return in a single response. If not specified, the default is 10 policy engines per page, with a maximum of 100 per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyEnginesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyEnginesRequest:
    out: ListPolicyEnginesRequest = {}  # type: ignore[typeddict-item]
    return out
