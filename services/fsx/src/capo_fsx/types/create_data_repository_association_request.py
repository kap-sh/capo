"""Generated from Smithy shape ``com.amazonaws.fsx#CreateDataRepositoryAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.archive_path
    import capo_fsx.types.batch_import_meta_data_on_create
    import capo_fsx.types.client_request_token
    import capo_fsx.types.file_system_id
    import capo_fsx.types.megabytes
    import capo_fsx.types.namespace
    import capo_fsx.types.s3_data_repository_configuration
    import capo_fsx.types.tags


class CreateDataRepositoryAssociationRequest(TypedDict, closed=True):
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    file_system_path: NotRequired["capo_fsx.types.namespace.Namespace"]
    """<p>A path on the file system that points to a high-level directory (such as <code>/ns1/</code>) or subdirectory (such as <code>/ns1/subdir/</code>) that will be mapped 1-1 with <code>DataRepositoryPath</code>. The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path <code>/ns1/</code>, then you cannot link another data repository with file system path <code>/ns1/ns2</code>.</p> <p>This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.</p> <note> <p>If you specify only a forward slash (<code>/</code>) as the file system path, you can link only one data repository to the file system. You can only specify "/" as the file system path for the first data repository associated with a file system.</p> </note>"""
    data_repository_path: NotRequired["capo_fsx.types.archive_path.ArchivePath"]
    """<p>The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix/</code> (where <code>prefix</code> is optional). This path specifies where in the S3 data repository files will be imported from or exported to.</p>"""
    batch_import_meta_data_on_create: NotRequired[
        "capo_fsx.types.batch_import_meta_data_on_create.BatchImportMetaDataOnCreate"
    ]
    """<p>Set to <code>true</code> to run an import data repository task to import metadata from the data repository to the file system after the data repository association is created. Default is <code>false</code>.</p>"""
    imported_file_chunk_size: NotRequired["capo_fsx.types.megabytes.Megabytes"]
    """<p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p>"""
    s3: NotRequired[
        "capo_fsx.types.s3_data_repository_configuration.S3DataRepositoryConfiguration"
    ]
    """<p>The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["capo_fsx.types.tags.Tags"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataRepositoryAssociationRequest) -> dict:
    out: dict = {}
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
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
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataRepositoryAssociationRequest:
    out: CreateDataRepositoryAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
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
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out
