"""Generated from Smithy shape ``com.amazonaws.swf#DescribeWorkflowExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.workflow_execution


class DescribeWorkflowExecutionInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain containing the workflow execution.</p>"""
    execution: "capo_swf.types.workflow_execution.WorkflowExecution"
    """<p>The workflow execution to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeWorkflowExecutionInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.workflow_execution

    out["execution"] = capo_swf.types.workflow_execution.serialize_aws_json_1_0(
        value["execution"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeWorkflowExecutionInput:
    out: DescribeWorkflowExecutionInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("execution") is not None:
        import capo_swf.types.workflow_execution

        out["execution"] = capo_swf.types.workflow_execution.deserialize_aws_json_1_0(
            data["execution"]
        )
    else:
        raise DeserializationError("DescribeWorkflowExecutionInput.execution required")
    return out
