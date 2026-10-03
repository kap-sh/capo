"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheCreating``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.aws_account_id
    import capo_fsx.types.copy_tags_to_data_repository_associations
    import capo_fsx.types.creation_time
    import capo_fsx.types.data_repository_association_ids
    import capo_fsx.types.dns_name
    import capo_fsx.types.file_cache_failure_details
    import capo_fsx.types.file_cache_id
    import capo_fsx.types.file_cache_lifecycle
    import capo_fsx.types.file_cache_lustre_configuration
    import capo_fsx.types.file_cache_type
    import capo_fsx.types.file_system_type_version
    import capo_fsx.types.kms_key_id
    import capo_fsx.types.network_interface_ids
    import capo_fsx.types.resource_arn
    import capo_fsx.types.storage_capacity
    import capo_fsx.types.subnet_ids
    import capo_fsx.types.tags
    import capo_fsx.types.vpc_id


class FileCacheCreating(TypedDict, closed=True):
    owner_id: NotRequired["capo_fsx.types.aws_account_id.AWSAccountId"]
    creation_time: NotRequired["capo_fsx.types.creation_time.CreationTime"]
    file_cache_id: NotRequired["capo_fsx.types.file_cache_id.FileCacheId"]
    """<p>The system-generated, unique ID of the cache.</p>"""
    file_cache_type: NotRequired["capo_fsx.types.file_cache_type.FileCacheType"]
    """<p>The type of cache, which must be <code>LUSTRE</code>.</p>"""
    file_cache_type_version: NotRequired[
        "capo_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>The Lustre version of the cache, which must be <code>2.12</code>.</p>"""
    lifecycle: NotRequired["capo_fsx.types.file_cache_lifecycle.FileCacheLifecycle"]
    """<p>The lifecycle status of the cache. The following are the possible values and what they mean:</p> <ul> <li> <p> <code>AVAILABLE</code> - The cache is in a healthy state, and is reachable and available for use.</p> </li> <li> <p> <code>CREATING</code> - The new cache is being created.</p> </li> <li> <p> <code>DELETING</code> - An existing cache is being deleted.</p> </li> <li> <p> <code>UPDATING</code> - The cache is undergoing a customer-initiated update.</p> </li> <li> <p> <code>FAILED</code> - An existing cache has experienced an unrecoverable failure. When creating a new cache, the cache was unable to be created.</p> </li> </ul>"""
    failure_details: NotRequired[
        "capo_fsx.types.file_cache_failure_details.FileCacheFailureDetails"
    ]
    """<p>A structure providing details of any failures that occurred in creating a cache.</p>"""
    storage_capacity: NotRequired["capo_fsx.types.storage_capacity.StorageCapacity"]
    """<p>The storage capacity of the cache in gibibytes (GiB).</p>"""
    vpc_id: NotRequired["capo_fsx.types.vpc_id.VpcId"]
    subnet_ids: NotRequired["capo_fsx.types.subnet_ids.SubnetIds"]
    network_interface_ids: NotRequired[
        "capo_fsx.types.network_interface_ids.NetworkInterfaceIds"
    ]
    dns_name: NotRequired["capo_fsx.types.dns_name.DNSName"]
    """<p>The Domain Name System (DNS) name for the cache.</p>"""
    kms_key_id: NotRequired["capo_fsx.types.kms_key_id.KmsKeyId"]
    """<p>Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on an Amazon File Cache. If a <code>KmsKeyId</code> isn't specified, the Amazon FSx-managed KMS key for your account is used. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html">Encrypt</a> in the <i>Key Management Service API Reference</i>.</p>"""
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    copy_tags_to_data_repository_associations: NotRequired[
        "capo_fsx.types.copy_tags_to_data_repository_associations.CopyTagsToDataRepositoryAssociations"
    ]
    """<p>A boolean flag indicating whether tags for the cache should be copied to data repository associations.</p>"""
    lustre_configuration: NotRequired[
        "capo_fsx.types.file_cache_lustre_configuration.FileCacheLustreConfiguration"
    ]
    """<p>The configuration for the Amazon File Cache resource.</p>"""
    data_repository_association_ids: NotRequired[
        "capo_fsx.types.data_repository_association_ids.DataRepositoryAssociationIds"
    ]
    """<p>A list of IDs of data repository associations that are associated with this cache.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheCreating) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "creation_time" in value:
        import capo_fsx.types.creation_time

        out["CreationTime"] = capo_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "file_cache_type" in value:
        import capo_fsx.types.file_cache_type

        out["FileCacheType"] = capo_fsx.types.file_cache_type.serialize_aws_json_1_1(
            value["file_cache_type"]
        )
    if "file_cache_type_version" in value:
        out["FileCacheTypeVersion"] = value["file_cache_type_version"]
    if "lifecycle" in value:
        import capo_fsx.types.file_cache_lifecycle

        out["Lifecycle"] = capo_fsx.types.file_cache_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "failure_details" in value:
        import capo_fsx.types.file_cache_failure_details

        out["FailureDetails"] = (
            capo_fsx.types.file_cache_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import capo_fsx.types.subnet_ids

        out["SubnetIds"] = capo_fsx.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "network_interface_ids" in value:
        import capo_fsx.types.network_interface_ids

        out["NetworkInterfaceIds"] = (
            capo_fsx.types.network_interface_ids.serialize_aws_json_1_1(
                value["network_interface_ids"]
            )
        )
    if "dns_name" in value:
        out["DNSName"] = value["dns_name"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "copy_tags_to_data_repository_associations" in value:
        out["CopyTagsToDataRepositoryAssociations"] = value[
            "copy_tags_to_data_repository_associations"
        ]
    if "lustre_configuration" in value:
        import capo_fsx.types.file_cache_lustre_configuration

        out["LustreConfiguration"] = (
            capo_fsx.types.file_cache_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "data_repository_association_ids" in value:
        import capo_fsx.types.data_repository_association_ids

        out["DataRepositoryAssociationIds"] = (
            capo_fsx.types.data_repository_association_ids.serialize_aws_json_1_1(
                value["data_repository_association_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheCreating:
    out: FileCacheCreating = {}  # type: ignore[typeddict-item]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("CreationTime") is not None:
        import capo_fsx.types.creation_time

        out["creation_time"] = capo_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("FileCacheId") is not None:
        out["file_cache_id"] = data["FileCacheId"]
    if data.get("FileCacheType") is not None:
        import capo_fsx.types.file_cache_type

        out["file_cache_type"] = (
            capo_fsx.types.file_cache_type.deserialize_aws_json_1_1(
                data["FileCacheType"]
            )
        )
    if data.get("FileCacheTypeVersion") is not None:
        out["file_cache_type_version"] = data["FileCacheTypeVersion"]
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.file_cache_lifecycle

        out["lifecycle"] = capo_fsx.types.file_cache_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if data.get("FailureDetails") is not None:
        import capo_fsx.types.file_cache_failure_details

        out["failure_details"] = (
            capo_fsx.types.file_cache_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if data.get("StorageCapacity") is not None:
        out["storage_capacity"] = data["StorageCapacity"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetIds") is not None:
        import capo_fsx.types.subnet_ids

        out["subnet_ids"] = capo_fsx.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if data.get("NetworkInterfaceIds") is not None:
        import capo_fsx.types.network_interface_ids

        out["network_interface_ids"] = (
            capo_fsx.types.network_interface_ids.deserialize_aws_json_1_1(
                data["NetworkInterfaceIds"]
            )
        )
    if data.get("DNSName") is not None:
        out["dns_name"] = data["DNSName"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CopyTagsToDataRepositoryAssociations") is not None:
        out["copy_tags_to_data_repository_associations"] = data[
            "CopyTagsToDataRepositoryAssociations"
        ]
    if data.get("LustreConfiguration") is not None:
        import capo_fsx.types.file_cache_lustre_configuration

        out["lustre_configuration"] = (
            capo_fsx.types.file_cache_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if data.get("DataRepositoryAssociationIds") is not None:
        import capo_fsx.types.data_repository_association_ids

        out["data_repository_association_ids"] = (
            capo_fsx.types.data_repository_association_ids.deserialize_aws_json_1_1(
                data["DataRepositoryAssociationIds"]
            )
        )
    return out
