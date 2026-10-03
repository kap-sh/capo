"""Generated from Smithy shape ``com.amazonaws.workspaces#RegisterWorkspaceDirectoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.active_directory_config
    import capo_workspaces.types.arn
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.directory_id
    import capo_workspaces.types.microsoft_entra_config
    import capo_workspaces.types.subnet_ids
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.tenancy
    import capo_workspaces.types.user_identity_type
    import capo_workspaces.types.workspace_directory_description
    import capo_workspaces.types.workspace_directory_name
    import capo_workspaces.types.workspace_type


class RegisterWorkspaceDirectoryRequest(TypedDict, closed=True):
    directory_id: NotRequired["capo_workspaces.types.directory_id.DirectoryId"]
    """<p>The identifier of the directory. You cannot register a directory if it does not have a status of Active. If the directory does not have a status of Active, you will receive an InvalidResourceStateException error. If you have already registered the maximum number of directories that you can register with Amazon WorkSpaces, you will receive a ResourceLimitExceededException error. Deregister directories that you are not using for WorkSpaces, and try again.</p>"""
    subnet_ids: NotRequired["capo_workspaces.types.subnet_ids.SubnetIds"]
    """<p>The identifiers of the subnets for your virtual private cloud (VPC). Make sure that the subnets are in supported Availability Zones. The subnets must also be in separate Availability Zones. If these conditions are not met, you will receive an OperationNotSupportedException error.</p>"""
    enable_self_service: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether self-service capabilities are enabled or disabled.</p>"""
    tenancy: NotRequired["capo_workspaces.types.tenancy.Tenancy"]
    """<p>Indicates whether your WorkSpace directory is dedicated or shared. To use Bring Your Own License (BYOL) images, this value must be set to <code>DEDICATED</code> and your Amazon Web Services account must be enabled for BYOL. If your account has not been enabled for BYOL, you will receive an InvalidParameterValuesException error. For more information about BYOL images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html">Bring Your Own Windows Desktop Images</a>.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags associated with the directory.</p>"""
    workspace_directory_name: NotRequired[
        "capo_workspaces.types.workspace_directory_name.WorkspaceDirectoryName"
    ]
    """<p>The name of the directory to register.</p>"""
    workspace_directory_description: NotRequired[
        "capo_workspaces.types.workspace_directory_description.WorkspaceDirectoryDescription"
    ]
    """<p>Description of the directory to register.</p>"""
    user_identity_type: NotRequired[
        "capo_workspaces.types.user_identity_type.UserIdentityType"
    ]
    """<p>The type of identity management the user is using.</p>"""
    idc_instance_arn: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the identity center instance.</p>"""
    microsoft_entra_config: NotRequired[
        "capo_workspaces.types.microsoft_entra_config.MicrosoftEntraConfig"
    ]
    """<p>The details about Microsoft Entra config.</p>"""
    workspace_type: NotRequired["capo_workspaces.types.workspace_type.WorkspaceType"]
    """<p>Indicates whether the directory's WorkSpace type is personal or pools.</p>"""
    active_directory_config: NotRequired[
        "capo_workspaces.types.active_directory_config.ActiveDirectoryConfig"
    ]
    """<p>The active directory config of the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterWorkspaceDirectoryRequest) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "subnet_ids" in value:
        import capo_workspaces.types.subnet_ids

        out["SubnetIds"] = capo_workspaces.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "enable_self_service" in value:
        out["EnableSelfService"] = value["enable_self_service"]
    if "tenancy" in value:
        import capo_workspaces.types.tenancy

        out["Tenancy"] = capo_workspaces.types.tenancy.serialize_aws_json_1_1(
            value["tenancy"]
        )
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "workspace_directory_name" in value:
        out["WorkspaceDirectoryName"] = value["workspace_directory_name"]
    if "workspace_directory_description" in value:
        out["WorkspaceDirectoryDescription"] = value["workspace_directory_description"]
    if "user_identity_type" in value:
        import capo_workspaces.types.user_identity_type

        out["UserIdentityType"] = (
            capo_workspaces.types.user_identity_type.serialize_aws_json_1_1(
                value["user_identity_type"]
            )
        )
    if "idc_instance_arn" in value:
        out["IdcInstanceArn"] = value["idc_instance_arn"]
    if "microsoft_entra_config" in value:
        import capo_workspaces.types.microsoft_entra_config

        out["MicrosoftEntraConfig"] = (
            capo_workspaces.types.microsoft_entra_config.serialize_aws_json_1_1(
                value["microsoft_entra_config"]
            )
        )
    if "workspace_type" in value:
        import capo_workspaces.types.workspace_type

        out["WorkspaceType"] = (
            capo_workspaces.types.workspace_type.serialize_aws_json_1_1(
                value["workspace_type"]
            )
        )
    if "active_directory_config" in value:
        import capo_workspaces.types.active_directory_config

        out["ActiveDirectoryConfig"] = (
            capo_workspaces.types.active_directory_config.serialize_aws_json_1_1(
                value["active_directory_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterWorkspaceDirectoryRequest:
    out: RegisterWorkspaceDirectoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("SubnetIds") is not None:
        import capo_workspaces.types.subnet_ids

        out["subnet_ids"] = capo_workspaces.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("EnableSelfService") is not None:
        out["enable_self_service"] = data["EnableSelfService"]
    if data.get("Tenancy") is not None:
        import capo_workspaces.types.tenancy

        out["tenancy"] = capo_workspaces.types.tenancy.deserialize_aws_json_1_1(
            data["Tenancy"]
        )
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("WorkspaceDirectoryName") is not None:
        out["workspace_directory_name"] = data["WorkspaceDirectoryName"]
    if data.get("WorkspaceDirectoryDescription") is not None:
        out["workspace_directory_description"] = data["WorkspaceDirectoryDescription"]
    if data.get("UserIdentityType") is not None:
        import capo_workspaces.types.user_identity_type

        out["user_identity_type"] = (
            capo_workspaces.types.user_identity_type.deserialize_aws_json_1_1(
                data["UserIdentityType"]
            )
        )
    if data.get("IdcInstanceArn") is not None:
        out["idc_instance_arn"] = data["IdcInstanceArn"]
    if data.get("MicrosoftEntraConfig") is not None:
        import capo_workspaces.types.microsoft_entra_config

        out["microsoft_entra_config"] = (
            capo_workspaces.types.microsoft_entra_config.deserialize_aws_json_1_1(
                data["MicrosoftEntraConfig"]
            )
        )
    if data.get("WorkspaceType") is not None:
        import capo_workspaces.types.workspace_type

        out["workspace_type"] = (
            capo_workspaces.types.workspace_type.deserialize_aws_json_1_1(
                data["WorkspaceType"]
            )
        )
    if data.get("ActiveDirectoryConfig") is not None:
        import capo_workspaces.types.active_directory_config

        out["active_directory_config"] = (
            capo_workspaces.types.active_directory_config.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfig"]
            )
        )
    return out
