"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileCacheRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.copy_tags_to_data_repository_associations
    import capo_fsx.types.create_file_cache_data_repository_associations
    import capo_fsx.types.create_file_cache_lustre_configuration
    import capo_fsx.types.file_cache_type
    import capo_fsx.types.file_system_type_version
    import capo_fsx.types.kms_key_id
    import capo_fsx.types.security_group_ids
    import capo_fsx.types.storage_capacity
    import capo_fsx.types.subnet_ids
    import capo_fsx.types.tags


class CreateFileCacheRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    """<p>An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.</p> <p>By using the idempotent operation, you can retry a <code>CreateFileCache</code> operation without the risk of creating an extra cache. This approach can be useful when an initial call fails in a way that makes it unclear whether a cache was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a cache, the client receives success as long as the parameters are the same.</p>"""
    file_cache_type: NotRequired["capo_fsx.types.file_cache_type.FileCacheType"]
    """<p>The type of cache that you're creating, which must be <code>LUSTRE</code>.</p>"""
    file_cache_type_version: NotRequired[
        "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>Sets the Lustre version for the cache that you're creating, which must be <code>2.12</code>.</p>"""
    storage_capacity: NotRequired["capo_fsx.types.storage_capacity.StorageCapacity"]
    """<p>The storage capacity of the cache in gibibytes (GiB). Valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.</p>"""
    subnet_ids: NotRequired["capo_fsx.types.subnet_ids.SubnetIds"]
    security_group_ids: NotRequired[
        "capo_fsx.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of IDs specifying the security groups to apply to all network interfaces created for Amazon File Cache access. This list isn't returned in later requests to describe the cache.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    copy_tags_to_data_repository_associations: NotRequired[
        "capo_fsx.types.copy_tags_to_data_repository_associations.CopyTagsToDataRepositoryAssociations"
    ]
    """<p>A boolean flag indicating whether tags for the cache should be copied to data repository associations. This value defaults to false.</p>"""
    kms_key_id: NotRequired["capo_fsx.types.kms_key_id.KmsKeyId"]
    """<p>Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on an Amazon File Cache. If a <code>KmsKeyId</code> isn't specified, the Amazon FSx-managed KMS key for your account is used. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html">Encrypt</a> in the <i>Key Management Service API Reference</i>.</p>"""
    lustre_configuration: NotRequired[
        "capo_fsx.types.create_file_cache_lustre_configuration.CreateFileCacheLustreConfiguration"
    ]
    """<p>The configuration for the Amazon File Cache resource being created.</p>"""
    data_repository_associations: NotRequired[
        "capo_fsx.types.create_file_cache_data_repository_associations.CreateFileCacheDataRepositoryAssociations"
    ]
    """<p>A list of up to 8 configurations for data repository associations (DRAs) to be created during the cache creation. The DRAs link the cache to either an Amazon S3 data repository or a Network File System (NFS) data repository that supports the NFSv3 protocol.</p> <p>The DRA configurations must meet the following requirements:</p> <ul> <li> <p>All configurations on the list must be of the same data repository type, either all S3 or all NFS. A cache can't link to different data repository types at the same time.</p> </li> <li> <p>An NFS DRA must link to an NFS file system that supports the NFSv3 protocol.</p> </li> </ul> <p>DRA automatic import and automatic export is not supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileCacheRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_cache_type" in value:
        import capo_fsx.types.file_cache_type

        out["FileCacheType"] = capo_fsx.types.file_cache_type.serialize_aws_json_1_1(
            value["file_cache_type"]
        )
    if "file_cache_type_version" in value:
        out["FileCacheTypeVersion"] = value["file_cache_type_version"]
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    if "subnet_ids" in value:
        import capo_fsx.types.subnet_ids

        out["SubnetIds"] = capo_fsx.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_fsx.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_fsx.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "copy_tags_to_data_repository_associations" in value:
        out["CopyTagsToDataRepositoryAssociations"] = value[
            "copy_tags_to_data_repository_associations"
        ]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "lustre_configuration" in value:
        import capo_fsx.types.create_file_cache_lustre_configuration

        out["LustreConfiguration"] = (
            capo_fsx.types.create_file_cache_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "data_repository_associations" in value:
        import capo_fsx.types.create_file_cache_data_repository_associations

        out["DataRepositoryAssociations"] = (
            capo_fsx.types.create_file_cache_data_repository_associations.serialize_aws_json_1_1(
                value["data_repository_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileCacheRequest:
    out: CreateFileCacheRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("FileCacheType") is not None:
        import capo_fsx.types.file_cache_type

        out["file_cache_type"] = (
            capo_fsx.types.file_cache_type.deserialize_aws_json_1_1(
                data["FileCacheType"]
            )
        )
    if data.get("FileCacheTypeVersion") is not None:
        out["file_cache_type_version"] = data["FileCacheTypeVersion"]
    if data.get("StorageCapacity") is not None:
        out["storage_capacity"] = data["StorageCapacity"]
    if data.get("SubnetIds") is not None:
        import capo_fsx.types.subnet_ids

        out["subnet_ids"] = capo_fsx.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("SecurityGroupIds") is not None:
        import capo_fsx.types.security_group_ids

        out["security_group_ids"] = (
            capo_fsx.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CopyTagsToDataRepositoryAssociations") is not None:
        out["copy_tags_to_data_repository_associations"] = data[
            "CopyTagsToDataRepositoryAssociations"
        ]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("LustreConfiguration") is not None:
        import capo_fsx.types.create_file_cache_lustre_configuration

        out["lustre_configuration"] = (
            capo_fsx.types.create_file_cache_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if data.get("DataRepositoryAssociations") is not None:
        import capo_fsx.types.create_file_cache_data_repository_associations

        out["data_repository_associations"] = (
            capo_fsx.types.create_file_cache_data_repository_associations.deserialize_aws_json_1_1(
                data["DataRepositoryAssociations"]
            )
        )
    return out
