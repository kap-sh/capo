"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.appstream_agent_version
    import capo_appstream.types.arn
    import capo_appstream.types.boolean_object
    import capo_appstream.types.domain_join_info
    import capo_appstream.types.image_builder_state
    import capo_appstream.types.image_builder_state_change_reason
    import capo_appstream.types.latest_appstream_agent_version
    import capo_appstream.types.network_access_configuration
    import capo_appstream.types.platform_type
    import capo_appstream.types.resource_errors
    import capo_appstream.types.string
    import capo_appstream.types.timestamp
    import capo_appstream.types.volume_config
    import capo_appstream.types.vpc_config


class ImageBuilder(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image builder.</p>"""
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN for the image builder.</p>"""
    image_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the image from which this builder was created.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description to display.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The image builder name to display.</p>"""
    vpc_config: NotRequired["capo_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration of the image builder.</p>"""
    instance_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The instance type for the image builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.compute.large</p> </li> <li> <p>stream.compute.xlarge</p> </li> <li> <p>stream.compute.2xlarge</p> </li> <li> <p>stream.compute.4xlarge</p> </li> <li> <p>stream.compute.8xlarge</p> </li> <li> <p>stream.memory.large</p> </li> <li> <p>stream.memory.xlarge</p> </li> <li> <p>stream.memory.2xlarge</p> </li> <li> <p>stream.memory.4xlarge</p> </li> <li> <p>stream.memory.8xlarge</p> </li> <li> <p>stream.memory.z1d.large</p> </li> <li> <p>stream.memory.z1d.xlarge</p> </li> <li> <p>stream.memory.z1d.2xlarge</p> </li> <li> <p>stream.memory.z1d.3xlarge</p> </li> <li> <p>stream.memory.z1d.6xlarge</p> </li> <li> <p>stream.memory.z1d.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.xlarge</p> </li> <li> <p>stream.graphics.g4dn.2xlarge</p> </li> <li> <p>stream.graphics.g4dn.4xlarge</p> </li> <li> <p>stream.graphics.g4dn.8xlarge</p> </li> <li> <p>stream.graphics.g4dn.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.16xlarge</p> </li> <li> <p>stream.graphics.g5.xlarge</p> </li> <li> <p>stream.graphics.g5.2xlarge</p> </li> <li> <p>stream.graphics.g5.4xlarge</p> </li> <li> <p>stream.graphics.g5.8xlarge</p> </li> <li> <p>stream.graphics.g5.16xlarge</p> </li> <li> <p>stream.graphics.g5.12xlarge</p> </li> <li> <p>stream.graphics.g5.24xlarge</p> </li> <li> <p>stream.graphics.g6.xlarge</p> </li> <li> <p>stream.graphics.g6.2xlarge</p> </li> <li> <p>stream.graphics.g6.4xlarge</p> </li> <li> <p>stream.graphics.g6.8xlarge</p> </li> <li> <p>stream.graphics.g6.16xlarge</p> </li> <li> <p>stream.graphics.g6.12xlarge</p> </li> <li> <p>stream.graphics.g6.24xlarge</p> </li> <li> <p>stream.graphics.gr6.4xlarge</p> </li> <li> <p>stream.graphics.gr6.8xlarge</p> </li> <li> <p>stream.graphics.g6f.large</p> </li> <li> <p>stream.graphics.g6f.xlarge</p> </li> <li> <p>stream.graphics.g6f.2xlarge</p> </li> <li> <p>stream.graphics.g6f.4xlarge</p> </li> <li> <p>stream.graphics.gr6f.4xlarge</p> </li> </ul>"""
    platform: NotRequired["capo_appstream.types.platform_type.PlatformType"]
    """<p>The operating system platform of the image builder.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    state: NotRequired["capo_appstream.types.image_builder_state.ImageBuilderState"]
    """<p>The state of the image builder.</p>"""
    state_change_reason: NotRequired[
        "capo_appstream.types.image_builder_state_change_reason.ImageBuilderStateChangeReason"
    ]
    """<p>The reason why the last state change occurred.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The time stamp when the image builder was created.</p>"""
    enable_default_internet_access: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Enables or disables default internet access for the image builder.</p>"""
    domain_join_info: NotRequired[
        "capo_appstream.types.domain_join_info.DomainJoinInfo"
    ]
    """<p>The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain. </p>"""
    network_access_configuration: NotRequired[
        "capo_appstream.types.network_access_configuration.NetworkAccessConfiguration"
    ]
    image_builder_errors: NotRequired[
        "capo_appstream.types.resource_errors.ResourceErrors"
    ]
    """<p>The image builder errors.</p>"""
    appstream_agent_version: NotRequired[
        "capo_appstream.types.appstream_agent_version.AppstreamAgentVersion"
    ]
    """<p>The version of the WorkSpaces Applications agent that is currently being used by the image builder. </p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.</p>"""
    root_volume_config: NotRequired["capo_appstream.types.volume_config.VolumeConfig"]
    """<p>The current configuration of the root volume for the image builder, including the storage size in GB.</p>"""
    latest_appstream_agent_version: NotRequired[
        "capo_appstream.types.latest_appstream_agent_version.LatestAppstreamAgentVersion"
    ]
    """<p>Indicates whether the image builder is using the latest WorkSpaces Applications agent version or not.</p>"""
    disable_imdsv1: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Indicates whether Instance Metadata Service Version 1 (IMDSv1) is disabled for the image builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilder) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "platform" in value:
        import capo_appstream.types.platform_type

        out["Platform"] = capo_appstream.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "state" in value:
        import capo_appstream.types.image_builder_state

        out["State"] = capo_appstream.types.image_builder_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_change_reason" in value:
        import capo_appstream.types.image_builder_state_change_reason

        out["StateChangeReason"] = (
            capo_appstream.types.image_builder_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "domain_join_info" in value:
        import capo_appstream.types.domain_join_info

        out["DomainJoinInfo"] = (
            capo_appstream.types.domain_join_info.serialize_aws_json_1_1(
                value["domain_join_info"]
            )
        )
    if "network_access_configuration" in value:
        import capo_appstream.types.network_access_configuration

        out["NetworkAccessConfiguration"] = (
            capo_appstream.types.network_access_configuration.serialize_aws_json_1_1(
                value["network_access_configuration"]
            )
        )
    if "image_builder_errors" in value:
        import capo_appstream.types.resource_errors

        out["ImageBuilderErrors"] = (
            capo_appstream.types.resource_errors.serialize_aws_json_1_1(
                value["image_builder_errors"]
            )
        )
    if "appstream_agent_version" in value:
        out["AppstreamAgentVersion"] = value["appstream_agent_version"]
    if "access_endpoints" in value:
        import capo_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            capo_appstream.types.access_endpoint_list.serialize_aws_json_1_1(
                value["access_endpoints"]
            )
        )
    if "root_volume_config" in value:
        import capo_appstream.types.volume_config

        out["RootVolumeConfig"] = (
            capo_appstream.types.volume_config.serialize_aws_json_1_1(
                value["root_volume_config"]
            )
        )
    if "latest_appstream_agent_version" in value:
        import capo_appstream.types.latest_appstream_agent_version

        out["LatestAppstreamAgentVersion"] = (
            capo_appstream.types.latest_appstream_agent_version.serialize_aws_json_1_1(
                value["latest_appstream_agent_version"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageBuilder:
    out: ImageBuilder = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("ImageArn") is not None:
        out["image_arn"] = data["ImageArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("VpcConfig") is not None:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("Platform") is not None:
        import capo_appstream.types.platform_type

        out["platform"] = capo_appstream.types.platform_type.deserialize_aws_json_1_1(
            data["Platform"]
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("State") is not None:
        import capo_appstream.types.image_builder_state

        out["state"] = (
            capo_appstream.types.image_builder_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("StateChangeReason") is not None:
        import capo_appstream.types.image_builder_state_change_reason

        out["state_change_reason"] = (
            capo_appstream.types.image_builder_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("EnableDefaultInternetAccess") is not None:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if data.get("DomainJoinInfo") is not None:
        import capo_appstream.types.domain_join_info

        out["domain_join_info"] = (
            capo_appstream.types.domain_join_info.deserialize_aws_json_1_1(
                data["DomainJoinInfo"]
            )
        )
    if data.get("NetworkAccessConfiguration") is not None:
        import capo_appstream.types.network_access_configuration

        out["network_access_configuration"] = (
            capo_appstream.types.network_access_configuration.deserialize_aws_json_1_1(
                data["NetworkAccessConfiguration"]
            )
        )
    if data.get("ImageBuilderErrors") is not None:
        import capo_appstream.types.resource_errors

        out["image_builder_errors"] = (
            capo_appstream.types.resource_errors.deserialize_aws_json_1_1(
                data["ImageBuilderErrors"]
            )
        )
    if data.get("AppstreamAgentVersion") is not None:
        out["appstream_agent_version"] = data["AppstreamAgentVersion"]
    if data.get("AccessEndpoints") is not None:
        import capo_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_appstream.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    if data.get("RootVolumeConfig") is not None:
        import capo_appstream.types.volume_config

        out["root_volume_config"] = (
            capo_appstream.types.volume_config.deserialize_aws_json_1_1(
                data["RootVolumeConfig"]
            )
        )
    if data.get("LatestAppstreamAgentVersion") is not None:
        import capo_appstream.types.latest_appstream_agent_version

        out["latest_appstream_agent_version"] = (
            capo_appstream.types.latest_appstream_agent_version.deserialize_aws_json_1_1(
                data["LatestAppstreamAgentVersion"]
            )
        )
    if data.get("DisableIMDSV1") is not None:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
