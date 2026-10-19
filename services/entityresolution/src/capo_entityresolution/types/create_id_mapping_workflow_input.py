"""Generated from Smithy shape ``com.amazonaws.entityresolution#CreateIdMappingWorkflowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.description
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.id_mapping_incremental_run_config
    import capo_entityresolution.types.id_mapping_role_arn
    import capo_entityresolution.types.id_mapping_techniques
    import capo_entityresolution.types.id_mapping_workflow_input_source_config
    import capo_entityresolution.types.id_mapping_workflow_output_source_config
    import capo_entityresolution.types.tag_map


class CreateIdMappingWorkflowInput(TypedDict, closed=True):
    workflow_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow. There can't be multiple <code>IdMappingWorkflows</code> with the same name.</p>"""
    description: NotRequired["capo_entityresolution.types.description.Description"]
    """<p>A description of the workflow.</p>"""
    input_source_config: "capo_entityresolution.types.id_mapping_workflow_input_source_config.IdMappingWorkflowInputSourceConfig"
    """<p>A list of <code>InputSource</code> objects, which have the fields <code>InputSourceARN</code> and <code>SchemaName</code>.</p>"""
    output_source_config: NotRequired[
        "capo_entityresolution.types.id_mapping_workflow_output_source_config.IdMappingWorkflowOutputSourceConfig"
    ]
    """<p>A list of <code>IdMappingWorkflowOutputSource</code> objects, each of which contains fields <code>outputS3Path</code> and <code>KMSArn</code>.</p>"""
    id_mapping_techniques: (
        "capo_entityresolution.types.id_mapping_techniques.IdMappingTechniques"
    )
    """<p>An object which defines the ID mapping technique and any additional configurations.</p>"""
    incremental_run_config: NotRequired[
        "capo_entityresolution.types.id_mapping_incremental_run_config.IdMappingIncrementalRunConfig"
    ]
    """<p> The incremental run configuration for the ID mapping workflow.</p>"""
    role_arn: NotRequired[
        "capo_entityresolution.types.id_mapping_role_arn.IdMappingRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to create resources on your behalf as part of workflow execution.</p>"""
    tags: NotRequired["capo_entityresolution.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIdMappingWorkflowInput) -> dict:
    out: dict = {}
    out["workflowName"] = value["workflow_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_entityresolution.types.id_mapping_workflow_input_source_config

    out["inputSourceConfig"] = (
        capo_entityresolution.types.id_mapping_workflow_input_source_config.serialize_json(
            value["input_source_config"]
        )
    )
    if "output_source_config" in value:
        import capo_entityresolution.types.id_mapping_workflow_output_source_config

        out["outputSourceConfig"] = (
            capo_entityresolution.types.id_mapping_workflow_output_source_config.serialize_json(
                value["output_source_config"]
            )
        )
    import capo_entityresolution.types.id_mapping_techniques

    out["idMappingTechniques"] = (
        capo_entityresolution.types.id_mapping_techniques.serialize_json(
            value["id_mapping_techniques"]
        )
    )
    if "incremental_run_config" in value:
        import capo_entityresolution.types.id_mapping_incremental_run_config

        out["incrementalRunConfig"] = (
            capo_entityresolution.types.id_mapping_incremental_run_config.serialize_json(
                value["incremental_run_config"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIdMappingWorkflowInput:
    out: CreateIdMappingWorkflowInput = {}  # type: ignore[typeddict-item]
    if data.get("workflowName") is not None:
        out["workflow_name"] = data["workflowName"]
    else:
        raise DeserializationError(
            "CreateIdMappingWorkflowInput.workflow_name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("inputSourceConfig") is not None:
        import capo_entityresolution.types.id_mapping_workflow_input_source_config

        out["input_source_config"] = (
            capo_entityresolution.types.id_mapping_workflow_input_source_config.deserialize_json(
                data["inputSourceConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdMappingWorkflowInput.input_source_config required"
        )
    if data.get("outputSourceConfig") is not None:
        import capo_entityresolution.types.id_mapping_workflow_output_source_config

        out["output_source_config"] = (
            capo_entityresolution.types.id_mapping_workflow_output_source_config.deserialize_json(
                data["outputSourceConfig"]
            )
        )
    if data.get("idMappingTechniques") is not None:
        import capo_entityresolution.types.id_mapping_techniques

        out["id_mapping_techniques"] = (
            capo_entityresolution.types.id_mapping_techniques.deserialize_json(
                data["idMappingTechniques"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIdMappingWorkflowInput.id_mapping_techniques required"
        )
    if data.get("incrementalRunConfig") is not None:
        import capo_entityresolution.types.id_mapping_incremental_run_config

        out["incremental_run_config"] = (
            capo_entityresolution.types.id_mapping_incremental_run_config.deserialize_json(
                data["incrementalRunConfig"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("tags") is not None:
        import capo_entityresolution.types.tag_map

        out["tags"] = capo_entityresolution.types.tag_map.deserialize_json(data["tags"])
    return out
