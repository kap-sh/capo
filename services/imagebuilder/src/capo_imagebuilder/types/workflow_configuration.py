"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.on_workflow_failure
    import capo_imagebuilder.types.parallel_group
    import capo_imagebuilder.types.workflow_parameter_list
    import capo_imagebuilder.types.workflow_version_arn_or_build_version_arn


class WorkflowConfiguration(TypedDict, closed=True):
    workflow_arn: "capo_imagebuilder.types.workflow_version_arn_or_build_version_arn.WorkflowVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the workflow resource.</p>"""
    parameters: NotRequired[
        "capo_imagebuilder.types.workflow_parameter_list.WorkflowParameterList"
    ]
    """<p>Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.</p>"""
    parallel_group: NotRequired["capo_imagebuilder.types.parallel_group.ParallelGroup"]
    """<p>Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.</p>"""
    on_failure: NotRequired[
        "capo_imagebuilder.types.on_workflow_failure.OnWorkflowFailure"
    ]
    """<p>The action to take if the workflow fails. With <code>CONTINUE</code>, a failed workflow is logged and image creation proceeds to the next workflow. If you don't set a value, the image build fails when the workflow fails. You can only set this property for test workflows.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowConfiguration) -> dict:
    out: dict = {}
    out["workflowArn"] = value["workflow_arn"]
    if "parameters" in value:
        import capo_imagebuilder.types.workflow_parameter_list

        out["parameters"] = (
            capo_imagebuilder.types.workflow_parameter_list.serialize_json(
                value["parameters"]
            )
        )
    if "parallel_group" in value:
        out["parallelGroup"] = value["parallel_group"]
    if "on_failure" in value:
        import capo_imagebuilder.types.on_workflow_failure

        out["onFailure"] = capo_imagebuilder.types.on_workflow_failure.serialize_json(
            value["on_failure"]
        )
    return out


def deserialize_json(data: dict) -> WorkflowConfiguration:
    out: WorkflowConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("workflowArn") is not None:
        out["workflow_arn"] = data["workflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("parameters") is not None:
        import capo_imagebuilder.types.workflow_parameter_list

        out["parameters"] = (
            capo_imagebuilder.types.workflow_parameter_list.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("parallelGroup") is not None:
        out["parallel_group"] = data["parallelGroup"]
    if data.get("onFailure") is not None:
        import capo_imagebuilder.types.on_workflow_failure

        out["on_failure"] = (
            capo_imagebuilder.types.on_workflow_failure.deserialize_json(
                data["onFailure"]
            )
        )
    return out
