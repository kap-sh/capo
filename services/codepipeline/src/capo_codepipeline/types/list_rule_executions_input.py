"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListRuleExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.max_results
    import capo_codepipeline.types.next_token
    import capo_codepipeline.types.pipeline_name
    import capo_codepipeline.types.rule_execution_filter


class ListRuleExecutionsInput(TypedDict, closed=True):
    pipeline_name: "capo_codepipeline.types.pipeline_name.PipelineName"
    """<p>The name of the pipeline for which you want to get execution summary information.</p>"""
    filter: NotRequired[
        "capo_codepipeline.types.rule_execution_filter.RuleExecutionFilter"
    ]
    """<p>Input information used to filter rule execution history.</p>"""
    max_results: NotRequired["capo_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned nextToken value. Pipeline history is limited to the most recent 12 months, based on pipeline execution start times. Default value is 100.</p>"""
    next_token: NotRequired["capo_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous <code>ListRuleExecutions</code> call, which can be used to return the next set of rule executions in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleExecutionsInput) -> dict:
    out: dict = {}
    out["pipelineName"] = value["pipeline_name"]
    if "filter" in value:
        import capo_codepipeline.types.rule_execution_filter

        out["filter"] = (
            capo_codepipeline.types.rule_execution_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleExecutionsInput:
    out: ListRuleExecutionsInput = {}  # type: ignore[typeddict-item]
    if data.get("pipelineName") is not None:
        out["pipeline_name"] = data["pipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("filter") is not None:
        import capo_codepipeline.types.rule_execution_filter

        out["filter"] = (
            capo_codepipeline.types.rule_execution_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
