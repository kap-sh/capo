"""Generated from Smithy shape ``com.amazonaws.datasync#FsxProtocolSmb``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.managed_secret_config
    import capo_datasync.types.smb_domain
    import capo_datasync.types.smb_mount_options
    import capo_datasync.types.smb_password
    import capo_datasync.types.smb_user


class FsxProtocolSmb(TypedDict, closed=True):
    domain: NotRequired["capo_datasync.types.smb_domain.SmbDomain"]
    """<p>Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs to.</p> <p>If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SVM.</p> <p>If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right SVM.</p>"""
    mount_options: NotRequired["capo_datasync.types.smb_mount_options.SmbMountOptions"]
    password: "capo_datasync.types.smb_password.SmbPassword"
    """<p>Specifies the password of a user who has permission to access your SVM.</p>"""
    user: "capo_datasync.types.smb_user.SmbUser"
    """<p>Specifies a user that can mount and access the files, folders, and metadata in your SVM.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb">Using the SMB protocol</a>.</p>"""
    managed_secret_config: NotRequired[
        "capo_datasync.types.managed_secret_config.ManagedSecretConfig"
    ]
    """<p>Describes configuration information for a DataSync-managed secret, such as a <code>Password</code> that DataSync uses to access a specific storage location. DataSync uses the default Amazon Web Services-managed KMS key to encrypt this secret in Secrets Manager.</p> <note> <p>Do not provide this for a <code>CreateLocation</code> request. <code>ManagedSecretConfig</code> is a ReadOnly property and is only be populated in the <code>DescribeLocation</code> response.</p> </note>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, which includes the password that DataSync uses to access a specific FSx for ONTAP storage location (using SMB), with a customer-managed KMS key.</p> <p>When you include this parameter as part of a <code>CreateLocationFsxOntap</code> request, you provide only the KMS key ARN. DataSync uses this KMS key together with the <code>Password</code> you specify for to create a DataSync-managed secret to store the location access credentials.</p> <p>Make sure that DataSync has permission to access the KMS key that you specify. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key"> Using a service-managed secret encrypted with a custom KMS key</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>Password</code>) or <code>CustomSecretConfig</code> (without <code>Password</code>) to provide credentials for a <code>CreateLocationFsxOntap</code> request. Do not provide both parameters for the same request.</p> </note>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed Secrets Manager secret where the password for an FSx for ONTAP storage location (using SMB) is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key"> Using a secret that you manage</a>.</p> <note> <p>You can use either <code>CmkSecretConfig</code> (with <code>Password</code>) or <code>CustomSecretConfig</code> (without <code>Password</code>) to provide credentials for a <code>CreateLocationFsxOntap</code> request. Do not provide both parameters for the same request.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FsxProtocolSmb) -> dict:
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
    out["Password"] = value.get("password", "")
    out["User"] = value["user"]
    if "managed_secret_config" in value:
        import capo_datasync.types.managed_secret_config

        out["ManagedSecretConfig"] = (
            capo_datasync.types.managed_secret_config.serialize_aws_json_1_1(
                value["managed_secret_config"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> FsxProtocolSmb:
    out: FsxProtocolSmb = {}  # type: ignore[typeddict-item]
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
    else:
        out["password"] = ""
    if data.get("User") is not None:
        out["user"] = data["User"]
    else:
        raise DeserializationError("FsxProtocolSmb.user required")
    if data.get("ManagedSecretConfig") is not None:
        import capo_datasync.types.managed_secret_config

        out["managed_secret_config"] = (
            capo_datasync.types.managed_secret_config.deserialize_aws_json_1_1(
                data["ManagedSecretConfig"]
            )
        )
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
