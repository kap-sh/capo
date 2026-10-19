"""Generated from Smithy shape ``com.amazonaws.swf#DescribeWorkflowTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_swf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_swf.types.domain_name
    import capo_swf.types.workflow_type


class DescribeWorkflowTypeInput(TypedDict, closed=True):
    domain: "capo_swf.types.domain_name.DomainName"
    """<p>The name of the domain in which this workflow type is registered.</p>"""
    workflow_type: "capo_swf.types.workflow_type.WorkflowType"
    """<p>The workflow type to describe.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeWorkflowTypeInput) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    import capo_swf.types.workflow_type

    out["workflowType"] = capo_swf.types.workflow_type.serialize_aws_json_1_0(
        value["workflow_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeWorkflowTypeInput:
    out: DescribeWorkflowTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("workflowType") is not None:
        import capo_swf.types.workflow_type

        out["workflow_type"] = capo_swf.types.workflow_type.deserialize_aws_json_1_0(
            data["workflowType"]
        )
    else:
        raise DeserializationError("DescribeWorkflowTypeInput.workflow_type required")
    return out
