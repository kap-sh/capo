"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationFsxWindowsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.cmk_secret_config
    import capo_datasync.types.custom_secret_config
    import capo_datasync.types.fsx_windows_subdirectory
    import capo_datasync.types.location_arn
    import capo_datasync.types.smb_password
    import capo_datasync.types.smb_user
    import capo_datasync.types.update_smb_domain


class UpdateLocationFsxWindowsRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the ARN of the FSx for Windows File Server transfer location that you're updating.</p>"""
    subdirectory: NotRequired[
        "capo_datasync.types.fsx_windows_subdirectory.FsxWindowsSubdirectory"
    ]
    """<p>Specifies a mount path for your file system using forward slashes. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>"""
    domain: NotRequired["capo_datasync.types.update_smb_domain.UpdateSmbDomain"]
    """<p>Specifies the name of the Windows domain that your FSx for Windows File Server file system belongs to.</p> <p>If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right file system.</p>"""
    user: NotRequired["capo_datasync.types.smb_user.SmbUser"]
    """<p>Specifies the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p> <p>For information about choosing a user with the right level of access for your transfer, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions">required permissions</a> for FSx for Windows File Server locations.</p>"""
    password: NotRequired["capo_datasync.types.smb_password.SmbPassword"]
    """<p>Specifies the password of the user with the permissions to mount and access the files, folders, and file metadata in your FSx for Windows File Server file system.</p>"""
    cmk_secret_config: NotRequired[
        "capo_datasync.types.cmk_secret_config.CmkSecretConfig"
    ]
    """<p>Specifies configuration information for a DataSync-managed secret, such as a <code>Password</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed KMS key.</p>"""
    custom_secret_config: NotRequired[
        "capo_datasync.types.custom_secret_config.CustomSecretConfig"
    ]
    """<p>Specifies configuration information for a customer-managed secret, such as a <code>Password</code> or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed Identity and Access Management (IAM) role that provides access to the secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationFsxWindowsRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "user" in value:
        out["User"] = value["user"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationFsxWindowsRequest:
    out: UpdateLocationFsxWindowsRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "UpdateLocationFsxWindowsRequest.location_arn required"
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("User") is not None:
        out["user"] = data["User"]
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
