"""Generated from Smithy shape ``com.amazonaws.appstream#UpdateAppBlockBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.app_block_builder_attributes
    import capo_appstream.types.arn
    import capo_appstream.types.boolean_object
    import capo_appstream.types.description
    import capo_appstream.types.display_name
    import capo_appstream.types.name
    import capo_appstream.types.platform_type
    import capo_appstream.types.string
    import capo_appstream.types.vpc_config


class UpdateAppBlockBuilderRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The unique name for the app block builder.</p>"""
    description: NotRequired["capo_appstream.types.description.Description"]
    """<p>The description of the app block builder.</p>"""
    display_name: NotRequired["capo_appstream.types.display_name.DisplayName"]
    """<p>The display name of the app block builder.</p>"""
    platform: NotRequired["capo_appstream.types.platform_type.PlatformType"]
    """<p>The platform of the app block builder.</p> <p> <code>WINDOWS_SERVER_2019</code> is the only valid value.</p>"""
    instance_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The instance type to use when launching the app block builder. The following instance types are available:</p> <ul> <li> <p>stream.standard.small</p> </li> <li> <p>stream.standard.medium</p> </li> <li> <p>stream.standard.large</p> </li> <li> <p>stream.standard.xlarge</p> </li> <li> <p>stream.standard.2xlarge</p> </li> </ul>"""
    vpc_config: NotRequired["capo_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the app block builder.</p> <p>App block builders require that you specify at least two subnets in different availability zones.</p>"""
    enable_default_internet_access: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Enables or disables default internet access for the app block builder.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to apply to the app block builder. To assume a role, the app block builder calls the AWS Security Token Service (STS) <code>AssumeRole</code> API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the <b>appstream_machine_role</b> credential profile on the instance.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html">Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances</a> in the <i>Amazon WorkSpaces Applications Administration Guide</i>.</p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.</p>"""
    attributes_to_delete: NotRequired[
        "capo_appstream.types.app_block_builder_attributes.AppBlockBuilderAttributes"
    ]
    """<p>The attributes to delete from the app block builder.</p>"""
    disable_imdsv1: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Set to true to disable Instance Metadata Service Version 1 (IMDSv1) and enforce IMDSv2. Set to false to enable both IMDSv1 and IMDSv2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAppBlockBuilderRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "platform" in value:
        import capo_appstream.types.platform_type

        out["Platform"] = capo_appstream.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "access_endpoints" in value:
        import capo_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            capo_appstream.types.access_endpoint_list.serialize_aws_json_1_1(
                value["access_endpoints"]
            )
        )
    if "attributes_to_delete" in value:
        import capo_appstream.types.app_block_builder_attributes

        out["AttributesToDelete"] = (
            capo_appstream.types.app_block_builder_attributes.serialize_aws_json_1_1(
                value["attributes_to_delete"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAppBlockBuilderRequest:
    out: UpdateAppBlockBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Platform") is not None:
        import capo_appstream.types.platform_type

        out["platform"] = capo_appstream.types.platform_type.deserialize_aws_json_1_1(
            data["Platform"]
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("VpcConfig") is not None:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("EnableDefaultInternetAccess") is not None:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("AccessEndpoints") is not None:
        import capo_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_appstream.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    if data.get("AttributesToDelete") is not None:
        import capo_appstream.types.app_block_builder_attributes

        out["attributes_to_delete"] = (
            capo_appstream.types.app_block_builder_attributes.deserialize_aws_json_1_1(
                data["AttributesToDelete"]
            )
        )
    if data.get("DisableIMDSV1") is not None:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
