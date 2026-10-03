"""Generated from Smithy shape ``com.amazonaws.datasync#FsxUpdateProtocolSmb``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.smb_mount_options
    import capo_datasync.types.smb_password
    import capo_datasync.types.smb_user
    import capo_datasync.types.update_smb_domain


class FsxUpdateProtocolSmb(TypedDict, closed=True):
    domain: NotRequired["capo_datasync.types.update_smb_domain.UpdateSmbDomain"]
    """<p>Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs to.</p> <p>If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right SVM.</p>"""
    mount_options: NotRequired["capo_datasync.types.smb_mount_options.SmbMountOptions"]
    password: NotRequired["capo_datasync.types.smb_password.SmbPassword"]
    """<p>Specifies the password of a user who has permission to access your SVM.</p>"""
    user: NotRequired["capo_datasync.types.smb_user.SmbUser"]
    """<p>Specifies a user that can mount and access the files, folders, and metadata in your SVM.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb">Using the SMB protocol</a>.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, such as a <code>Password</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed secret, such as a <code>Password</code> or set of credentials that DataSync uses to access a specific transfer location. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxUpdateProtocolSmb) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "mount_options" in value:
        import capo_datasync.types.smb_mount_options

        out["MountOptions"] = (
            capo_datasync.types.smb_mount_options.serialize_aws_json_1_1(
                value["mount_options"]
            )
        )
    if "password" in value:
        out["Password"] = value["password"]
    if "user" in value:
        out["User"] = value["user"]
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


def deserialize_aws_json_1_1(data: dict) -> FsxUpdateProtocolSmb:
    out: FsxUpdateProtocolSmb = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("MountOptions") is not None:
        import capo_datasync.types.smb_mount_options

        out["mount_options"] = (
            capo_datasync.types.smb_mount_options.deserialize_aws_json_1_1(
                data["MountOptions"]
            )
        )
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("User") is not None:
        out["user"] = data["User"]
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
