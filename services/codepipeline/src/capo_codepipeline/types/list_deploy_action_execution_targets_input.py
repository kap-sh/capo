"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListDeployActionExecutionTargetsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.action_execution_id
    import capo_codepipeline.types.max_results
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.target_filter_list


class ListDeployActionExecutionTargetsInput(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_codepipeline.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline with the deploy action.</p>"""
    action_execution_id: "capo_codepipeline.types.action_execution_id.ActionExecutionId"
    """<p>The execution ID for the deploy action.</p>"""
    filters: NotRequired["capo_codepipeline.types.target_filter_list.TargetFilterList"]
    """<p>Filters the targets for a specified deploy action.</p>"""
    max_results: NotRequired["capo_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>An identifier that was returned from the previous list action types call, which can be used to return the next set of action types in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDeployActionExecutionTargetsInput) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["pipelineName"] = value["pipeline_name"]
    out["actionExecutionId"] = value["action_execution_id"]
    if "filters" in value:
        import capo_codepipeline.types.target_filter_list

        out["filters"] = (
            capo_codepipeline.types.target_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDeployActionExecutionTargetsInput:
    out: ListDeployActionExecutionTargetsInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    if data.get("actionExecutionId") is not None:
        out["action_execution_id"] = data["actionExecutionId"]
    else:
        out["action_execution_id"] = ""
    if data.get("filters") is not None:
        import capo_codepipeline.types.target_filter_list

        out["filters"] = (
            capo_codepipeline.types.target_filter_list.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
