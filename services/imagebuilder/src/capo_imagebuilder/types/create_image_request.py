"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.container_recipe_arn
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.image_recipe_arn
    import capo_imagebuilder.types.image_scanning_configuration
    import capo_imagebuilder.types.image_tests_configuration
    import capo_imagebuilder.types.infrastructure_configuration_arn
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.workflow_configuration_list


class CreateImageRequest(TypedDict, closed=True):
    image_recipe_arn: NotRequired[
        "capo_imagebuilder.types.image_recipe_arn.ImageRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed. You must specify either this property or <code>containerRecipeArn</code>, but not both.</p>"""
    container_recipe_arn: NotRequired[
        "capo_imagebuilder.types.container_recipe_arn.ContainerRecipeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested. You must specify either this property or <code>imageRecipeArn</code>, but not both.</p>"""
    distribution_configuration_arn: NotRequired[
        "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of the image build. If you don't specify a distribution configuration, Image Builder creates the output image only in the account and Amazon Web Services Region where the build runs.</p>"""
    infrastructure_configuration_arn: "capo_imagebuilder.types.infrastructure_configuration_arn.InfrastructureConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.</p>"""
    image_tests_configuration: NotRequired[
        "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>Settings that determine whether Image Builder runs tests on the image after building it. Image tests are enabled by default.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to <code>true</code>.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>Settings for vulnerability scans that Amazon Inspector runs during image creation. For AMI output, Amazon Inspector scans the test instance. For container output, Amazon Inspector scans the container image that Image Builder pushes to the Amazon ECR repository specified in <code>ecrConfiguration</code>.</p>"""
    workflows: NotRequired[
        "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
    ]
    """<p>The array of workflow configuration objects for the build. If you specify workflows, they replace the default workflows that Image Builder otherwise runs for the build, and you must also provide an <code>executionRole</code>.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions. This property is required if you specify <code>workflows</code>. If you don't provide a role, Image Builder uses the Image Builder service-linked role in your account, and creates it if it doesn't exist.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The CloudWatch Logs log group where Image Builder sends the image build logs. If you specify a log group name outside of the <code>/aws/imagebuilder/</code> namespace, you must also provide an <code>executionRole</code> that has permission to write to that log group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImageRequest) -> dict:
    out: dict = {}
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    if "distribution_configuration_arn" in value:
        out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    out["infrastructureConfigurationArn"] = value["infrastructure_configuration_arn"]
    if "image_tests_configuration" in value:
        import capo_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            capo_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
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
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "logging_configuration" in value:
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateImageRequest:
    out: CreateImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("imageRecipeArn") is not None:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    if data.get("containerRecipeArn") is not None:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    if data.get("distributionConfigurationArn") is not None:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    if data.get("infrastructureConfigurationArn") is not None:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    else:
        raise DeserializationError(
            "CreateImageRequest.infrastructure_configuration_arn required"
        )
    if data.get("imageTestsConfiguration") is not None:
        import capo_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            capo_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
    if data.get("enhancedImageMetadataEnabled") is not None:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateImageRequest.client_token required")
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
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    if data.get("loggingConfiguration") is not None:
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
