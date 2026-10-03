"""Generated from Smithy shape ``com.amazonaws.sfn#ListExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.execution_redrive_filter
    import capo_sfn.types.execution_status
    import capo_sfn.types.list_executions_page_token
    import capo_sfn.types.long_arn
    import capo_sfn.types.page_size


class ListExecutionsInput(TypedDict, closed=True):
    state_machine_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the state machine whose executions is listed.</p> <p>You can specify either a <code>mapRunArn</code> or a <code>stateMachineArn</code>, but not both.</p> <p>You can also return a list of executions associated with a specific <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html">alias</a> or <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html">version</a>, by specifying an alias ARN or a version ARN in the <code>stateMachineArn</code> parameter.</p>"""
    status_filter: NotRequired["capo_sfn.types.execution_status.ExecutionStatus"]
    """<p>If specified, only list the executions whose current execution status matches the given filter.</p> <p>If you provide a <code>PENDING_REDRIVE</code> statusFilter, you must specify <code>mapRunArn</code>. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/redrive-map-run.html#redrive-child-workflow-behavior">Child workflow execution redrive behaviour</a> in the <i>Step Functions Developer Guide</i>. </p> <p>If you provide a stateMachineArn and a <code>PENDING_REDRIVE</code> statusFilter, the API returns a validation exception.</p>"""
    max_results: "capo_sfn.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>"""
    next_token: NotRequired[
        "capo_sfn.types.list_executions_page_token.ListExecutionsPageToken"
    ]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    map_run_arn: NotRequired["capo_sfn.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of the Map Run that started the child workflow executions. If the <code>mapRunArn</code> field is specified, a list of all of the child workflow executions started by a Map Run is returned. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html">Examining Map Run</a> in the <i>Step Functions Developer Guide</i>.</p> <p>You can specify either a <code>mapRunArn</code> or a <code>stateMachineArn</code>, but not both.</p>"""
    redrive_filter: NotRequired[
        "capo_sfn.types.execution_redrive_filter.ExecutionRedriveFilter"
    ]
    """<p>Sets a filter to list executions based on whether or not they have been redriven.</p> <p>For a Distributed Map, <code>redriveFilter</code> sets a filter to list child workflow executions based on whether or not they have been redriven.</p> <p>If you do not provide a <code>redriveFilter</code>, Step Functions returns a list of both redriven and non-redriven executions.</p> <p>If you provide a state machine ARN in <code>redriveFilter</code>, the API returns a validation exception.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListExecutionsInput) -> dict:
    out: dict = {}
    if "state_machine_arn" in value:
        out["stateMachineArn"] = value["state_machine_arn"]
    if "status_filter" in value:
        import capo_sfn.types.execution_status

        out["statusFilter"] = capo_sfn.types.execution_status.serialize_aws_json_1_0(
            value["status_filter"]
        )
    out["maxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "map_run_arn" in value:
        out["mapRunArn"] = value["map_run_arn"]
    if "redrive_filter" in value:
        import capo_sfn.types.execution_redrive_filter

        out["redriveFilter"] = (
            capo_sfn.types.execution_redrive_filter.serialize_aws_json_1_0(
                value["redrive_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListExecutionsInput:
    out: ListExecutionsInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    if data.get("statusFilter") is not None:
        import capo_sfn.types.execution_status

        out["status_filter"] = capo_sfn.types.execution_status.deserialize_aws_json_1_0(
            data["statusFilter"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    if data.get("redriveFilter") is not None:
        import capo_sfn.types.execution_redrive_filter

        out["redrive_filter"] = (
            capo_sfn.types.execution_redrive_filter.deserialize_aws_json_1_0(
                data["redriveFilter"]
            )
        )
    return out
