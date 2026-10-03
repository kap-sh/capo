"""Generated from Smithy shape ``com.amazonaws.fsx#CreateDataRepositoryTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.capacity_to_release
    import capo_fsx.types.client_request_token
    import capo_fsx.types.completion_report
    import capo_fsx.types.data_repository_task_paths
    import capo_fsx.types.data_repository_task_type
    import capo_fsx.types.file_system_id
    import capo_fsx.types.release_configuration
    import capo_fsx.types.tags


class CreateDataRepositoryTaskRequest(TypedDict, closed=True):
    type: NotRequired["capo_fsx.types.data_repository_task_type.DataRepositoryTaskType"]
    """<p>Specifies the type of data repository task to create.</p> <ul> <li> <p> <code>EXPORT_TO_REPOSITORY</code> tasks export from your Amazon FSx for Lustre file system to a linked data repository.</p> </li> <li> <p> <code>IMPORT_METADATA_FROM_REPOSITORY</code> tasks import metadata changes from a linked S3 bucket to your Amazon FSx for Lustre file system.</p> </li> <li> <p> <code>RELEASE_DATA_FROM_FILESYSTEM</code> tasks release files in your Amazon FSx for Lustre file system that have been exported to a linked S3 bucket and that meet your specified release criteria.</p> </li> <li> <p> <code>AUTO_RELEASE_DATA</code> tasks automatically release files from an Amazon File Cache resource.</p> </li> </ul>"""
    paths: NotRequired[
        "capo_fsx.types.data_repository_task_paths.DataRepositoryTaskPaths"
    ]
    """<p>A list of paths for the data repository task to use when the task is processed. If a path that you provide isn't valid, the task fails. If you don't provide paths, the default behavior is to export all files to S3 (for export tasks), import all files from S3 (for import tasks), or release all exported files that meet the last accessed time criteria (for release tasks).</p> <ul> <li> <p>For export tasks, the list contains paths on the FSx for Lustre file system from which the files are exported to the Amazon S3 bucket. The default path is the file system root directory. The paths you provide need to be relative to the mount point of the file system. If the mount point is <code>/mnt/fsx</code> and <code>/mnt/fsx/path1</code> is a directory or file on the file system you want to export, then the path to provide is <code>path1</code>.</p> </li> <li> <p>For import tasks, the list contains paths in the Amazon S3 bucket from which POSIX metadata changes are imported to the FSx for Lustre file system. The path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix</code> (where <code>prefix</code> is optional).</p> </li> <li> <p>For release tasks, the list contains directory or file paths on the FSx for Lustre file system from which to release exported files. If a directory is specified, files within the directory are released. If a file path is specified, only that file is released. To release all exported files in the file system, specify a forward slash (/) as the path.</p> <note> <p>A file must also meet the last accessed time criteria specified in for the file to be released.</p> </note> </li> </ul>"""
    file_system_id: NotRequired["capo_fsx.types.file_system_id.FileSystemId"]
    report: NotRequired["capo_fsx.types.completion_report.CompletionReport"]
    """<p>Defines whether or not Amazon FSx provides a CompletionReport once the task has completed. A CompletionReport provides a detailed report on the files that Amazon FSx processed that meet the criteria specified by the <code>Scope</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/LustreGuide/task-completion-report.html">Working with Task Completion Reports</a>.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    tags: NotRequired["capo_fsx.types.tags.Tags"]
    capacity_to_release: NotRequired[
        "capo_fsx.types.capacity_to_release.CapacityToRelease"
    ]
    """<p>Specifies the amount of data to release, in GiB, by an Amazon File Cache <code>AUTO_RELEASE_DATA</code> task that automatically releases files from the cache.</p>"""
    release_configuration: NotRequired[
        "capo_fsx.types.release_configuration.ReleaseConfiguration"
    ]
    """<p>The configuration that specifies the last accessed time criteria for files that will be released from an Amazon FSx for Lustre file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataRepositoryTaskRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_fsx.types.data_repository_task_type

        out["Type"] = capo_fsx.types.data_repository_task_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "paths" in value:
        import capo_fsx.types.data_repository_task_paths

        out["Paths"] = capo_fsx.types.data_repository_task_paths.serialize_aws_json_1_1(
            value["paths"]
        )
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "report" in value:
        import capo_fsx.types.completion_report

        out["Report"] = capo_fsx.types.completion_report.serialize_aws_json_1_1(
            value["report"]
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_fsx.types.tags

        out["Tags"] = capo_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "capacity_to_release" in value:
        out["CapacityToRelease"] = value["capacity_to_release"]
    if "release_configuration" in value:
        import capo_fsx.types.release_configuration

        out["ReleaseConfiguration"] = (
            capo_fsx.types.release_configuration.serialize_aws_json_1_1(
                value["release_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataRepositoryTaskRequest:
    out: CreateDataRepositoryTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_fsx.types.data_repository_task_type

        out["type"] = capo_fsx.types.data_repository_task_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("Paths") is not None:
        import capo_fsx.types.data_repository_task_paths

        out["paths"] = (
            capo_fsx.types.data_repository_task_paths.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    if data.get("Report") is not None:
        import capo_fsx.types.completion_report

        out["report"] = capo_fsx.types.completion_report.deserialize_aws_json_1_1(
            data["Report"]
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Tags") is not None:
        import capo_fsx.types.tags

        out["tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("CapacityToRelease") is not None:
        out["capacity_to_release"] = data["CapacityToRelease"]
    if data.get("ReleaseConfiguration") is not None:
        import capo_fsx.types.release_configuration

        out["release_configuration"] = (
            capo_fsx.types.release_configuration.deserialize_aws_json_1_1(
                data["ReleaseConfiguration"]
            )
        )
    return out
