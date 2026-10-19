"""Generated from Smithy shape ``com.amazonaws.swf#CountClosedWorkflowExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_swf.types.close_status_filter
    import capo_swf.types.domain_name
    import capo_swf.types.execution_time_filter
    import capo_swf.types.tag_filter
    import capo_swf.types.workflow_execution_filter
    import capo_swf.types.workflow_type_filter


class CountClosedWorkflowExecutionsInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow executions to count.</p>"""
    start_time_filter: NotRequired[
        "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
    ]
    """<p>If specified, only workflow executions that meet the start time criteria of the filter are counted.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>"""
    close_time_filter: NotRequired[
        "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
    ]
    """<p>If specified, only workflow executions that meet the close time criteria of the filter are counted.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>"""
    execution_filter: NotRequired[
        "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
    ]
    """<p>If specified, only workflow executions matching the <code>WorkflowId</code> in the filter are counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    type_filter: NotRequired["capo_swf.types.workflow_type_filter.WorkflowTypeFilter"]
    """<p>If specified, indicates the type of the workflow executions to be counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    tag_filter: NotRequired["capo_swf.types.tag_filter.TagFilter"]
    """<p>If specified, only executions that have a tag that matches the filter are counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    close_status_filter: NotRequired[
        "capo_swf.types.close_status_filter.CloseStatusFilter"
    ]
    """<p>If specified, only workflow executions that match this close status are counted. This filter has an affect only if <code>executionStatus</code> is specified as <code>CLOSED</code>.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountClosedWorkflowExecutionsInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    if "start_time_filter" in value:
        import capo_swf.types.execution_time_filter

        out["startTimeFilter"] = (
            capo_swf.types.execution_time_filter.serialize_aws_json_1_0(
                value["start_time_filter"]
            )
        )
    if "close_time_filter" in value:
        import capo_swf.types.execution_time_filter

        out["closeTimeFilter"] = (
            capo_swf.types.execution_time_filter.serialize_aws_json_1_0(
                value["close_time_filter"]
            )
        )
    if "execution_filter" in value:
        import capo_swf.types.workflow_execution_filter

        out["executionFilter"] = (
            capo_swf.types.workflow_execution_filter.serialize_aws_json_1_0(
                value["execution_filter"]
            )
        )
    if "type_filter" in value:
        import capo_swf.types.workflow_type_filter

        out["typeFilter"] = capo_swf.types.workflow_type_filter.serialize_aws_json_1_0(
            value["type_filter"]
        )
    if "tag_filter" in value:
        import capo_swf.types.tag_filter

        out["tagFilter"] = capo_swf.types.tag_filter.serialize_aws_json_1_0(
            value["tag_filter"]
        )
    if "close_status_filter" in value:
        import capo_swf.types.close_status_filter

        out["closeStatusFilter"] = (
            capo_swf.types.close_status_filter.serialize_aws_json_1_0(
                value["close_status_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountClosedWorkflowExecutionsInput:
    out: CountClosedWorkflowExecutionsInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("startTimeFilter") is not None:
        import capo_swf.types.execution_time_filter

        out["start_time_filter"] = (
            capo_swf.types.execution_time_filter.deserialize_aws_json_1_0(
                data["startTimeFilter"]
            )
        )
    if data.get("closeTimeFilter") is not None:
        import capo_swf.types.execution_time_filter

        out["close_time_filter"] = (
            capo_swf.types.execution_time_filter.deserialize_aws_json_1_0(
                data["closeTimeFilter"]
            )
        )
    if data.get("executionFilter") is not None:
        import capo_swf.types.workflow_execution_filter

        out["execution_filter"] = (
            capo_swf.types.workflow_execution_filter.deserialize_aws_json_1_0(
                data["executionFilter"]
            )
        )
    if data.get("typeFilter") is not None:
        import capo_swf.types.workflow_type_filter

        out["type_filter"] = (
            capo_swf.types.workflow_type_filter.deserialize_aws_json_1_0(
                data["typeFilter"]
            )
        )
    if data.get("tagFilter") is not None:
        import capo_swf.types.tag_filter

        out["tag_filter"] = capo_swf.types.tag_filter.deserialize_aws_json_1_0(
            data["tagFilter"]
        )
    if data.get("closeStatusFilter") is not None:
        import capo_swf.types.close_status_filter

        out["close_status_filter"] = (
            capo_swf.types.close_status_filter.deserialize_aws_json_1_0(
                data["closeStatusFilter"]
            )
        )
    return out
