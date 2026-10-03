"""Generated from Smithy shape ``com.amazonaws.swf#ListClosedWorkflowExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.close_status_filter
    import capo_swf.types.domain_name
    import capo_swf.types.execution_time_filter
    import capo_swf.types.page_size
    import capo_swf.types.page_token
    import capo_swf.types.reverse_order
    import capo_swf.types.tag_filter
    import capo_swf.types.workflow_execution_filter
    import capo_swf.types.workflow_type_filter


class ListClosedWorkflowExecutionsInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain that contains the workflow executions to list.</p>"""
    start_time_filter: NotRequired[
        "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
    ]
    """<p>If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>"""
    close_time_filter: NotRequired[
        "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
    ]
    """<p>If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>"""
    execution_filter: NotRequired[
        "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
    ]
    """<p>If specified, only workflow executions matching the workflow ID specified in the filter are returned.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    close_status_filter: NotRequired[
        "capo_swf.types.close_status_filter.CloseStatusFilter"
    ]
    """<p>If specified, only workflow executions that match this <i>close status</i> are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    type_filter: NotRequired["capo_swf.types.workflow_type_filter.WorkflowTypeFilter"]
    """<p>If specified, only executions of the type specified in the filter are returned.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    tag_filter: NotRequired["capo_swf.types.tag_filter.TagFilter"]
    """<p>If specified, only executions that have the matching tag are listed.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>"""
    next_page_token: NotRequired["capo_swf.types.page_token.PageToken"]
    """<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    maximum_page_size: "capo_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: "capo_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListClosedWorkflowExecutionsInput) -> dict:
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
    if "close_status_filter" in value:
        import capo_swf.types.close_status_filter

        out["closeStatusFilter"] = (
            capo_swf.types.close_status_filter.serialize_aws_json_1_0(
                value["close_status_filter"]
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
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> ListClosedWorkflowExecutionsInput:
    out: ListClosedWorkflowExecutionsInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("ListClosedWorkflowExecutionsInput.domain required")
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
    if data.get("closeStatusFilter") is not None:
        import capo_swf.types.close_status_filter

        out["close_status_filter"] = (
            capo_swf.types.close_status_filter.deserialize_aws_json_1_0(
                data["closeStatusFilter"]
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
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    if data.get("maximumPageSize") is not None:
        out["maximum_page_size"] = data["maximumPageSize"]
    else:
        out["maximum_page_size"] = 0
    if data.get("reverseOrder") is not None:
        out["reverse_order"] = data["reverseOrder"]
    else:
        out["reverse_order"] = False
    return out
