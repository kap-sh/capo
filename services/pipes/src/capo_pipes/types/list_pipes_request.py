"""Generated from Smithy shape ``com.amazonaws.pipes#ListPipesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.limit_max100
    import capo_pipes.types.next_token
    import capo_pipes.types.pipe_name
    import capo_pipes.types.pipe_state
    import capo_pipes.types.requested_pipe_state
    import capo_pipes.types.resource_arn


class ListPipesRequest(TypedDict, closed=True):
    name_prefix: NotRequired["capo_pipes.types.pipe_name.PipeName"]
    """<p>A value that will return a subset of the pipes associated with this account. For example, <code>"NamePrefix": "ABC"</code> will return all endpoints with "ABC" in the name.</p>"""
    desired_state: NotRequired[
        "capo_pipes.types.requested_pipe_state.RequestedPipeState"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["capo_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    source_prefix: NotRequired["capo_pipes.types.resource_arn.ResourceArn"]
    """<p>The prefix matching the pipe source.</p>"""
    target_prefix: NotRequired["capo_pipes.types.resource_arn.ResourceArn"]
    """<p>The prefix matching the pipe target.</p>"""
    next_token: NotRequired["capo_pipes.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""
    limit: NotRequired["capo_pipes.types.limit_max100.LimitMax100"]
    """<p>The maximum number of pipes to include in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPipesRequest:
    out: ListPipesRequest = {}  # type: ignore[typeddict-item]
    return out
