"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.arn
    import capo_appstream.types.boolean
    import capo_appstream.types.boolean_object
    import capo_appstream.types.compute_capacity
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.domain_join_info
    import capo_appstream.types.fleet_attributes
    import capo_appstream.types.integer
    import capo_appstream.types.name
    import capo_appstream.types.platform_type
    import capo_appstream.types.s3_location
    import capo_appstream.types.stream_view
    import capo_appstream.types.string
    import capo_appstream.types.usb_device_filter_strings
    import capo_appstream.types.volume_config
    import capo_appstream.types.vpc_config


class UpdateFleetRequest(TypedDict, closed=True):
    image_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image used to create the fleet.</p>"""
    image_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the public, private, or shared image to use.</p>"""
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>A unique name for the fleet.</p>"""
    instance_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The instance type to use when launching fleet instances. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> <li> <p>stream.compute.large</p> </li> <li> <p>stream.compute.xlarge</p> </li> <li> <p>stream.compute.2xlarge</p> </li> <li> <p>stream.compute.4xlarge</p> </li> <li> <p>stream.compute.8xlarge</p> </li> <li> <p>stream.memory.large</p> </li> <li> <p>stream.memory.xlarge</p> </li> <li> <p>stream.memory.2xlarge</p> </li> <li> <p>stream.memory.4xlarge</p> </li> <li> <p>stream.memory.8xlarge</p> </li> <li> <p>stream.memory.z1d.large</p> </li> <li> <p>stream.memory.z1d.xlarge</p> </li> <li> <p>stream.memory.z1d.2xlarge</p> </li> <li> <p>stream.memory.z1d.3xlarge</p> </li> <li> <p>stream.memory.z1d.6xlarge</p> </li> <li> <p>stream.memory.z1d.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.xlarge</p> </li> <li> <p>stream.graphics.g4dn.2xlarge</p> </li> <li> <p>stream.graphics.g4dn.4xlarge</p> </li> <li> <p>stream.graphics.g4dn.8xlarge</p> </li> <li> <p>stream.graphics.g4dn.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.16xlarge</p> </li> <li> <p>stream.graphics.g5.xlarge</p> </li> <li> <p>stream.graphics.g5.2xlarge</p> </li> <li> <p>stream.graphics.g5.4xlarge</p> </li> <li> <p>stream.graphics.g5.8xlarge</p> </li> <li> <p>stream.graphics.g5.16xlarge</p> </li> <li> <p>stream.graphics.g5.12xlarge</p> </li> <li> <p>stream.graphics.g5.24xlarge</p> </li> <li> <p>stream.graphics.g6.xlarge</p> </li> <li> <p>stream.graphics.g6.2xlarge</p> </li> <li> <p>stream.graphics.g6.4xlarge</p> </li> <li> <p>stream.graphics.g6.8xlarge</p> </li> <li> <p>stream.graphics.g6.16xlarge</p> </li> <li> <p>stream.graphics.g6.12xlarge</p> </li> <li> <p>stream.graphics.g6.24xlarge</p> </li> <li> <p>stream.graphics.gr6.4xlarge</p> </li> <li> <p>stream.graphics.gr6.8xlarge</p> </li> <li> <p>stream.graphics.g6f.large</p> </li> <li> <p>stream.graphics.g6f.xlarge</p> </li> <li> <p>stream.graphics.g6f.2xlarge</p> </li> <li> <p>stream.graphics.g6f.4xlarge</p> </li> <li> <p>stream.graphics.gr6f.4xlarge</p> </li> </ul> <p>The following instance types are available for Elastic fleets:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>"""
    compute_capacity: NotRequired[
        "capo_appstream.types.compute_capacity.ComputeCapacity"
    ]
    """<p>The desired capacity for the fleet. This is not allowed for Elastic fleets.</p>"""
    vpc_config: NotRequired["capo_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the fleet. This is required for Elastic fleets, but not required for other fleet types. Elastic fleets require that you specify at least two subnets in different availability zones. </p>"""
    max_user_duration_in_seconds: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum amount of time that a streaming session can remain active, in seconds. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.</p> <p>Specify a value between 600 and 432000.</p>"""
    disconnect_timeout_in_seconds: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The amount of time that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within this time interval, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance. </p> <p>Specify a value between 60 and 36000.</p>"""
    delete_vpc_config: NotRequired["capo_appstream.types.boolean.Boolean"]
    """<p>Deletes the VPC association for the specified fleet.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description to display.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The fleet name to display.</p>"""
    enable_default_internet_access: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Enables or disables default internet access for the fleet.</p>"""
    domain_join_info: NotRequired[
        "capo_appstream.types.domain_join_info.DomainJoinInfo"
    ]
    """<p>The name of the directory and organizational unit (OU) to use to join the fleet to a Microsoft Active Directory domain. </p>"""
    idle_disconnect_timeout_in_seconds: NotRequired[
        "capo_appstream.types.integer.Integer"
    ]
    """<p>The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the <code>DisconnectTimeoutInSeconds</code> time interval begins. Users are notified before they are disconnected due to inactivity. If users try to reconnect to the streaming session before the time interval specified in <code>DisconnectTimeoutInSeconds</code> elapses, they are connected to their previous session. Users are considered idle when they stop providing keyboard or mouse input during their streaming session. File uploads and downloads, audio in, audio out, and pixels changing do not qualify as user activity. If users continue to be idle after the time interval in <code>IdleDisconnectTimeoutInSeconds</code> elapses, they are disconnected. </p> <p>To prevent users from being disconnected due to inactivity, specify a value of 0. Otherwise, specify a value between 60 and 36000. The default value is 0.</p> <note> <p>If you enable this feature, we recommend that you specify a value that corresponds exactly to a whole number of minutes (for example, 60, 120, and 180). If you don't do this, the value is rounded to the nearest minute. For example, if you specify a value of 70, users are disconnected after 1 minute of inactivity. If you specify a value that is at the midpoint between two different minutes, the value is rounded up. For example, if you specify a value of 90, users are disconnected after 2 minutes of inactivity. </p> </note>"""
    attributes_to_delete: NotRequired[
        "capo_appstream.types.fleet_attributes.FleetAttributes"
    ]
    """<p>The fleet attributes to delete.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to apply to the fleet. To assume a role, a fleet instance calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    stream_view: NotRequired["capo_appstream.types.stream_view.StreamView"]
    """<p>The WorkSpaces Applications view that is displayed to your users when they stream from the fleet. When <code>APP</code> is specified, only the windows of applications opened by users display. When <code>DESKTOP</code> is specified, the standard desktop that is provided by the operating system displays.</p> <p>The default value is <code>APP</code>.</p>"""
    platform: NotRequired["capo_appstream.types.platform_type.PlatformType"]
    """<p>The platform of the fleet. WINDOWS_SERVER_2019, AMAZON_LINUX2 and UBUNTU_PRO_2404 are supported for Elastic fleets. </p>"""
    max_concurrent_sessions: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum number of concurrent sessions for a fleet.</p>"""
    usb_device_filter_strings: NotRequired[
        "capo_appstream.types.usb_device_filter_strings.UsbDeviceFilterStrings"
    ]
    """<p>The USB device filter strings that specify which USB devices a user can redirect to the fleet streaming session, when using the Windows native client. This is allowed but not required for Elastic fleets.</p>"""
    session_script_s3_location: NotRequired[
        "capo_appstream.types.s3_location.S3Location"
    ]
    """<p>The S3 location of the session scripts configuration zip file. This only applies to Elastic fleets. </p>"""
    max_sessions_per_instance: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The maximum number of user sessions on an instance. This only applies to multi-session fleets.</p>"""
    root_volume_config: NotRequired["capo_appstream.types.volume_config.VolumeConfig"]
    """<p>The updated configuration for the root volume of fleet instances. Note that volume size cannot be decreased below the image volume size.</p>"""
    disable_imdsv1: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p> <note> <p>Before disabling IMDSv1, ensure your WorkSpaces Applications images are running the agent version or managed image update released on or after January 16, 2024 to support IMDSv2 enforcement.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFleetRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "compute_capacity" in value:
        import capo_appstream.types.compute_capacity

        out["ComputeCapacity"] = (
            capo_appstream.types.compute_capacity.serialize_aws_json_1_1(
                value["compute_capacity"]
            )
        )
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "max_user_duration_in_seconds" in value:
        out["MaxUserDurationInSeconds"] = value["max_user_duration_in_seconds"]
    if "disconnect_timeout_in_seconds" in value:
        out["DisconnectTimeoutInSeconds"] = value["disconnect_timeout_in_seconds"]
    if "delete_vpc_config" in value:
        out["DeleteVpcConfig"] = value["delete_vpc_config"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "domain_join_info" in value:
        import capo_appstream.types.domain_join_info

        out["DomainJoinInfo"] = (
            capo_appstream.types.domain_join_info.serialize_aws_json_1_1(
                value["domain_join_info"]
            )
        )
    if "idle_disconnect_timeout_in_seconds" in value:
        out["IdleDisconnectTimeoutInSeconds"] = value[
            "idle_disconnect_timeout_in_seconds"
        ]
    if "attributes_to_delete" in value:
        import capo_appstream.types.fleet_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.fleet_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "stream_view" in value:
        import capo_appstream.types.stream_view

        out["StreamView"] = capo_appstream.types.stream_view.serialize_aws_json_1_1(
            value["stream_view"]
        )
    if "platform" in value:
        import capo_appstream.types.platform_type

        out["Platform"] = capo_appstream.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "max_concurrent_sessions" in value:
        out["MaxConcurrentSessions"] = value["max_concurrent_sessions"]
    if "usb_device_filter_strings" in value:
        import capo_appstream.types.usb_device_filter_strings

        out["UsbDeviceFilterStrings"] = (
            capo_appstream.types.usb_device_filter_strings.serialize_aws_json_1_1(
                value["usb_device_filter_strings"]
            )
        )
    if "session_script_s3_location" in value:
        import capo_appstream.types.s3_location

        out["SessionScriptS3Location"] = (
            capo_appstream.types.s3_location.serialize_aws_json_1_1(
                value["session_script_s3_location"]
            )
        )
    if "max_sessions_per_instance" in value:
        out["MaxSessionsPerInstance"] = value["max_sessions_per_instance"]
    if "root_volume_config" in value:
        import capo_appstream.types.volume_config

        out["RootVolumeConfig"] = (
            capo_appstream.types.volume_config.serialize_aws_json_1_1(
                value["root_volume_config"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFleetRequest:
    out: UpdateFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    if data.get("ImageArn") is not None:
        out["image_arn"] = data["ImageArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("ComputeCapacity") is not None:
        import capo_appstream.types.compute_capacity

        out["compute_capacity"] = (
            capo_appstream.types.compute_capacity.deserialize_aws_json_1_1(
                data["ComputeCapacity"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("MaxUserDurationInSeconds") is not None:
        out["max_user_duration_in_seconds"] = data["MaxUserDurationInSeconds"]
    if data.get("DisconnectTimeoutInSeconds") is not None:
        out["disconnect_timeout_in_seconds"] = data["DisconnectTimeoutInSeconds"]
    if data.get("DeleteVpcConfig") is not None:
        out["delete_vpc_config"] = data["DeleteVpcConfig"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("EnableDefaultInternetAccess") is not None:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if data.get("DomainJoinInfo") is not None:
        import capo_appstream.types.domain_join_info

        out["domain_join_info"] = (
            capo_appstream.types.domain_join_info.deserialize_aws_json_1_1(
                data["DomainJoinInfo"]
            )
        )
    if data.get("IdleDisconnectTimeoutInSeconds") is not None:
        out["idle_disconnect_timeout_in_seconds"] = data[
            "IdleDisconnectTimeoutInSeconds"
        ]
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.fleet_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.fleet_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("StreamView") is not None:
        import capo_appstream.types.stream_view

        out["stream_view"] = capo_appstream.types.stream_view.deserialize_aws_json_1_1(
            data["StreamView"]
        )
    if data.get("Platform") is not None:
        import capo_appstream.types.platform_type

        out["platform"] = capo_appstream.types.platform_type.deserialize_aws_json_1_1(
            data["Platform"]
        )
    if data.get("MaxConcurrentSessions") is not None:
        out["max_concurrent_sessions"] = data["MaxConcurrentSessions"]
    if data.get("UsbDeviceFilterStrings") is not None:
        import capo_appstream.types.usb_device_filter_strings

        out["usb_device_filter_strings"] = (
            capo_appstream.types.usb_device_filter_strings.deserialize_aws_json_1_1(
                data["UsbDeviceFilterStrings"]
            )
        )
    if data.get("SessionScriptS3Location") is not None:
        import capo_appstream.types.s3_location

        out["session_script_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["SessionScriptS3Location"]
            )
        )
    if data.get("MaxSessionsPerInstance") is not None:
        out["max_sessions_per_instance"] = data["MaxSessionsPerInstance"]
    if data.get("RootVolumeConfig") is not None:
        import capo_appstream.types.volume_config

        out["root_volume_config"] = (
            capo_appstream.types.volume_config.deserialize_aws_json_1_1(
                data["RootVolumeConfig"]
            )
        )
    if data.get("DisableIMDSV1") is not None:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
