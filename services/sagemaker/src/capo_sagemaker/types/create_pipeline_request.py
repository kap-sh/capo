"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreatePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.idempotency_token
    import capo_sagemaker.types.parallelism_configuration
    import capo_sagemaker.types.pipeline_definition
    import capo_sagemaker.types.pipeline_definition_s3_location
    import capo_sagemaker.types.pipeline_description
    import capo_sagemaker.types.pipeline_name
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class CreatePipelineRequest(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_sagemaker.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_display_name: NotRequired[
        "capo_sagemaker.types.pipeline_name.PipelineName"
    ]
    """<p>The display name of the pipeline.</p>"""
    pipeline_definition: NotRequired[
        "capo_sagemaker.types.pipeline_definition.PipelineDefinition"
    ]
    """<p>The <a href="https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/">JSON pipeline definition</a> of the pipeline.</p>"""
    pipeline_definition_s3_location: NotRequired[
        "capo_sagemaker.types.pipeline_definition_s3_location.PipelineDefinitionS3Location"
    ]
    """<p>The location of the pipeline definition stored in Amazon S3. If specified, SageMaker will retrieve the pipeline definition from this location.</p>"""
    pipeline_description: NotRequired[
        "capo_sagemaker.types.pipeline_description.PipelineDescription"
    ]
    """<p>A description of the pipeline.</p>"""
    client_request_token: NotRequired[
        "capo_sagemaker.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the role used by the pipeline to access and create resources.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of tags to apply to the created pipeline.</p>"""
    parallelism_configuration: NotRequired[
        "capo_sagemaker.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>This is the configuration that controls the parallelism of the pipeline. If specified, it applies to all runs of this pipeline by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePipelineRequest) -> dict:
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
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "parallelism_configuration" in value:
        import capo_sagemaker.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            capo_sagemaker.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePipelineRequest:
    out: CreatePipelineRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ParallelismConfiguration") is not None:
        import capo_sagemaker.types.parallelism_configuration

        out["parallelism_configuration"] = (
            capo_sagemaker.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    return out
