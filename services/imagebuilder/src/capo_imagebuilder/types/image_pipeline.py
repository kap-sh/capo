"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImagePipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.arn
    import capo_imagebuilder.types.consecutive_failures
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.image_scanning_configuration
    import capo_imagebuilder.types.image_status
    import capo_imagebuilder.types.image_tests_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.pipeline_logging_configuration
    import capo_imagebuilder.types.pipeline_status
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.schedule
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.workflow_configuration_list


class ImagePipeline(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the image pipeline.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the image pipeline.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the image pipeline.</p>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The platform of the image pipeline, inherited from the recipe that the pipeline uses.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to collect additional information about the image being created, including the operating system (OS) version and package list. Defaults to <code>true</code>.</p>"""
    image_recipe_arn: NotRequired["capo_imagebuilder.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.</p>"""
    container_recipe_arn: NotRequired["capo_imagebuilder.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.</p>"""
    infrastructure_configuration_arn: NotRequired["capo_imagebuilder.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.</p>"""
    distribution_configuration_arn: NotRequired["capo_imagebuilder.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.</p>"""
    image_tests_configuration: NotRequired[
        "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>The image tests configuration of the image pipeline.</p>"""
    schedule: NotRequired["capo_imagebuilder.types.schedule.Schedule"]
    """<p>The schedule of the image pipeline.</p>"""
    status: NotRequired["capo_imagebuilder.types.pipeline_status.PipelineStatus"]
    """<p>The status of the image pipeline. A disabled pipeline doesn't run on its schedule, but you can still start builds manually. Image Builder can also disable a pipeline automatically when consecutive scheduled builds fail.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this image pipeline was created.</p>"""
    date_updated: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this image pipeline was last updated.</p>"""
    date_last_run: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which this image pipeline was last run.</p>"""
    last_run_status: NotRequired["capo_imagebuilder.types.image_status.ImageStatus"]
    """<p>The status of the last image that this pipeline built, such as <code>BUILDING</code>, <code>TESTING</code>, <code>FAILED</code>, or <code>AVAILABLE</code>.</p>"""
    date_next_run: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The next date when the pipeline is scheduled to run.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of this image pipeline.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>Contains settings for vulnerability scans that Amazon Inspector runs against the test instance during image creation.</p>"""
    image_tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that Image Builder applies to the Image Builder image resource that this pipeline's scheduled executions create. These tags don't apply to the output AMI. Builds that you start manually use the tags from the <a href="https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_StartImagePipelineExecution.html">StartImagePipelineExecution</a> request instead.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>"""
    workflows: NotRequired[
        "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
    ]
    """<p>Contains the workflows that run for the image pipeline.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.pipeline_logging_configuration.PipelineLoggingConfiguration"
    ]
    """<p>The CloudWatch Logs configuration for the pipeline: the log group for image build logs and the log group for pipeline execution logs.</p>"""
    consecutive_failures: NotRequired[
        "capo_imagebuilder.types.consecutive_failures.ConsecutiveFailures"
    ]
    """<p>Image Builder tracks the number of consecutive failures for scheduled pipeline executions and takes one of the following actions each time it runs on a schedule:</p> <ul> <li> <p>If the pipeline execution is successful, the number of consecutive failures resets to zero.</p> </li> <li> <p>If the pipeline execution fails, Image Builder increments the number of consecutive failures. If the failure count reaches the limit defined in the <a>AutoDisablePolicy</a>, Image Builder disables the pipeline.</p> </li> </ul> <p>The consecutive failure count is also reset to zero under the following conditions:</p> <ul> <li> <p>The pipeline runs manually and succeeds.</p> </li> <li> <p>The pipeline configuration is updated.</p> </li> </ul> <p>If the pipeline runs manually and fails, the count remains the same. The next scheduled run continues to increment where it left off before.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImagePipeline) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "image_recipe_arn" in value:
        out["imageRecipeArn"] = value["image_recipe_arn"]
    if "container_recipe_arn" in value:
        out["containerRecipeArn"] = value["container_recipe_arn"]
    if "infrastructure_configuration_arn" in value:
        out["infrastructureConfigurationArn"] = value[
            "infrastructure_configuration_arn"
        ]
    if "distribution_configuration_arn" in value:
        out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    if "image_tests_configuration" in value:
        import capo_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            capo_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
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
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "date_updated" in value:
        out["dateUpdated"] = value["date_updated"]
    if "date_last_run" in value:
        out["dateLastRun"] = value["date_last_run"]
    if "last_run_status" in value:
        import capo_imagebuilder.types.image_status

        out["lastRunStatus"] = capo_imagebuilder.types.image_status.serialize_json(
            value["last_run_status"]
        )
    if "date_next_run" in value:
        out["dateNextRun"] = value["date_next_run"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "image_scanning_configuration" in value:
        import capo_imagebuilder.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            capo_imagebuilder.types.image_scanning_configuration.serialize_json(
                value["image_scanning_configuration"]
            )
        )
    if "image_tags" in value:
        import capo_imagebuilder.types.tag_map

        out["imageTags"] = capo_imagebuilder.types.tag_map.serialize_json(
            value["image_tags"]
        )
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
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
    if "consecutive_failures" in value:
        out["consecutiveFailures"] = value["consecutive_failures"]
    return out


def deserialize_json(data: dict) -> ImagePipeline:
    out: ImagePipeline = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("platform") is not None:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if data.get("enhancedImageMetadataEnabled") is not None:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if data.get("imageRecipeArn") is not None:
        out["image_recipe_arn"] = data["imageRecipeArn"]
    if data.get("containerRecipeArn") is not None:
        out["container_recipe_arn"] = data["containerRecipeArn"]
    if data.get("infrastructureConfigurationArn") is not None:
        out["infrastructure_configuration_arn"] = data["infrastructureConfigurationArn"]
    if data.get("distributionConfigurationArn") is not None:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    if data.get("imageTestsConfiguration") is not None:
        import capo_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            capo_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
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
    if data.get("dateCreated") is not None:
        out["date_created"] = data["dateCreated"]
    if data.get("dateUpdated") is not None:
        out["date_updated"] = data["dateUpdated"]
    if data.get("dateLastRun") is not None:
        out["date_last_run"] = data["dateLastRun"]
    if data.get("lastRunStatus") is not None:
        import capo_imagebuilder.types.image_status

        out["last_run_status"] = capo_imagebuilder.types.image_status.deserialize_json(
            data["lastRunStatus"]
        )
    if data.get("dateNextRun") is not None:
        out["date_next_run"] = data["dateNextRun"]
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("imageScanningConfiguration") is not None:
        import capo_imagebuilder.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_imagebuilder.types.image_scanning_configuration.deserialize_json(
                data["imageScanningConfiguration"]
            )
        )
    if data.get("imageTags") is not None:
        import capo_imagebuilder.types.tag_map

        out["image_tags"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["imageTags"]
        )
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
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
    if data.get("consecutiveFailures") is not None:
        out["consecutive_failures"] = data["consecutiveFailures"]
    return out
