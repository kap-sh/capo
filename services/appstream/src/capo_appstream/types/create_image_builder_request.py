"""Generated from Smithy shape ``com.amazonaws.appstream#CreateImageBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.appstream_agent_version
    import capo_appstream.types.arn
    import capo_appstream.types.boolean_object
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.domain_join_info
    import capo_appstream.types.name
    import capo_appstream.types.string
    import capo_appstream.types.string_list
    import capo_appstream.types.tags
    import capo_appstream.types.volume_config
    import capo_appstream.types.vpc_config


class CreateImageBuilderRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>A unique name for the image builder.</p>"""
    image_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the image used to create the image builder.</p>"""
    image_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the public, private, or shared image to use.</p>"""
    instance_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The instance type to use when launching the image builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.compute.large</p> </li> <li> <p>stream.compute.xlarge</p> </li> <li> <p>stream.compute.2xlarge</p> </li> <li> <p>stream.compute.4xlarge</p> </li> <li> <p>stream.compute.8xlarge</p> </li> <li> <p>stream.memory.large</p> </li> <li> <p>stream.memory.xlarge</p> </li> <li> <p>stream.memory.2xlarge</p> </li> <li> <p>stream.memory.4xlarge</p> </li> <li> <p>stream.memory.8xlarge</p> </li> <li> <p>stream.memory.z1d.large</p> </li> <li> <p>stream.memory.z1d.xlarge</p> </li> <li> <p>stream.memory.z1d.2xlarge</p> </li> <li> <p>stream.memory.z1d.3xlarge</p> </li> <li> <p>stream.memory.z1d.6xlarge</p> </li> <li> <p>stream.memory.z1d.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.xlarge</p> </li> <li> <p>stream.graphics.g4dn.2xlarge</p> </li> <li> <p>stream.graphics.g4dn.4xlarge</p> </li> <li> <p>stream.graphics.g4dn.8xlarge</p> </li> <li> <p>stream.graphics.g4dn.12xlarge</p> </li> <li> <p>stream.graphics.g4dn.16xlarge</p> </li> <li> <p>stream.graphics.g5.xlarge</p> </li> <li> <p>stream.graphics.g5.2xlarge</p> </li> <li> <p>stream.graphics.g5.4xlarge</p> </li> <li> <p>stream.graphics.g5.8xlarge</p> </li> <li> <p>stream.graphics.g5.16xlarge</p> </li> <li> <p>stream.graphics.g5.12xlarge</p> </li> <li> <p>stream.graphics.g5.24xlarge</p> </li> <li> <p>stream.graphics.g6.xlarge</p> </li> <li> <p>stream.graphics.g6.2xlarge</p> </li> <li> <p>stream.graphics.g6.4xlarge</p> </li> <li> <p>stream.graphics.g6.8xlarge</p> </li> <li> <p>stream.graphics.g6.16xlarge</p> </li> <li> <p>stream.graphics.g6.12xlarge</p> </li> <li> <p>stream.graphics.g6.24xlarge</p> </li> <li> <p>stream.graphics.gr6.4xlarge</p> </li> <li> <p>stream.graphics.gr6.8xlarge</p> </li> <li> <p>stream.graphics.g6f.large</p> </li> <li> <p>stream.graphics.g6f.xlarge</p> </li> <li> <p>stream.graphics.g6f.2xlarge</p> </li> <li> <p>stream.graphics.g6f.4xlarge</p> </li> <li> <p>stream.graphics.gr6f.4xlarge</p> </li> </ul>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description to display.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The image builder name to display.</p>"""
    vpc_config: NotRequired["capo_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the image builder. You can specify only one subnet.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to apply to the image builder. To assume a role, the image builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    enable_default_internet_access: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Enables or disables default internet access for the image builder.</p>"""
    domain_join_info: NotRequired[
        "capo_appstream.types.domain_join_info.DomainJoinInfo"
    ]
    """<p>The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain. </p>"""
    appstream_agent_version: NotRequired[
        "capo_appstream.types.appstream_agent_version.AppstreamAgentVersion"
    ]
    """<p>The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST]. </p>"""
    tags: NotRequired["capo_appstream.types.tags.Tags"]
    r"""<p>The tags to associate with the image builder. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=. </p> <p>Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters: </p> <p>_ . : / = + \ - @</p> <p>If you do not specify a value, the value is set to an empty string.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html">Tagging Your Resources</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the image builder only through the specified endpoints.</p>"""
    root_volume_config: NotRequired["capo_appstream.types.volume_config.VolumeConfig"]
    """<p>The configuration for the root volume of the image builder. Use this to customize storage capacity from 200 GB up to 500 GB based on your application installation requirements.</p>"""
    softwares_to_install: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The list of license included applications to install on the image builder during creation.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>"""
    softwares_to_uninstall: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The list of license included applications to uninstall from the image builder during creation.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>"""
    disable_imdsv1: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p> <note> <p>Before disabling IMDSv1, ensure your WorkSpaces Applications images are running the agent version or managed image update released on or after January 16, 2024 to support IMDSv2 enforcement.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImageBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "domain_join_info" in value:
        import capo_appstream.types.domain_join_info

        out["DomainJoinInfo"] = (
            capo_appstream.types.domain_join_info.serialize_aws_json_1_1(
                value["domain_join_info"]
            )
        )
    if "appstream_agent_version" in value:
        out["AppstreamAgentVersion"] = value["appstream_agent_version"]
    if "tags" in value:
        import capo_appstream.types.tags

        out["Tags"] = capo_appstream.types.tags.serialize_aws_json_1_1(value["tags"])
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
    if "softwares_to_install" in value:
        import capo_appstream.types.string_list

        out["SoftwaresToInstall"] = (
            capo_appstream.types.string_list.serialize_aws_json_1_1(
                value["softwares_to_install"]
            )
        )
    if "softwares_to_uninstall" in value:
        import capo_appstream.types.string_list

        out["SoftwaresToUninstall"] = (
            capo_appstream.types.string_list.serialize_aws_json_1_1(
                value["softwares_to_uninstall"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImageBuilderRequest:
    out: CreateImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    if data.get("ImageArn") is not None:
        out["image_arn"] = data["ImageArn"]
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("VpcConfig") is not None:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("EnableDefaultInternetAccess") is not None:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if data.get("DomainJoinInfo") is not None:
        import capo_appstream.types.domain_join_info

        out["domain_join_info"] = (
            capo_appstream.types.domain_join_info.deserialize_aws_json_1_1(
                data["DomainJoinInfo"]
            )
        )
    if data.get("AppstreamAgentVersion") is not None:
        out["appstream_agent_version"] = data["AppstreamAgentVersion"]
    if data.get("Tags") is not None:
        import capo_appstream.types.tags

        out["tags"] = capo_appstream.types.tags.deserialize_aws_json_1_1(data["Tags"])
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
    if data.get("SoftwaresToInstall") is not None:
        import capo_appstream.types.string_list

        out["softwares_to_install"] = (
            capo_appstream.types.string_list.deserialize_aws_json_1_1(
                data["SoftwaresToInstall"]
            )
        )
    if data.get("SoftwaresToUninstall") is not None:
        import capo_appstream.types.string_list

        out["softwares_to_uninstall"] = (
            capo_appstream.types.string_list.deserialize_aws_json_1_1(
                data["SoftwaresToUninstall"]
            )
        )
    if data.get("DisableIMDSV1") is not None:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
