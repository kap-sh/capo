"""Generated from Smithy shape ``com.amazonaws.ecs#EFSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.efs_authorization_config
    import capo_ecs.types.efs_transit_encryption
    import capo_ecs.types.string


class EFSVolumeConfiguration(TypedDict, closed=True):
    file_system_id: "capo_ecs.types.string.String"
    """<p>The Amazon EFS file system ID to use.</p>"""
    root_directory: NotRequired["capo_ecs.types.string.String"]
    """<p>The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume will be used. Specifying <code>/</code> will have the same effect as omitting this parameter.</p> <important> <p>If an EFS access point is specified in the <code>authorizationConfig</code>, the root directory parameter must either be omitted or set to <code>/</code> which will enforce the path set on the EFS access point.</p> </important>"""
    transit_encryption: NotRequired[
        "capo_ecs.types.efs_transit_encryption.EFSTransitEncryption"
    ]
    """<p>Determines whether to use encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be turned on if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of <code>DISABLED</code> is used. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html">Encrypting data in transit</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    transit_encryption_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon EFS mount helper uses. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html">EFS mount helper</a> in the <i>Amazon Elastic File System User Guide</i>.</p>"""
    authorization_config: NotRequired[
        "capo_ecs.types.efs_authorization_config.EFSAuthorizationConfig"
    ]
    """<p>The authorization configuration details for the Amazon EFS file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EFSVolumeConfiguration) -> dict:
    out: dict = {}
    out["fileSystemId"] = value["file_system_id"]
    if "root_directory" in value:
        out["rootDirectory"] = value["root_directory"]
    if "transit_encryption" in value:
        import capo_ecs.types.efs_transit_encryption

        out["transitEncryption"] = (
            capo_ecs.types.efs_transit_encryption.serialize_aws_json_1_1(
                value["transit_encryption"]
            )
        )
    if "transit_encryption_port" in value:
        out["transitEncryptionPort"] = value["transit_encryption_port"]
    if "authorization_config" in value:
        import capo_ecs.types.efs_authorization_config

        out["authorizationConfig"] = (
            capo_ecs.types.efs_authorization_config.serialize_aws_json_1_1(
                value["authorization_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EFSVolumeConfiguration:
    out: EFSVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemId") is not None:
        out["file_system_id"] = data["fileSystemId"]
    else:
        raise DeserializationError("EFSVolumeConfiguration.file_system_id required")
    if data.get("rootDirectory") is not None:
        out["root_directory"] = data["rootDirectory"]
    if data.get("transitEncryption") is not None:
        import capo_ecs.types.efs_transit_encryption

        out["transit_encryption"] = (
            capo_ecs.types.efs_transit_encryption.deserialize_aws_json_1_1(
                data["transitEncryption"]
            )
        )
    if data.get("transitEncryptionPort") is not None:
        out["transit_encryption_port"] = data["transitEncryptionPort"]
    if data.get("authorizationConfig") is not None:
        import capo_ecs.types.efs_authorization_config

        out["authorization_config"] = (
            capo_ecs.types.efs_authorization_config.deserialize_aws_json_1_1(
                data["authorizationConfig"]
            )
        )
    return out
