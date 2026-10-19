"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetWorkflowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.nullable_boolean
    import capo_glue.types.workflow_names


class BatchGetWorkflowsRequest(TypedDict, closed=True):
    names: "capo_glue.types.workflow_names.WorkflowNames"
    """<p>A list of workflow names, which may be the names returned from the <code>ListWorkflows</code> operation.</p>"""
    include_graph: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to include a graph when returning the workflow resource metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetWorkflowsRequest) -> dict:
    out: dict = {}
    import capo_glue.types.workflow_names

    out["Names"] = capo_glue.types.workflow_names.serialize_aws_json_1_1(value["names"])
    if "include_graph" in value:
        out["IncludeGraph"] = value["include_graph"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetWorkflowsRequest:
    out: BatchGetWorkflowsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_glue.types.workflow_names

        out["names"] = capo_glue.types.workflow_names.deserialize_aws_json_1_1(
            data["Names"]
        )
    else:
        out["names"] = []
    if data.get("IncludeGraph") is not None:
        out["include_graph"] = data["IncludeGraph"]
    return out
