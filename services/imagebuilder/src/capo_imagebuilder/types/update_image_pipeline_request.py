"""Generated from Smithy shape ``com.amazonaws.imagebuilder#UpdateImagePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.container_recipe_arn
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.image_scanning_configuration
    import capo_imagebuilder.types.image_tests_configuration
    import capo_imagebuilder.types.infrastructure_configuration_arn
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.pipeline_logging_configuration
    import capo_imagebuilder.types.pipeline_status
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.schedule
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.workflow_configuration_list


class UpdateImagePipelineRequest(TypedDict, closed=True):
    image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline that you want to update.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the image pipeline.</p>"""
    image_recipe_arn: NotRequired[
        "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that configures images created by this image pipeline. You must specify either this property or <code>containerRecipeArn</code>, but not both.</p>"""
    container_recipe_arn: NotRequired[
        "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container recipe that is used to configure images created by this container pipeline. You must specify either this property or <code>imageRecipeArn</code>, but not both.</p>"""
    infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that Image Builder uses to build images created by this image pipeline.</p>"""
    distribution_configuration_arn: NotRequired[
        "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that Image Builder uses to configure and distribute images created by this image pipeline.</p>"""
    image_tests_configuration: NotRequired[
        "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>Specifies the test settings that Image Builder applies to images that this pipeline creates. If you don't provide test settings, Image Builder stores a default configuration with image tests enabled.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to <code>true</code>.</p>"""
    schedule: NotRequired["capo_imagebuilder.types.schedule.Schedule"]
    """<p>The schedule of the image pipeline. Because the update replaces the entire configuration, omitting this property removes any existing schedule. The pipeline then runs only when you call <a>StartImagePipelineExecution</a>.</p>"""
    status: NotRequired["capo_imagebuilder.types.pipeline_status.PipelineStatus"]
    """<p>The status of the image pipeline. Defaults to <code>ENABLED</code> when omitted. To keep a pipeline disabled, include this property set to <code>DISABLED</code> in your update request.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>Contains settings for vulnerability scans that Amazon Inspector runs against the test instance during image creation.</p>"""
    workflows: NotRequired[
        "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
    ]
    """<p>The array of workflow configuration objects for builds that this pipeline starts. You must also specify <code>executionRole</code> when you provide workflows.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
    ]
    """<p>Specifies the logging configuration for the image pipeline. Use this to define custom CloudWatch Logs log groups for your pipeline execution logs and image build logs. The service manages log groups with names starting with <code>/aws/imagebuilder/</code> using the service-linked role. For custom log group names outside of this prefix, you must also provide an <code>executionRole</code>.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions. If you omit this property, the pipeline reverts to the Image Builder service-linked role.</p>"""
    image_tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that Image Builder applies to the Image Builder image resource that this pipeline's scheduled executions create. These tags don't apply to the output AMI. To tag output AMIs, use <code>amiTags</code> in the pipeline's distribution configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateImagePipelineRequest) -> dict:
    out: dict = {}
    out["imagePipelineArn"] = value["image_pipeline_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    if "distribution_configuration_arn" in value:
        out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    if "image_tests_configuration" in value:
        import capo_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            capo_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "schedule" in value:
        import capo_imagebuilder.types.schedule

        out["schedule"] = capo_imagebuilder.types.schedule.serialize_json(
            value["schedule"]
        )
    if "status" in value:
        import capo_imagebuilder.types.pipeline_status

        out["status"] = capo_imagebuilder.types.pipeline_status.serialize_json(
            value["status"]
        )
    out["clientToken"] = value["client_token"]
    if "image_scanning_configuration" in value:
        import capo_imagebuilder.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            capo_imagebuilder.types.image_scanning_configuration.serialize_json(
                value["image_scanning_configuration"]
            )
        )
    if "workflows" in value:
        import capo_imagebuilder.types.workflow_configuration_list

        out["workflows"] = (
            capo_imagebuilder.types.workflow_configuration_list.serialize_json(
                value["workflows"]
            )
        )
    if "logging_configuration" in value:
        import capo_imagebuilder.types.pipeline_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.pipeline_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "image_tags" in value:
        import capo_imagebuilder.types.tag_map

        out["imageTags"] = capo_imagebuilder.types.tag_map.serialize_json(
            value["image_tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateImagePipelineRequest:
    out: UpdateImagePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("imagePipelineArn") is not None:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    else:
        raise DeserializationError(
            "UpdateImagePipelineRequest.image_pipeline_arn required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("imageRecipeArn") is not None:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    if data.get("containerRecipeArn") is not None:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    if data.get("infrastructureConfigurationArn") is not None:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "UpdateImagePipelineRequest.infrastructure_configuration_arn required"
        )
    if data.get("distributionConfigurationArn") is not None:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    if data.get("imageTestsConfiguration") is not None:
        import capo_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            capo_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
    if data.get("enhancedImageMetadataEnabled") is not None:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if data.get("schedule") is not None:
        import capo_imagebuilder.types.schedule

        out["schedule"] = capo_imagebuilder.types.schedule.deserialize_json(
            data["schedule"]
        )
    if data.get("status") is not None:
        import capo_imagebuilder.types.pipeline_status

        out["status"] = capo_imagebuilder.types.pipeline_status.deserialize_json(
            data["status"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("UpdateImagePipelineRequest.client_token required")
    if data.get("imageScanningConfiguration") is not None:
        import capo_imagebuilder.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_imagebuilder.types.image_scanning_configuration.deserialize_json(
                data["imageScanningConfiguration"]
            )
        )
    if data.get("workflows") is not None:
        import capo_imagebuilder.types.workflow_configuration_list

        out["workflows"] = (
            capo_imagebuilder.types.workflow_configuration_list.deserialize_json(
                data["workflows"]
            )
        )
    if data.get("loggingConfiguration") is not None:
        import capo_imagebuilder.types.pipeline_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.pipeline_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("imageTags") is not None:
        import capo_imagebuilder.types.tag_map

        out["image_tags"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["imageTags"]
        )
    return out
