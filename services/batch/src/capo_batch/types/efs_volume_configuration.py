"""Generated from Smithy shape ``com.amazonaws.batch#EFSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.efs_authorization_config
    import capo_batch.types.efs_transit_encryption
    import capo_batch.types.integer
    import capo_batch.types.string


class EFSVolumeConfiguration(TypedDict, closed=True):
    file_system_id: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon EFS file system ID to use.</p>"""
    root_directory: NotRequired["capo_batch.types.string.String"]
    """<p>The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying <code>/</code> has the same effect as omitting this parameter. The maximum length is 4,096 characters.</p> <important> <p>If an EFS access point is specified in the <code>authorizationConfig</code>, the root directory parameter must either be omitted or set to <code>/</code>, which enforces the path set on the Amazon EFS access point.</p> </important>"""
    transit_encryption: NotRequired[
        "capo_batch.types.efs_transit_encryption.EFSTransitEncryption"
    ]
    """<p>Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of <code>DISABLED</code> is used. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html">Encrypting data in transit</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    transit_encryption_port: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html">EFS mount helper</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    authorization_config: NotRequired[
        "capo_batch.types.efs_authorization_config.EFSAuthorizationConfig"
    ]
    """<p>The authorization configuration details for the Amazon EFS file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EFSVolumeConfiguration) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["fileSystemId"] = value["file_system_id"]
    if "root_directory" in value:
        out["rootDirectory"] = value["root_directory"]
    if "transit_encryption" in value:
        import capo_batch.types.efs_transit_encryption

        out["transitEncryption"] = (
            capo_batch.types.efs_transit_encryption.serialize_json(
                value["transit_encryption"]
            )
        )
    if "transit_encryption_port" in value:
        out["transitEncryptionPort"] = value["transit_encryption_port"]
    if "authorization_config" in value:
        import capo_batch.types.efs_authorization_config

        out["authorizationConfig"] = (
            capo_batch.types.efs_authorization_config.serialize_json(
                value["authorization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> EFSVolumeConfiguration:
    out: EFSVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    if data.get("rootDirectory") is not None:
        out["root_directory"] = data["rootDirectory"]
    if data.get("transitEncryption") is not None:
        import capo_batch.types.efs_transit_encryption

        out["transit_encryption"] = (
            capo_batch.types.efs_transit_encryption.deserialize_json(
                data["transitEncryption"]
            )
        )
    if data.get("transitEncryptionPort") is not None:
        out["transit_encryption_port"] = data["transitEncryptionPort"]
    if data.get("authorizationConfig") is not None:
        import capo_batch.types.efs_authorization_config

        out["authorization_config"] = (
            capo_batch.types.efs_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    return out
