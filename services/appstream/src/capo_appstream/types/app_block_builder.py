"""Generated from Smithy shape ``com.amazonaws.appstream#AppBlockBuilder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.access_endpoint_list
    import capo_appstream.types.app_block_builder_platform_type
    import capo_appstream.types.app_block_builder_state
    import capo_appstream.types.app_block_builder_state_change_reason
    import capo_appstream.types.arn
    import capo_appstream.types.boolean_object
    import capo_appstream.types.resource_errors
    import capo_appstream.types.string
    import capo_appstream.types.timestamp
    import capo_appstream.types.vpc_config


class AppBlockBuilder(TypedDict, closed=True):
    arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the app block builder.</p>"""
    name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the app block builder.</p>"""
    display_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The display name of the app block builder.</p>"""
    description: NotRequired["capo_appstream.types.string.String"]
    """<p>The description of the app block builder.</p>"""
    platform: NotRequired[
        "capo_appstream.types.app_block_builder_platform_type.AppBlockBuilderPlatformType"
    ]
    """<p>The platform of the app block builder.</p> <p> <code>WINDOWS_SERVER_2019</code> is the only valid value.</p>"""
    instance_type: NotRequired["capo_appstream.types.string.String"]
    """<p>The instance type of the app block builder.</p>"""
    enable_default_internet_access: NotRequired[
        "capo_appstream.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether default internet access is enabled for the app block builder.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the IAM role that is applied to the app block builder.</p>"""
    vpc_config: NotRequired["capo_appstream.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the app block builder.</p>"""
    state: NotRequired[
        "capo_appstream.types.app_block_builder_state.AppBlockBuilderState"
    ]
    """<p>The state of the app block builder.</p>"""
    created_time: NotRequired["capo_appstream.types.timestamp.Timestamp"]
    """<p>The creation time of the app block builder.</p>"""
    app_block_builder_errors: NotRequired[
        "capo_appstream.types.resource_errors.ResourceErrors"
    ]
    """<p>The app block builder errors.</p>"""
    state_change_reason: NotRequired[
        "capo_appstream.types.app_block_builder_state_change_reason.AppBlockBuilderStateChangeReason"
    ]
    """<p>The state change reason.</p>"""
    access_endpoints: NotRequired[
        "capo_appstream.types.access_endpoint_list.AccessEndpointList"
    ]
    """<p>The list of interface VPC endpoint (interface endpoint) objects. Administrators can connect to the app block builder only through the specified endpoints.</p>"""
    disable_imdsv1: NotRequired["capo_appstream.types.boolean_object.BooleanObject"]
    """<p>Indicates whether Instance Metadata Service Version 1 (IMDSv1) is disabled for the app block builder.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppBlockBuilder) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "platform" in value:
        import capo_appstream.types.app_block_builder_platform_type

        out["Platform"] = (
            capo_appstream.types.app_block_builder_platform_type.serialize_aws_json_1_1(
                value["platform"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "state" in value:
        import capo_appstream.types.app_block_builder_state

        out["State"] = (
            capo_appstream.types.app_block_builder_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_aws_json_1_1(
            value["created_time"]
        )
    if "app_block_builder_errors" in value:
        import capo_appstream.types.resource_errors

        out["AppBlockBuilderErrors"] = (
            capo_appstream.types.resource_errors.serialize_aws_json_1_1(
                value["app_block_builder_errors"]
            )
        )
    if "state_change_reason" in value:
        import capo_appstream.types.app_block_builder_state_change_reason

        out["StateChangeReason"] = (
            capo_appstream.types.app_block_builder_state_change_reason.serialize_aws_json_1_1(
                value["state_change_reason"]
            )
        )
    if "access_endpoints" in value:
        import capo_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            capo_appstream.types.access_endpoint_list.serialize_aws_json_1_1(
                value["access_endpoints"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AppBlockBuilder:
    out: AppBlockBuilder = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Platform") is not None:
        import capo_appstream.types.app_block_builder_platform_type

        out["platform"] = (
            capo_appstream.types.app_block_builder_platform_type.deserialize_aws_json_1_1(
                data["Platform"]
            )
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("EnableDefaultInternetAccess") is not None:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("VpcConfig") is not None:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if data.get("State") is not None:
        import capo_appstream.types.app_block_builder_state

        out["state"] = (
            capo_appstream.types.app_block_builder_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedTime"]
        )
    if data.get("AppBlockBuilderErrors") is not None:
        import capo_appstream.types.resource_errors

        out["app_block_builder_errors"] = (
            capo_appstream.types.resource_errors.deserialize_aws_json_1_1(
                data["AppBlockBuilderErrors"]
            )
        )
    if data.get("StateChangeReason") is not None:
        import capo_appstream.types.app_block_builder_state_change_reason

        out["state_change_reason"] = (
            capo_appstream.types.app_block_builder_state_change_reason.deserialize_aws_json_1_1(
                data["StateChangeReason"]
            )
        )
    if data.get("AccessEndpoints") is not None:
        import capo_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_appstream.types.access_endpoint_list.deserialize_aws_json_1_1(
                data["AccessEndpoints"]
            )
        )
    if data.get("DisableIMDSV1") is not None:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AppBlockBuilder) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "platform" in value:
        import capo_appstream.types.app_block_builder_platform_type

        out["Platform"] = (
            capo_appstream.types.app_block_builder_platform_type.serialize_cbor(
                value["platform"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "enable_default_internet_access" in value:
        out["EnableDefaultInternetAccess"] = value["enable_default_internet_access"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "vpc_config" in value:
        import capo_appstream.types.vpc_config

        out["VpcConfig"] = capo_appstream.types.vpc_config.serialize_cbor(
            value["vpc_config"]
        )
    if "state" in value:
        import capo_appstream.types.app_block_builder_state

        out["State"] = capo_appstream.types.app_block_builder_state.serialize_cbor(
            value["state"]
        )
    if "created_time" in value:
        import capo_appstream.types.timestamp

        out["CreatedTime"] = capo_appstream.types.timestamp.serialize_cbor(
            value["created_time"]
        )
    if "app_block_builder_errors" in value:
        import capo_appstream.types.resource_errors

        out["AppBlockBuilderErrors"] = (
            capo_appstream.types.resource_errors.serialize_cbor(
                value["app_block_builder_errors"]
            )
        )
    if "state_change_reason" in value:
        import capo_appstream.types.app_block_builder_state_change_reason

        out["StateChangeReason"] = (
            capo_appstream.types.app_block_builder_state_change_reason.serialize_cbor(
                value["state_change_reason"]
            )
        )
    if "access_endpoints" in value:
        import capo_appstream.types.access_endpoint_list

        out["AccessEndpoints"] = (
            capo_appstream.types.access_endpoint_list.serialize_cbor(
                value["access_endpoints"]
            )
        )
    if "disable_imdsv1" in value:
        out["DisableIMDSV1"] = value["disable_imdsv1"]
    return out


def deserialize_cbor(data: dict) -> AppBlockBuilder:
    out: AppBlockBuilder = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Platform") is not None:
        import capo_appstream.types.app_block_builder_platform_type

        out["platform"] = (
            capo_appstream.types.app_block_builder_platform_type.deserialize_cbor(
                data["Platform"]
            )
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("EnableDefaultInternetAccess") is not None:
        out["enable_default_internet_access"] = data["EnableDefaultInternetAccess"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("VpcConfig") is not None:
        import capo_appstream.types.vpc_config

        out["vpc_config"] = capo_appstream.types.vpc_config.deserialize_cbor(
            data["VpcConfig"]
        )
    if data.get("State") is not None:
        import capo_appstream.types.app_block_builder_state

        out["state"] = capo_appstream.types.app_block_builder_state.deserialize_cbor(
            data["State"]
        )
    if data.get("CreatedTime") is not None:
        import capo_appstream.types.timestamp

        out["created_time"] = capo_appstream.types.timestamp.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("AppBlockBuilderErrors") is not None:
        import capo_appstream.types.resource_errors

        out["app_block_builder_errors"] = (
            capo_appstream.types.resource_errors.deserialize_cbor(
                data["AppBlockBuilderErrors"]
            )
        )
    if data.get("StateChangeReason") is not None:
        import capo_appstream.types.app_block_builder_state_change_reason

        out["state_change_reason"] = (
            capo_appstream.types.app_block_builder_state_change_reason.deserialize_cbor(
                data["StateChangeReason"]
            )
        )
    if data.get("AccessEndpoints") is not None:
        import capo_appstream.types.access_endpoint_list

        out["access_endpoints"] = (
            capo_appstream.types.access_endpoint_list.deserialize_cbor(
                data["AccessEndpoints"]
            )
        )
    if data.get("DisableIMDSV1") is not None:
        out["disable_imdsv1"] = data["DisableIMDSV1"]
    return out
