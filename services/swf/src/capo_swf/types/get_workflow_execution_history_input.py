"""Generated from Smithy shape ``com.amazonaws.swf#GetWorkflowExecutionHistoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.page_size
    import capo_swf.types.page_token
    import capo_swf.types.reverse_order
    import capo_swf.types.workflow_execution


class GetWorkflowExecutionHistoryInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution.</p>"""
    execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>Specifies the workflow execution for which to return the history.</p>"""
    next_page_token: NotRequired["capo_swf.types.page_token.PageToken"]
    """<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>"""
    maximum_page_size: "capo_swf.types.page_size.PageSize"
    """<p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>"""
    reverse_order: "capo_swf.types.reverse_order.ReverseOrder"
    """<p>When set to <code>true</code>, returns the events in reverse order. By default the results are returned in ascending order of the <code>eventTimeStamp</code> of the events.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowExecutionHistoryInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.workflow_execution

    out["execution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["execution"]
    )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    out["maximumPageSize"] = value.get("maximum_page_size", 0)
    out["reverseOrder"] = value.get("reverse_order", False)
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowExecutionHistoryInput:
    out: GetWorkflowExecutionHistoryInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("GetWorkflowExecutionHistoryInput.domain required")
    if data.get("execution") is not None:
        import capo_swf.types.workflow_execution

        out["execution"] = capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
            data["execution"]
        )
    else:
        raise DeserializationError(
            "GetWorkflowExecutionHistoryInput.execution required"
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
