"""Generated from Smithy shape ``com.amazonaws.swf#CountOpenWorkflowExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.execution_time_filter
    import capo_swf.types.tag_filter
    import capo_swf.types.workflow_execution_filter
    import capo_swf.types.workflow_type_filter


class CountOpenWorkflowExecutionsInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow executions to count.</p>"""
    start_time_filter: "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
    """<p>Specifies the start time criteria that workflow executions must meet in order to be counted.</p>"""
    type_filter: NotRequired["capo_swf.types.workflow_type_filter.WorkflowTypeFilter"]
    """<p>Specifies the type of the workflow executions to be counted.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    tag_filter: NotRequired["capo_swf.types.tag_filter.TagFilter"]
    """<p>If specified, only executions that have a tag that matches the filter are counted.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    execution_filter: NotRequired[
        "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
    ]
    """<p>If specified, only workflow executions matching the <code>WorkflowId</code> in the filter are counted.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountOpenWorkflowExecutionsInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.execution_time_filter

    out["startTimeFilter"] = (
        capo_swf.types.execution_time_filter.serialize_aws_json_1_0(
            value["start_time_filter"]
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
    if "execution_filter" in value:
        import capo_swf.types.workflow_execution_filter

        out["executionFilter"] = (
            capo_swf.types.workflow_execution_filter.serialize_aws_json_1_0(
                value["execution_filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountOpenWorkflowExecutionsInput:
    out: CountOpenWorkflowExecutionsInput = {}  # type: ignore[typeddict-item]
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
    else:
        raise DeserializationError(
            "CountOpenWorkflowExecutionsInput.start_time_filter required"
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
    if data.get("executionFilter") is not None:
        import capo_swf.types.workflow_execution_filter

        out["execution_filter"] = (
            capo_swf.types.workflow_execution_filter.deserialize_aws_json_1_0(
                data["executionFilter"]
            )
        )
    return out
