"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListPipelineExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.list_pipeline_executions_request_max_results_integer
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.pipeline_execution_state
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.workspace_name


class ListPipelineExecutionsRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.list_pipeline_executions_request_max_results_integer.ListPipelineExecutionsRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return per request. This is an upper bound; the actual number of results may be less. Default: 50.</p>"""
    state: NotRequired[
        "capo_iotsitewise.types.pipeline_execution_state.PipelineExecutionState"
    ]
    """<p>Filter by execution state. If not specified, executions in all states are returned.</p>"""
    start_time_after: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>Inclusive lower bound on execution start time (ISO-8601). Only executions with startTime &gt;= startTimeAfter are returned. Cannot be combined with endTimeAfter or endTimeBefore.</p>"""
    start_time_before: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>Exclusive upper bound on execution start time (ISO-8601). Only executions with startTime &lt; startTimeBefore are returned. Cannot be combined with endTimeAfter or endTimeBefore.</p>"""
    end_time_after: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>Inclusive lower bound on execution end time (ISO-8601). Only executions with endTime &gt;= endTimeAfter are returned. Cannot be combined with startTimeAfter or startTimeBefore. Only matches executions in terminal states.</p>"""
    end_time_before: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>Exclusive upper bound on execution end time (ISO-8601). Only executions with endTime &lt; endTimeBefore are returned. Cannot be combined with startTimeAfter or startTimeBefore. Only matches executions in terminal states.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPipelineExecutionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPipelineExecutionsRequest:
    out: ListPipelineExecutionsRequest = {}  # type: ignore[typeddict-item]
    return out
