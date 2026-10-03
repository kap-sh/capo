"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationFsxWindowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.fsx_filesystem_arn
    import capo_datasync.types.fsx_windows_subdirectory
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.smb_domain
    import capo_datasync.types.smb_password
    import capo_datasync.types.smb_user


class CreateLocationFsxWindowsRequest(TypedDict, closed=True):
    subdirectory: NotRequired[
        "capo_datasync.types.fsx_windows_subdirectory.FsxWindowsSubdirectory"
    ]
    """<p>Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination location).</p>"""
    fsx_filesystem_arn: "capo_datasync.types.fsx_filesystem_arn.FsxFilesystemArn"
    """<p>Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file system.</p>"""
    security_group_arns: (
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    )
    """<p>Specifies the ARNs of the Amazon EC2 security groups that provide access to your file system's preferred subnet.</p> <p>The security groups that you specify must be able to communicate with your file system's security groups. For information about configuring security groups for file system access, see the <a href="https://docs.aws.amazon.com/fsx/latest/WindowsGuide/limit-access-security-groups.html"> <i>Amazon FSx for Windows File Server User Guide</i> </a>.</p> <note> <p>If you choose a security group that doesn't allow connections from within itself, do one of the following:</p> <ul> <li> <p>Configure the security group to allow it to communicate within itself.</p> </li> <li> <p>Choose a different security group that can communicate with the mount target's security group.</p> </li> </ul> </note>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>"""
    user: "capo_datasync.types.smb_user.SmbUser"
    """<p>Specifies the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions">required permissions</a> for FSx for Windows File Server locations.</p>"""
    domain: NotRequired["capo_datasync.types.smb_domain.SmbDomain"]
    """<p>Specifies the name of the Windows domain that the FSx for Windows File Server file system belongs to.</p> <p>If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.</p>"""
    password: NotRequired["capo_datasync.types.smb_password.SmbPassword"]
    """<p>Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, which includes the password that DataSync uses to access a specific FSx Windows storage location, with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationFsxWindows</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the <code>Password</code> you specify for to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>Password</code>) or <code>CustomSecretConfig</code> (without <code>Password</code>) to provide credentials for a <code>CreateLocationFsxWindows</code> request. Do not provide both parameters for the same request.</p> </note>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed Secrets Manager secret where the password for an FSx for Windows File Server storage location is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>Password</code>) or <code>CustomSecretConfig</code> (without <code>Password</code>) to provide credentials for a <code>CreateLocationFsxWindows</code> request. Do not provide both parameters for the same request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationFsxWindowsRequest) -> dict:
    out: dict = {}
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    out["FsxFilesystemArn"] = value["fsx_filesystem_arn"]
    import capo_datasync.types.ec2_security_group_arn_list

    out["SecurityGroupArns"] = (
        capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
            value["security_group_arns"]
        )
    )
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    out["User"] = value["user"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "password" in value:
        out["Password"] = value["password"]
    if "cmk_secret_config" in value:
        import capo_datasync.types.cmk_secret_config

        out["CmkSecretConfig"] = (
            capo_datasync.types.cmk_secret_config.serialize_aws_json_1_1(
                value["cmk_secret_config"]
            )
        )
    if "custom_secret_config" in value:
        import capo_datasync.types.custom_secret_config

        out["CustomSecretConfig"] = (
            capo_datasync.types.custom_secret_config.serialize_aws_json_1_1(
                value["custom_secret_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationFsxWindowsRequest:
    out: CreateLocationFsxWindowsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("FsxFilesystemArn") is not None:
        out["fsx_filesystem_arn"] = data["FsxFilesystemArn"]
    else:
        raise DeserializationError(
            "CreateLocationFsxWindowsRequest.fsx_filesystem_arn required"
        )
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLocationFsxWindowsRequest.security_group_arns required"
        )
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("User") is not None:
        out["user"] = data["User"]
    else:
        raise DeserializationError("CreateLocationFsxWindowsRequest.user required")
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("CmkSecretConfig") is not None:
        import capo_datasync.types.cmk_secret_config

        out["cmk_secret_config"] = (
            capo_datasync.types.cmk_secret_config.deserialize_aws_json_1_1(
                data["CmkSecretConfig"]
            )
        )
    if data.get("CustomSecretConfig") is not None:
        import capo_datasync.types.custom_secret_config

        out["custom_secret_config"] = (
            capo_datasync.types.custom_secret_config.deserialize_aws_json_1_1(
                data["CustomSecretConfig"]
            )
        )
    return out
