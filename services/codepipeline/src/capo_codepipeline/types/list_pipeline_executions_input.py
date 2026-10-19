"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListPipelineExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.max_results
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.pipeline_execution_filter
    import capo_codepipeline.types.pipeline_name


class ListPipelineExecutionsInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which you want to get execution summary information.</p>"""
    max_results: NotRequired["capo_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.</p>"""
    filter: NotRequired[
        "capo_codepipeline.types.pipeline_execution_filter.PipelineExecutionFilter"
    ]
    """<p>The pipeline execution to filter on.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListPipelineExecutions</code> call, which can be used to return the next set of pipeline executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPipelineExecutionsInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_codepipeline.types.pipeline_execution_filter

        out["filter"] = (
            capo_codepipeline.types.pipeline_execution_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPipelineExecutionsInput:
    out: ListPipelineExecutionsInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_codepipeline.types.pipeline_execution_filter

        out["filter"] = (
            capo_codepipeline.types.pipeline_execution_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
