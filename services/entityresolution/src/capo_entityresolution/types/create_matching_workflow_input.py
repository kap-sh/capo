"""Generated from Smithy shape ``com.amazonaws.entityresolution#CreateMatchingWorkflowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.incremental_run_config
    import capo_entityresolution.types.input_source_config
    import capo_entityresolution.types.output_source_config
    import capo_entityresolution.types.resolution_techniques
    import capo_entityresolution.types.tag_map


class CreateMatchingWorkflowInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow. There can't be multiple <code>MatchingWorkflows</code> with the same name.</p>"""
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
    """<p>Optional. An object that defines the incremental run type. This object contains only the <code>incrementalRunType</code> field, which appears as "Automatic" in the console. </p> <important> <p>For workflows where <code>resolutionType</code> is <code>PROVIDER</code>, incremental processing is not supported. </p> </important>"""
    role_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>"""
    tags: NotRequired["capo_entityresolution.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMatchingWorkflowInput) -> dict:
    out: dict = {}
    out["workflowName"] = value["workflow_name"]
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
    if "tags" in value:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateMatchingWorkflowInput:
    out: CreateMatchingWorkflowInput = {}  # type: ignore[typeddict-item]
    if data.get("workflowName") is not None:
        out["workflow_name"] = data["workflowName"]
    else:
        raise DeserializationError("CreateMatchingWorkflowInput.workflow_name required")
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
        raise DeserializationError(
            "CreateMatchingWorkflowInput.input_source_config required"
        )
    if data.get("outputSourceConfig") is not None:
        import capo_entityresolution.types.output_source_config

        out["output_source_config"] = (
            capo_entityresolution.types.output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowInput.output_source_config required"
        )
    if data.get("resolutionTechniques") is not None:
        import capo_entityresolution.types.resolution_techniques

        out["resolution_techniques"] = (
            capo_entityresolution.types.resolution_techniques.deserialize_json(
                data["resolutionTechniques"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMatchingWorkflowInput.resolution_techniques required"
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
        raise DeserializationError("CreateMatchingWorkflowInput.role_arn required")
    if data.get("tags") is not None:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.deserialize_json(data["tags"])
    return out
