"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.archive_path
    import capo_fsx.types.auto_import_policy_type
    import capo_fsx.types.data_repository_failure_details
    import capo_fsx.types.data_repository_lifecycle
    import capo_fsx.types.megabytes


class DataRepositoryConfiguration(TypedDict, closed=True):
    lifecycle: NotRequired[
        "capo_fsx.types.data_repository_lifecycle.DataRepositoryLifecycle"
    ]
    """<p>Describes the state of the file system's S3 durable data repository, if it is configured with an S3 repository. The lifecycle can have the following values:</p> <ul> <li> <p> <code>CREATING</code> - The data repository configuration between the FSx file system and the linked S3 data repository is being created. The data repository is unavailable.</p> </li> <li> <p> <code>AVAILABLE</code> - The data repository is available for use.</p> </li> <li> <p> <code>MISCONFIGURED</code> - Amazon FSx cannot automatically import updates from the S3 bucket until the data repository configuration is corrected. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/troubleshooting.html#troubleshooting-misconfigured-data-repository">Troubleshooting a Misconfigured linked S3 bucket</a>. </p> </li> <li> <p> <code>UPDATING</code> - The data repository is undergoing a customer initiated update and availability may be impacted.</p> </li> <li> <p> <code>FAILED</code> - The data repository is in a terminal state that cannot be recovered.</p> </li> </ul>"""
    import_path: NotRequired["capo_fsx.types.archive_path.ArchivePath"]
    """<p>The import path to the Amazon S3 bucket (and optional prefix) that you're using as the data repository for your FSx for Lustre file system, for example <code>s3://import-bucket/optional-prefix</code>. If a prefix is specified after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.</p>"""
    export_path: NotRequired["capo_fsx.types.archive_path.ArchivePath"]
    """<p>The export path to the Amazon S3 bucket (and prefix) that you are using to store new and changed Lustre file system files in S3.</p>"""
    imported_file_chunk_size: NotRequired["capo_fsx.types.megabytes.Megabytes"]
    """<p>For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.</p> <p>The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.</p>"""
    auto_import_policy: NotRequired[
        "capo_fsx.types.auto_import_policy_type.AutoImportPolicyType"
    ]
    """<p>Describes the file system's linked S3 data repository's <code>AutoImportPolicy</code>. The AutoImportPolicy configures how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. <code>AutoImportPolicy</code> can have the following values:</p> <ul> <li> <p> <code>NONE</code> - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.</p> </li> <li> <p> <code>NEW</code> - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. </p> </li> <li> <p> <code>NEW_CHANGED</code> - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.</p> </li> <li> <p> <code>NEW_CHANGED_DELETED</code> - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.</p> </li> </ul>"""
    failure_details: NotRequired[
        "capo_fsx.types.data_repository_failure_details.DataRepositoryFailureDetails"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryConfiguration) -> dict:
    out: dict = {}
    if "lifecycle" in value:
        import capo_fsx.types.data_repository_lifecycle

        out["Lifecycle"] = (
            capo_fsx.types.data_repository_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "import_path" in value:
        out["ImportPath"] = value["import_path"]
    if "export_path" in value:
        out["ExportPath"] = value["export_path"]
    if "imported_file_chunk_size" in value:
        out["ImportedFileChunkSize"] = value["imported_file_chunk_size"]
    if "auto_import_policy" in value:
        import capo_fsx.types.auto_import_policy_type

        out["AutoImportPolicy"] = (
            capo_fsx.types.auto_import_policy_type.serialize_aws_json_1_1(
                value["auto_import_policy"]
            )
        )
    if "failure_details" in value:
        import capo_fsx.types.data_repository_failure_details

        out["FailureDetails"] = (
            capo_fsx.types.data_repository_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryConfiguration:
    out: DataRepositoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.data_repository_lifecycle

        out["lifecycle"] = (
            capo_fsx.types.data_repository_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if data.get("ImportPath") is not None:
        out["import_path"] = data["ImportPath"]
    if data.get("ExportPath") is not None:
        out["export_path"] = data["ExportPath"]
    if data.get("ImportedFileChunkSize") is not None:
        out["imported_file_chunk_size"] = data["ImportedFileChunkSize"]
    if data.get("AutoImportPolicy") is not None:
        import capo_fsx.types.auto_import_policy_type

        out["auto_import_policy"] = (
            capo_fsx.types.auto_import_policy_type.deserialize_aws_json_1_1(
                data["AutoImportPolicy"]
            )
        )
    if data.get("FailureDetails") is not None:
        import capo_fsx.types.data_repository_failure_details

        out["failure_details"] = (
            capo_fsx.types.data_repository_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    return out
