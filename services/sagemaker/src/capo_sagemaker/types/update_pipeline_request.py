"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdatePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.parallelism_configuration
    import capo_sagemaker.types.pipeline_definition
    import capo_sagemaker.types.pipeline_definition_s3_location
    import capo_sagemaker.types.pipeline_description
    import capo_sagemaker.types.pipeline_name
    import capo_sagemaker.types.pipeline_version_alias_list
    import capo_sagemaker.types.role_arn


class UpdatePipelineRequest(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline to update.</p>"""
    pipeline_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_definition: NotRequired[
        "capo_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The JSON pipeline definition.</p>"""
    pipeline_definition_s3_location: NotRequired[
        "capo_sagemaker.types.pipeline_definition_s3_location.PipelineDefinitionS3Location"
    ]
    """<p>The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.</p>"""
    pipeline_description: NotRequired[
        "capo_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>The description of the pipeline.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) that the pipeline uses to execute.</p>"""
    parallelism_configuration: NotRequired[
        "capo_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>If specified, it applies to all executions of this pipeline by default.</p>"""
    pipeline_version_aliases: NotRequired[
        "capo_sagemaker.types.pipeline_version_alias_list.PipelineVersionAliasList"
    ]
    """<p>The aliases to assign to the new pipeline version that this update creates. You can specify aliases only when the update changes the pipeline definition. To change the aliases of an existing version, use <code>UpdatePipelineVersion</code>.</p> <p>An alias must be unique within the pipeline. To move an alias from an existing version to the new version, first remove the alias from the existing version with <code>UpdatePipelineVersion</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePipelineRequest) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_display_name" in value:
        out["PipelineDisplayName"] = value["pipeline_display_name"]
    if "pipeline_definition" in value:
        out["PipelineDefinition"] = value["pipeline_definition"]
    if "pipeline_definition_s3_location" in value:
        import capo_sagemaker.types.pipeline_definition_s3_location

        out["PipelineDefinitionS3Location"] = (
            capo_sagemaker.types.pipeline_definition_s3_location.serialize_aws_json_1_1(
                value["pipeline_definition_s3_location"]
            )
        )
    if "pipeline_description" in value:
        out["PipelineDescription"] = value["pipeline_description"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "parallelism_configuration" in value:
        import capo_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            capo_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    if "pipeline_version_aliases" in value:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["PipelineVersionAliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.serialize_aws_json_1_1(
                value["pipeline_version_aliases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePipelineRequest:
    out: UpdatePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineName") is not None:
        out["pipeline_name"] = data["PipelineName"]
    if data.get("PipelineDisplayName") is not None:
        out["pipeline_display_name"] = data["PipelineDisplayName"]
    if data.get("PipelineDefinition") is not None:
        out["pipeline_definition"] = data["PipelineDefinition"]
    if data.get("PipelineDefinitionS3Location") is not None:
        import capo_sagemaker.types.pipeline_definition_s3_location

        out["pipeline_definition_s3_location"] = (
            capo_sagemaker.types.pipeline_definition_s3_location.deserialize_aws_json_1_1(
                data["PipelineDefinitionS3Location"]
            )
        )
    if data.get("PipelineDescription") is not None:
        out["pipeline_description"] = data["PipelineDescription"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ParallelismConfiguration") is not None:
        import capo_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            capo_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    if data.get("PipelineVersionAliases") is not None:
        import capo_sagemaker.types.pipeline_version_alias_list

        out["pipeline_version_aliases"] = (
            capo_sagemaker.types.pipeline_version_alias_list.deserialize_aws_json_1_1(
                data["PipelineVersionAliases"]
            )
        )
    return out
