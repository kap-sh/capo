"""Generated from Smithy shape ``com.amazonaws.appstream#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.applications
    import capo_appstream.types.appstream_agent_version
    import capo_appstream.types.arn
    import capo_appstream.types.boolean
    import capo_appstream.types.dynamic_app_providers_enabled
    import capo_appstream.types.image_permissions
    import capo_appstream.types.image_shared_with_others
    import capo_appstream.types.image_software_metadata
    import capo_appstream.types.image_state
    import capo_appstream.types.image_state_change_reason
    import capo_appstream.types.image_type
    import capo_appstream.types.latest_appstream_agent_version
    import capo_appstream.types.platform_type
    import capo_appstream.types.resource_errors
    import capo_appstream.types.string
    import capo_appstream.types.string_list
    import capo_appstream.types.timestamp
    import capo_appstream.types.visibility_type


class Image(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image.</p>"""
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the image.</p>"""
    base_image_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the image from which this image was created.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The image name to display.</p>"""
    state: NotRequired["capo_appstream.types.image_state.ImageState"]
    """<p>The image starts in the <code>PENDING</code> state. If image creation succeeds, the state is <code>AVAILABLE</code>. If image creation fails, the state is <code>FAILED</code>.</p>"""
    visibility: NotRequired["capo_appstream.types.visibility_type.VisibilityType"]
    """<p>Indicates whether the image is public or private.</p>"""
    image_builder_supported: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Indicates whether an image builder can be launched from this image.</p>"""
    image_builder_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image builder that was used to create the private image. If the image is shared, copied, or updated by using Managed Image Updates, this value is null.</p>"""
    platform: NotRequired["capo_appstream.types.platform_type.PlatformType"]
    """<p>The operating system platform of the image.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description to display.</p>"""
    state_change_reason: NotRequired[
        "capo_appstream.types.image_state_change_reason.ImageStateChangeReason"
    ]
    """<p>The reason why the last state change occurred.</p>"""
    applications: NotRequired["capo_appstream.types.applications.Applications"]
    """<p>The applications associated with the image.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time the image was created.</p>"""
    public_base_image_released_date: NotRequired[
        "capo_appstream.types.timestamp.Timestamp"
    ]
    """<p>The release date of the public base image. For private images, this date is the release date of the base image from which the image was created.</p>"""
    appstream_agent_version: NotRequired[
        "capo_appstream.types.appstream_agent_version.AppstreamAgentVersion"
    ]
    """<p>The version of the WorkSpaces Applications agent to use for instances that are launched from this image. </p>"""
    image_permissions: NotRequired[
        "capo_appstream.types.image_permissions.ImagePermissions"
    ]
    """<p>The permissions to provide to the destination AWS account for the specified image.</p>"""
    image_errors: NotRequired["capo_appstream.types.resource_errors.ResourceErrors"]
    """<p>Describes the errors that are returned when a new image can't be created.</p>"""
    latest_appstream_agent_version: NotRequired[
        "capo_appstream.types.latest_appstream_agent_version.LatestAppstreamAgentVersion"
    ]
    """<p>Indicates whether the image is using the latest WorkSpaces Applications agent version or not.</p>"""
    supported_instance_families: NotRequired[
        "capo_appstream.types.string_list.StringList"
    ]
    """<p>The supported instances families that determine which image a customer can use when the customer launches a fleet or image builder. The following instances families are supported:</p> <ul> <li> <p>General Purpose</p> </li> <li> <p>Compute Optimized</p> </li> <li> <p>Memory Optimized</p> </li> <li> <p>Graphics G4</p> </li> <li> <p>Graphics G5</p> </li> <li> <p>Graphics G6</p> </li> </ul>"""
    dynamic_app_providers_enabled: NotRequired[
        "capo_appstream.types.dynamic_app_providers_enabled.DynamicAppProvidersEnabled"
    ]
    """<p>Indicates whether dynamic app providers are enabled within an WorkSpaces Applications image or not.</p>"""
    image_shared_with_others: NotRequired[
        "capo_appstream.types.image_shared_with_others.ImageSharedWithOthers"
    ]
    """<p>Indicates whether the image is shared with another account ID.</p>"""
    managed_software_included: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Indicates whether the image includes license-included applications.</p>"""
    image_type: NotRequired["capo_appstream.types.image_type.ImageType"]
    """<p>The type of the image. Images created through AMI import have type "custom", while WorkSpaces Applications provided images have type "native". Custom images support additional instance types including GeneralPurpose, MemoryOptimized, ComputeOptimized, and Accelerated instance families.</p>"""
    image_software_metadata: NotRequired[
        "capo_appstream.types.image_software_metadata.ImageSoftwareMetadata"
    ]
    """<p>The software metadata associated with the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Image) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "base_image_arn" in value:
        out["BaseImageArn"] = value["base_image_arn"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "state" in value:
        import capo_appstream.types.image_state

        out["State"] = capo_appstream.types.image_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "visibility" in value:
        import capo_appstream.types.visibility_type

        out["Visibility"] = capo_appstream.types.visibility_type.serialize_aws_json_1_1(
            value["visibility"]
        )
    if "image_builder_supported" in value:
        out["ImageBuilderSupported"] = value["image_builder_supported"]
    if "image_builder_name" in value:
        out["ImageBuilderName"] = value["image_builder_name"]
    if "platform" in value:
        import capo_appstream.types.platform_type

        out["Platform"] = capo_appstream.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "state_change_reason" in value:
        import capo_appstream.types.image_state_change_reason

        out["StateChangeReason"] = (
            capo_appstream.types.image_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "applications" in value:
        import capo_appstream.types.applications

        out["Applications"] = capo_appstream.types.applications.serialize_aws_json_1_1(
            value["applications"]
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "public_base_image_released_date" in value:
        import capo_appstream.types.timestamp

        out["PublicBaseImageReleasedDate"] = (
            capo_appstream.types.timestamp.serialize_aws_json_1_1(
                value["public_base_image_released_date"]
            )
        )
    if "appstream_agent_version" in value:
        out["AppstreamAgentVersion"] = value["appstream_agent_version"]
    if "image_permissions" in value:
        import capo_appstream.types.image_permissions

        out["ImagePermissions"] = (
            capo_appstream.types.image_permissions.serialize_aws_json_1_1(
                value["image_permissions"]
            )
        )
    if "image_errors" in value:
        import capo_appstream.types.resource_errors

        out["ImageErrors"] = (
            capo_appstream.types.resource_errors.serialize_aws_json_1_1(
                value["image_errors"]
            )
        )
    if "latest_appstream_agent_version" in value:
        import capo_appstream.types.latest_appstream_agent_version

        out["LatestAppstreamAgentVersion"] = (
            capo_appstream.types.latest_appstream_agent_version.serialize_aws_json_1_1(
                value["latest_appstream_agent_version"]
            )
        )
    if "supported_instance_families" in value:
        import capo_appstream.types.string_list

        out["SupportedInstanceFamilies"] = (
            capo_appstream.types.string_list.serialize_aws_json_1_1(
                value["supported_instance_families"]
            )
        )
    if "dynamic_app_providers_enabled" in value:
        import capo_appstream.types.dynamic_app_providers_enabled

        out["DynamicAppProvidersEnabled"] = (
            capo_appstream.types.dynamic_app_providers_enabled.serialize_aws_json_1_1(
                value["dynamic_app_providers_enabled"]
            )
        )
    if "image_shared_with_others" in value:
        import capo_appstream.types.image_shared_with_others

        out["ImageSharedWithOthers"] = (
            capo_appstream.types.image_shared_with_others.serialize_aws_json_1_1(
                value["image_shared_with_others"]
            )
        )
    if "managed_software_included" in value:
        out["ManagedSoftwareIncluded"] = value["managed_software_included"]
    if "image_type" in value:
        import capo_appstream.types.image_type

        out["ImageType"] = capo_appstream.types.image_type.serialize_aws_json_1_1(
            value["image_type"]
        )
    if "image_software_metadata" in value:
        import capo_appstream.types.image_software_metadata

        out["ImageSoftwareMetadata"] = (
            capo_appstream.types.image_software_metadata.serialize_aws_json_1_1(
                value["image_software_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("BaseImageArn") is not None:
        out["base_image_arn"] = data["BaseImageArn"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("State") is not None:
        import capo_appstream.types.image_state

        out["state"] = capo_appstream.types.image_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("Visibility") is not None:
        import capo_appstream.types.visibility_type

        out["visibility"] = (
            capo_appstream.types.visibility_type.deserialize_aws_json_1_1(
                data["Visibility"]
            )
        )
    if data.get("ImageBuilderSupported") is not None:
        out["image_builder_supported"] = data["ImageBuilderSupported"]
    if data.get("ImageBuilderName") is not None:
        out["image_builder_name"] = data["ImageBuilderName"]
    if data.get("Platform") is not None:
        import capo_appstream.types.platform_type

        out["platform"] = capo_appstream.types.platform_type.deserialize_aws_json_1_1(
            data["Platform"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("StateChangeReason") is not None:
        import capo_appstream.types.image_state_change_reason

        out["state_change_reason"] = (
            capo_appstream.types.image_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if data.get("Applications") is not None:
        import capo_appstream.types.applications

        out["applications"] = (
            capo_appstream.types.applications.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("PublicBaseImageReleasedDate") is not None:
        import capo_appstream.types.timestamp

        out["public_base_image_released_date"] = (
            capo_appstream.types.timestamp.deserialize_aws_json_1_1(
                data["PublicBaseImageReleasedDate"]
            )
        )
    if data.get("AppstreamAgentVersion") is not None:
        out["appstream_agent_version"] = data["AppstreamAgentVersion"]
    if data.get("ImagePermissions") is not None:
        import capo_appstream.types.image_permissions

        out["image_permissions"] = (
            capo_appstream.types.image_permissions.deserialize_aws_json_1_1(
                data["ImagePermissions"]
            )
        )
    if data.get("ImageErrors") is not None:
        import capo_appstream.types.resource_errors

        out["image_errors"] = (
            capo_appstream.types.resource_errors.deserialize_aws_json_1_1(
                data["ImageErrors"]
            )
        )
    if data.get("LatestAppstreamAgentVersion") is not None:
        import capo_appstream.types.latest_appstream_agent_version

        out["latest_appstream_agent_version"] = (
            capo_appstream.types.latest_appstream_agent_version.deserialize_aws_json_1_1(
                data["LatestAppstreamAgentVersion"]
            )
        )
    if data.get("SupportedInstanceFamilies") is not None:
        import capo_appstream.types.string_list

        out["supported_instance_families"] = (
            capo_appstream.types.string_list.deserialize_aws_json_1_1(
                data["SupportedInstanceFamilies"]
            )
        )
    if data.get("DynamicAppProvidersEnabled") is not None:
        import capo_appstream.types.dynamic_app_providers_enabled

        out["dynamic_app_providers_enabled"] = (
            capo_appstream.types.dynamic_app_providers_enabled.deserialize_aws_json_1_1(
                data["DynamicAppProvidersEnabled"]
            )
        )
    if data.get("ImageSharedWithOthers") is not None:
        import capo_appstream.types.image_shared_with_others

        out["image_shared_with_others"] = (
            capo_appstream.types.image_shared_with_others.deserialize_aws_json_1_1(
                data["ImageSharedWithOthers"]
            )
        )
    if data.get("ManagedSoftwareIncluded") is not None:
        out["managed_software_included"] = data["ManagedSoftwareIncluded"]
    if data.get("ImageType") is not None:
        import capo_appstream.types.image_type

        out["image_type"] = capo_appstream.types.image_type.deserialize_aws_json_1_1(
            data["ImageType"]
        )
    if data.get("ImageSoftwareMetadata") is not None:
        import capo_appstream.types.image_software_metadata

        out["image_software_metadata"] = (
            capo_appstream.types.image_software_metadata.deserialize_aws_json_1_1(
                data["ImageSoftwareMetadata"]
            )
        )
    return out
