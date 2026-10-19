"""Generated from Smithy shape ``com.amazonaws.entityresolution#CreateMatchingWorkflowOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.incremental_run_config
    import capo_entityresolution.types.input_source_config
    import capo_entityresolution.types.matching_workflow_arn
    import capo_entityresolution.types.output_source_config
    import capo_entityresolution.types.resolution_techniques


class CreateMatchingWorkflowOutput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    workflow_arn: (
        "capo_entityresolution.types.matching_workflow_arn.MatchingWorkflowArn"
    )
    """<p>The ARN (Amazon Resource Name) that Entity Resolution generated for the <code>MatchingWorkflow</code>.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>A description of the workflow.</p>"""
    input_source_config: (
        "capo_entityresolution.types.input_source_config.InputSourceConfig"
    )
    """<p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>"""
    output_source_config: (
        "capo_entityresolution.types.output_source_config.OutputSourceConfig"
    )
    """<p>A list of <code>OutputSource</code> objects, each of which contains fields <code>outputS3Path</code>, <code>applyNormalization</code>, <code>KMSArn</code>, and <code>output</code>.</p>"""
    resolution_techniques: (
        "capo_entityresolution.types.resolution_techniques.ResolutionTechniques"
    )
    """<p>An object which defines the <code>resolutionType</code> and the <code>ruleBasedProperties</code>.</p>"""
    incremental_run_config: NotRequired[
        "capo_entityresolution.types.incremental_run_config.IncrementalRunConfig"
    ]
    """<p>An object which defines an incremental run type and has only <code>incrementalRunType</code> as a field.</p>"""
    role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMatchingWorkflowOutput) -> dict:
    out: dict = {}
    out["workflowName"] = value["workflow_name"]
    out["workflowArn"] = value["workflow_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_entityresolution.types.input_source_config

    out["inputSourceConfig"] = (
        capo_entityresolution.types.input_source_config.serialize_json(
            value["input_source_config"]
        )
    )
    import capo_entityresolution.types.output_source_config

    out["outputSourceConfig"] = (
        capo_entityresolution.types.output_source_config.serialize_json(
            value["output_source_config"]
        )
    )
    import capo_entityresolution.types.resolution_techniques

    out["resolutionTechniques"] = (
        capo_entityresolution.types.resolution_techniques.serialize_json(
            value["resolution_techniques"]
        )
    )
    if "incremental_run_config" in value:
        import capo_entityresolution.types.incremental_run_config

        out["incrementalRunConfig"] = (
            capo_entityresolution.types.incremental_run_config.serialize_json(
                value["incremental_run_config"]
            )
        )
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> CreateMatchingWorkflowOutput:
    out: CreateMatchingWorkflowOutput = {}  # type: ignore[typeddict-item]
    if data.get("workflowName") is not None:
        out["workflow_name"] = data["workflowName"]
    else:
        out["workflow_name"] = ""
    if data.get("workflowArn") is not None:
        out["workflow_arn"] = data["workflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inputSourceConfig") is not None:
        import capo_entityresolution.types.input_source_config

        out["input_source_config"] = (
            capo_entityresolution.types.input_source_config.deserialize_json(
                data["inputSourceConfig"]
            )
        )
    else:
        out["input_source_config"] = []
    if data.get("outputSourceConfig") is not None:
        import capo_entityresolution.types.output_source_config

        out["output_source_config"] = (
            capo_entityresolution.types.output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    else:
        out["output_source_config"] = []
    if data.get("resolutionTechniques") is not None:
        import capo_entityresolution.types.resolution_techniques

        out["resolution_techniques"] = (
            capo_entityresolution.types.resolution_techniques.deserialize_json(
                data["resolutionTechniques"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowOutput.resolution_techniques required"
        )
    if data.get("incrementalRunConfig") is not None:
        import capo_entityresolution.types.incremental_run_config

        out["incremental_run_config"] = (
            capo_entityresolution.types.incremental_run_config.deserialize_json(
                data["incrementalRunConfig"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
