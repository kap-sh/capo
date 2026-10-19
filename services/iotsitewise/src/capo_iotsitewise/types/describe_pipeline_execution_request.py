"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribePipelineExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.describe_pipeline_execution_request_max_results_integer
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.workspace_name


class DescribePipelineExecutionRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>The name of the pipeline.</p>"""
    pipeline_execution_id: "capo_iotsitewise.types.id.ID"
    """<p>The unique identifier of the pipeline execution.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.describe_pipeline_execution_request_max_results_integer.DescribePipelineExecutionRequestMaxResultsInteger"
    ]
    """<p>The maximum number of compute nodes to return per request. This is an upper bound; the actual number of results may be less. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipelineExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePipelineExecutionRequest:
    out: DescribePipelineExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
