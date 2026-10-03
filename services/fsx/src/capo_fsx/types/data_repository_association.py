"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.archive_path
    import capo_fsx.types.batch_import_meta_data_on_create
    import capo_fsx.types.creation_time
    import capo_fsx.types.data_repository_association_id
    import capo_fsx.types.data_repository_failure_details
    import capo_fsx.types.data_repository_lifecycle
    import capo_fsx.types.file_cache_id
    import capo_fsx.types.file_system_id
    import capo_fsx.types.megabytes
    import capo_fsx.types.namespace
    import capo_fsx.types.nfs_data_repository_configuration
    import capo_fsx.types.resource_arn
    import capo_fsx.types.s3_data_repository_configuration
    import capo_fsx.types.sub_directories_paths
    import capo_fsx.types.tags


class DataRepositoryAssociation(TypedDict, closed=True):
    association_id: NotRequired[
        "capo_fsx.types.data_repository_association_id.DataRepositoryAssociationId"
    ]
    """<p>The system-generated, unique ID of the data repository association.</p>"""
    resource_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    lifecycle: NotRequired[
        "capo_fsx.types.data_repository_lifecycle.DataRepositoryLifecycle"
    ]
    """<p>Describes the state of a data repository association. The lifecycle can have the following values:</p> <ul> <li> <p> <code>CREATING</code> - The data repository association between the file system or cache and the data repository is being created. The data repository is unavailable.</p> </li> <li> <p> <code>AVAILABLE</code> - The data repository association is available for use.</p> </li> <li> <p> <code>MISCONFIGURED</code> - The data repository association is misconfigured. Until the configuration is corrected, automatic import and automatic export will not work (only for Amazon FSx for Lustre).</p> </li> <li> <p> <code>UPDATING</code> - The data repository association is undergoing a customer initiated update that might affect its availability.</p> </li> <li> <p> <code>DELETING</code> - The data repository association is undergoing a customer initiated deletion.</p> </li> <li> <p> <code>FAILED</code> - The data repository association is in a terminal state that cannot be recovered.</p> </li> </ul>"""
    failure_details: NotRequired[
        "capo_fsx.types.data_repository_failure_details.DataRepositoryFailureDetails"
    ]
    file_system_path: NotRequired["capo_fsx.types.namespace.Namespace"]
    """<p>A path on the Amazon FSx for Lustre file system that points to a high-level directory (such as <code>/ns1/</code>) or subdirectory (such as <code>/ns1/subdir/</code>) that will be mapped 1-1 with <code>DataRepositoryPath</code>. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path <code>/ns1/</code>, then you cannot link another data repository with file system path <code>/ns1/ns2</code>.</p> <p>This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.</p> <note> <p>If you specify only a forward slash (<code>/</code>) as the file system path, you can link only one data repository to the file system. You can only specify "/" as the file system path for the first data repository associated with a file system.</p> </note>"""
    data_repository_path: NotRequired["capo_fsx.types.archive_path.ArchivePath"]
    """<p>The path to the data repository that will be linked to the cache or file system.</p> <ul> <li> <p>For Amazon File Cache, the path can be an NFS data repository that will be linked to the cache. The path can be in one of two formats:</p> <ul> <li> <p>If you are not using the <code>DataRepositorySubdirectories</code> parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format <code>nsf://nfs-domain-name/exportpath</code>. You can therefore link a single NFS Export to a single data repository association.</p> </li> <li> <p>If you are using the <code>DataRepositorySubdirectories</code> parameter, the path is the domain name of the NFS file system in the format <code>nfs://filer-domain-name</code>, which indicates the root of the subdirectories specified with the <code>DataRepositorySubdirectories</code> parameter.</p> </li> </ul> </li> <li> <p>For Amazon File Cache, the path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix/</code> (where <code>prefix</code> is optional).</p> </li> <li> <p>For Amazon FSx for Lustre, the path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix/</code> (where <code>prefix</code> is optional).</p> </li> </ul>"""
    batch_import_meta_data_on_create: NotRequired[
        "capo_fsx.types.batch_import_meta_data_on_create.BatchImportMetaDataOnCreate"
    ]
    """<p>A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to <code>true</code>.</p> <note> <p> <code>BatchImportMetaDataOnCreate</code> is not supported for data repositories linked to an Amazon File Cache resource.</p> </note>"""
    imported_file_chunk_size: NotRequired["capo_fsx.types.megabytes.Megabytes"]
    """<p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system or cache.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p>"""
    s3: NotRequired[
        "capo_fsx.types.s3_data_repository_configuration.S3DataRepositoryConfiguration"
    ]
    """<p>The configuration for an Amazon S3 data repository linked to an Amazon FSx for Lustre file system with a data repository association.</p>"""
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    creation_time: NotRequired["capo_fsx.types.creation_time.CreationTime"]
    file_cache_id: NotRequired["capo_fsx.types.file_cache_id.FileCacheId"]
    """<p>The globally unique ID of the Amazon File Cache resource.</p>"""
    file_cache_path: NotRequired["capo_fsx.types.namespace.Namespace"]
    """<p>A path on the Amazon File Cache that points to a high-level directory (such as <code>/ns1/</code>) or subdirectory (such as <code>/ns1/subdir/</code>) that will be mapped 1-1 with <code>DataRepositoryPath</code>. The leading forward slash in the path is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path <code>/ns1/</code>, then you cannot link another data repository with cache path <code>/ns1/ns2</code>.</p> <p>This path specifies the directory in your cache where files will be exported from. This cache directory can be linked to only one data repository (S3 or NFS) and no other data repository can be linked to the directory.</p> <note> <p>The cache path can only be set to root (/) on an NFS DRA when <code>DataRepositorySubdirectories</code> is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.</p> <p>The cache path cannot be set to root (/) for an S3 DRA.</p> </note>"""
    data_repository_subdirectories: NotRequired[
        "capo_fsx.types.sub_directories_paths.SubDirectoriesPaths"
    ]
    """<p>For Amazon File Cache, a list of NFS Exports that will be linked with an NFS data repository association. All the subdirectories must be on a single NFS file system. The Export paths are in the format <code>/exportpath1</code>. To use this parameter, you must configure <code>DataRepositoryPath</code> as the domain name of the NFS file system. The NFS file system domain name in effect is the root of the subdirectories. Note that <code>DataRepositorySubdirectories</code> is not supported for S3 data repositories.</p>"""
    nfs: NotRequired[
        "capo_fsx.types.nfs_data_repository_configuration.NFSDataRepositoryConfiguration"
    ]
    """<p>The configuration for an NFS data repository linked to an Amazon File Cache resource with a data repository association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryAssociation) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "lifecycle" in value:
        import capo_fsx.types.data_repository_lifecycle

        out["Lifecycle"] = (
            capo_fsx.types.data_repository_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "failure_details" in value:
        import capo_fsx.types.data_repository_failure_details

        out["FailureDetails"] = (
            capo_fsx.types.data_repository_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "file_system_path" in value:
        out["FileSystemPath"] = value["file_system_path"]
    if "data_repository_path" in value:
        out["DataRepositoryPath"] = value["data_repository_path"]
    if "batch_import_meta_data_on_create" in value:
        out["BatchImportMetaDataOnCreate"] = value["batch_import_meta_data_on_create"]
    if "imported_file_chunk_size" in value:
        out["ImportedFileChunkSize"] = value["imported_file_chunk_size"]
    if "s3" in value:
        import capo_fsx.types.s3_data_repository_configuration

        out["S3"] = (
            capo_fsx.types.s3_data_repository_configuration.serialize_aws_json_1_1(
                value["s3"]
            )
        )
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "creation_time" in value:
        import capo_fsx.types.creation_time

        out["CreationTime"] = capo_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "file_cache_path" in value:
        out["FileCachePath"] = value["file_cache_path"]
    if "data_repository_subdirectories" in value:
        import capo_fsx.types.sub_directories_paths

        out["DataRepositorySubdirectories"] = (
            capo_fsx.types.sub_directories_paths.serialize_aws_json_1_1(
                value["data_repository_subdirectories"]
            )
        )
    if "nfs" in value:
        import capo_fsx.types.nfs_data_repository_configuration

        out["NFS"] = (
            capo_fsx.types.nfs_data_repository_configuration.serialize_aws_json_1_1(
                value["nfs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryAssociation:
    out: DataRepositoryAssociation = {}  # type: ignore[typeddict-item]
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.data_repository_lifecycle

        out["lifecycle"] = (
            capo_fsx.types.data_repository_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if data.get("FailureDetails") is not None:
        import capo_fsx.types.data_repository_failure_details

        out["failure_details"] = (
            capo_fsx.types.data_repository_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if data.get("FileSystemPath") is not None:
        out["file_system_path"] = data["FileSystemPath"]
    if data.get("DataRepositoryPath") is not None:
        out["data_repository_path"] = data["DataRepositoryPath"]
    if data.get("BatchImportMetaDataOnCreate") is not None:
        out["batch_import_meta_data_on_create"] = data["BatchImportMetaDataOnCreate"]
    if data.get("ImportedFileChunkSize") is not None:
        out["imported_file_chunk_size"] = data["ImportedFileChunkSize"]
    if data.get("S3") is not None:
        import capo_fsx.types.s3_data_repository_configuration

        out["s3"] = (
            capo_fsx.types.s3_data_repository_configuration.deserialize_aws_json_1_1(
                data["S3"]
            )
        )
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CreationTime") is not None:
        import capo_fsx.types.creation_time

        out["creation_time"] = capo_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("FileCacheId") is not None:
        out["file_cache_id"] = data["FileCacheId"]
    if data.get("FileCachePath") is not None:
        out["file_cache_path"] = data["FileCachePath"]
    if data.get("DataRepositorySubdirectories") is not None:
        import capo_fsx.types.sub_directories_paths

        out["data_repository_subdirectories"] = (
            capo_fsx.types.sub_directories_paths.deserialize_aws_json_1_1(
                data["DataRepositorySubdirectories"]
            )
        )
    if data.get("NFS") is not None:
        import capo_fsx.types.nfs_data_repository_configuration

        out["nfs"] = (
            capo_fsx.types.nfs_data_repository_configuration.deserialize_aws_json_1_1(
                data["NFS"]
            )
        )
    return out
