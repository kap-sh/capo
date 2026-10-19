"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ListInvocationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.max_results
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.session_identifier


class ListInvocationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock_agent_runtime.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results. </p>"""
    max_results: NotRequired["capo_bedrock_agent_runtime.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>"""
    session_identifier: (
        "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the session to list invocations for. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvocationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListInvocationsRequest:
    out: ListInvocationsRequest = {}  # type: ignore[typeddict-item]
    return out
