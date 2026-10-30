"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.arn
    import capo_imagebuilder.types.build_type
    import capo_imagebuilder.types.container_recipe
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.date_time_timestamp
    import capo_imagebuilder.types.distribution_configuration
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.image_recipe
    import capo_imagebuilder.types.image_scan_state
    import capo_imagebuilder.types.image_scanning_configuration
    import capo_imagebuilder.types.image_source
    import capo_imagebuilder.types.image_state
    import capo_imagebuilder.types.image_tests_configuration
    import capo_imagebuilder.types.image_type
    import capo_imagebuilder.types.infrastructure_configuration
    import capo_imagebuilder.types.lifecycle_execution_id
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.os_version
    import capo_imagebuilder.types.output_resources
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number_with_build
    import capo_imagebuilder.types.workflow_configuration_list


class Image(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the image.</p> <note> <p>Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:</p> <ol> <li> <p>Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.</p> </li> <li> <p>Version ARNs have only the first three nodes: <major>.<minor>.<patch></p> </li> <li> <p>Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.</p> </li> </ol> </note>"""
    type: NotRequired["capo_imagebuilder.types.image_type.ImageType"]
    """<p>Specifies whether this image produces an AMI or a container image.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the image.</p>"""
    version: NotRequired[
        "capo_imagebuilder.types.version_number_with_build.VersionNumberWithBuild"
    ]
    """<p>The semantic version of the image.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> <p> <b>Filtering:</b> You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The image operating system platform, such as Linux or Windows.</p>"""
    enhanced_image_metadata_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether Image Builder collects additional information about the image, such as the operating system (OS) version and package list.</p>"""
    os_version: NotRequired["capo_imagebuilder.types.os_version.OsVersion"]
    """<p>The operating system version for instances that launch from this image. For example, Amazon Linux 2, Ubuntu 18, or Microsoft Windows Server 2019.</p>"""
    state: NotRequired["capo_imagebuilder.types.image_state.ImageState"]
    """<p>The state of the image.</p>"""
    image_recipe: NotRequired["capo_imagebuilder.types.image_recipe.ImageRecipe"]
    """<p>For images that distribute an AMI, this is the image recipe that Image Builder used to create the image. For container images, this is empty.</p>"""
    container_recipe: NotRequired[
        "capo_imagebuilder.types.container_recipe.ContainerRecipe"
    ]
    """<p>For container images, this is the container recipe that Image Builder used to create the image. For images that distribute an AMI, this is empty.</p>"""
    source_pipeline_name: NotRequired[
        "capo_imagebuilder.types.resource_name.ResourceName"
    ]
    """<p>The name of the image pipeline that created this image. Image Builder doesn't return this field for new images. Use <code>sourcePipelineArn</code> instead.</p>"""
    source_pipeline_arn: NotRequired["capo_imagebuilder.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the image pipeline that created this image. This field is only present for images that a pipeline execution created.</p>"""
    infrastructure_configuration: NotRequired[
        "capo_imagebuilder.types.infrastructure_configuration.InfrastructureConfiguration"
    ]
    """<p>The infrastructure that Image Builder used to create this image.</p>"""
    distribution_configuration: NotRequired[
        "capo_imagebuilder.types.distribution_configuration.DistributionConfiguration"
    ]
    """<p>The distribution configuration that Image Builder used to create this image.</p>"""
    image_tests_configuration: NotRequired[
        "capo_imagebuilder.types.image_tests_configuration.ImageTestsConfiguration"
    ]
    """<p>The image test settings that Image Builder used when it created this image.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date on which Image Builder created this image.</p>"""
    output_resources: NotRequired[
        "capo_imagebuilder.types.output_resources.OutputResources"
    ]
    """<p>The output resources that Image Builder produces for this image.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that apply to this image.</p>"""
    build_type: NotRequired["capo_imagebuilder.types.build_type.BuildType"]
    """<p>Indicates the type of build that created this image. The build can be initiated in the following ways:</p> <ul> <li> <p> <b>USER_INITIATED</b> – A manual pipeline build request.</p> </li> <li> <p> <b>SCHEDULED</b> – A pipeline build initiated by a cron expression in the Image Builder pipeline, or from EventBridge.</p> </li> <li> <p> <b>IMPORT</b> – A VM import created the image to use as the base image for the recipe.</p> </li> <li> <p> <b>IMPORT_ISO</b> – An ISO disk import created the image.</p> </li> </ul>"""
    image_source: NotRequired["capo_imagebuilder.types.image_source.ImageSource"]
    """<p>The origin of the base image that Image Builder used to build this image.</p>"""
    scan_state: NotRequired["capo_imagebuilder.types.image_scan_state.ImageScanState"]
    """<p>Contains information about the current state of scans for this image.</p>"""
    image_scanning_configuration: NotRequired[
        "capo_imagebuilder.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<p>The settings that determine whether and how Amazon Inspector scans this image.</p>"""
    deprecation_time: NotRequired[
        "capo_imagebuilder.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The time when deprecation occurs for an image resource. This can be a past or future date.</p>"""
    lifecycle_execution_id: NotRequired[
        "capo_imagebuilder.types.lifecycle_execution_id.LifecycleExecutionId"
    ]
    """<p>Identifies the last runtime instance of the lifecycle policy to take action on the image.</p>"""
    execution_role: NotRequired[
        "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.</p>"""
    workflows: NotRequired[
        "capo_imagebuilder.types.workflow_configuration_list.WorkflowConfigurationList"
    ]
    """<p>The build, test, and distribution workflow configurations that are associated with the image.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The logging configuration that's defined for the image. Image Builder uses the defined settings to direct execution log output during image creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Image) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "type" in value:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.serialize_json(value["type"])
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "enhanced_image_metadata_enabled" in value:
        out["enhancedImageMetadataEnabled"] = value["enhanced_image_metadata_enabled"]
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    if "state" in value:
        import capo_imagebuilder.types.image_state

        out["state"] = capo_imagebuilder.types.image_state.serialize_json(
            value["state"]
        )
    if "image_recipe" in value:
        import capo_imagebuilder.types.image_recipe

        out["imageRecipe"] = capo_imagebuilder.types.image_recipe.serialize_json(
            value["image_recipe"]
        )
    if "container_recipe" in value:
        import capo_imagebuilder.types.container_recipe

        out["containerRecipe"] = (
            capo_imagebuilder.types.container_recipe.serialize_json(
                value["container_recipe"]
            )
        )
    if "source_pipeline_name" in value:
        out["sourcePipelineName"] = value["source_pipeline_name"]
    if "source_pipeline_arn" in value:
        out["sourcePipelineArn"] = value["source_pipeline_arn"]
    if "infrastructure_configuration" in value:
        import capo_imagebuilder.types.infrastructure_configuration

        out["infrastructureConfiguration"] = (
            capo_imagebuilder.types.infrastructure_configuration.serialize_json(
                value["infrastructure_configuration"]
            )
        )
    if "distribution_configuration" in value:
        import capo_imagebuilder.types.distribution_configuration

        out["distributionConfiguration"] = (
            capo_imagebuilder.types.distribution_configuration.serialize_json(
                value["distribution_configuration"]
            )
        )
    if "image_tests_configuration" in value:
        import capo_imagebuilder.types.image_tests_configuration

        out["imageTestsConfiguration"] = (
            capo_imagebuilder.types.image_tests_configuration.serialize_json(
                value["image_tests_configuration"]
            )
        )
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "output_resources" in value:
        import capo_imagebuilder.types.output_resources

        out["outputResources"] = (
            capo_imagebuilder.types.output_resources.serialize_json(
                value["output_resources"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "build_type" in value:
        import capo_imagebuilder.types.build_type

        out["buildType"] = capo_imagebuilder.types.build_type.serialize_json(
            value["build_type"]
        )
    if "image_source" in value:
        import capo_imagebuilder.types.image_source

        out["imageSource"] = capo_imagebuilder.types.image_source.serialize_json(
            value["image_source"]
        )
    if "scan_state" in value:
        import capo_imagebuilder.types.image_scan_state

        out["scanState"] = capo_imagebuilder.types.image_scan_state.serialize_json(
            value["scan_state"]
        )
    if "image_scanning_configuration" in value:
        import capo_imagebuilder.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            capo_imagebuilder.types.image_scanning_configuration.serialize_json(
                value["image_scanning_configuration"]
            )
        )
    if "deprecation_time" in value:
        import capo_imagebuilder.types.date_time_timestamp

        out["deprecationTime"] = (
            capo_imagebuilder.types.date_time_timestamp.serialize_json(
                value["deprecation_time"]
            )
        )
    if "lifecycle_execution_id" in value:
        out["lifecycleExecutionId"] = value["lifecycle_execution_id"]
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
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("type") is not None:
        import capo_imagebuilder.types.image_type

        out["type"] = capo_imagebuilder.types.image_type.deserialize_json(data["type"])
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("platform") is not None:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if data.get("enhancedImageMetadataEnabled") is not None:
        out["enhanced_image_metadata_enabled"] = data["enhancedImageMetadataEnabled"]
    if data.get("osVersion") is not None:
        out["os_version"] = data["osVersion"]
    if data.get("state") is not None:
        import capo_imagebuilder.types.image_state

        out["state"] = capo_imagebuilder.types.image_state.deserialize_json(
            data["state"]
        )
    if data.get("imageRecipe") is not None:
        import capo_imagebuilder.types.image_recipe

        out["image_recipe"] = capo_imagebuilder.types.image_recipe.deserialize_json(
            data["imageRecipe"]
        )
    if data.get("containerRecipe") is not None:
        import capo_imagebuilder.types.container_recipe

        out["container_recipe"] = (
            capo_imagebuilder.types.container_recipe.deserialize_json(
                data["containerRecipe"]
            )
        )
    if data.get("sourcePipelineName") is not None:
        out["source_pipeline_name"] = data["sourcePipelineName"]
    if data.get("sourcePipelineArn") is not None:
        out["source_pipeline_arn"] = data["sourcePipelineArn"]
    if data.get("infrastructureConfiguration") is not None:
        import capo_imagebuilder.types.infrastructure_configuration

        out["infrastructure_configuration"] = (
            capo_imagebuilder.types.infrastructure_configuration.deserialize_json(
                data["infrastructureConfiguration"]
            )
        )
    if data.get("distributionConfiguration") is not None:
        import capo_imagebuilder.types.distribution_configuration

        out["distribution_configuration"] = (
            capo_imagebuilder.types.distribution_configuration.deserialize_json(
                data["distributionConfiguration"]
            )
        )
    if data.get("imageTestsConfiguration") is not None:
        import capo_imagebuilder.types.image_tests_configuration

        out["image_tests_configuration"] = (
            capo_imagebuilder.types.image_tests_configuration.deserialize_json(
                data["imageTestsConfiguration"]
            )
        )
    if data.get("dateCreated") is not None:
        out["date_created"] = data["dateCreated"]
    if data.get("outputResources") is not None:
        import capo_imagebuilder.types.output_resources

        out["output_resources"] = (
            capo_imagebuilder.types.output_resources.deserialize_json(
                data["outputResources"]
            )
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("buildType") is not None:
        import capo_imagebuilder.types.build_type

        out["build_type"] = capo_imagebuilder.types.build_type.deserialize_json(
            data["buildType"]
        )
    if data.get("imageSource") is not None:
        import capo_imagebuilder.types.image_source

        out["image_source"] = capo_imagebuilder.types.image_source.deserialize_json(
            data["imageSource"]
        )
    if data.get("scanState") is not None:
        import capo_imagebuilder.types.image_scan_state

        out["scan_state"] = capo_imagebuilder.types.image_scan_state.deserialize_json(
            data["scanState"]
        )
    if data.get("imageScanningConfiguration") is not None:
        import capo_imagebuilder.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            capo_imagebuilder.types.image_scanning_configuration.deserialize_json(
                data["imageScanningConfiguration"]
            )
        )
    if data.get("deprecationTime") is not None:
        import capo_imagebuilder.types.date_time_timestamp

        out["deprecation_time"] = (
            capo_imagebuilder.types.date_time_timestamp.deserialize_json(
                data["deprecationTime"]
            )
        )
    if data.get("lifecycleExecutionId") is not None:
        out["lifecycle_execution_id"] = data["lifecycleExecutionId"]
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
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
