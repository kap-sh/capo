"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeTaskExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.filter_list
    import capo_datasync.types.item_count
    import capo_datasync.types.long
    import capo_datasync.types.manifest_config
    import capo_datasync.types.options
    import capo_datasync.types.report_result
    import capo_datasync.types.task_execution_arn
    import capo_datasync.types.task_execution_files_failed_detail
    import capo_datasync.types.task_execution_files_listed_detail
    import capo_datasync.types.task_execution_folders_failed_detail
    import capo_datasync.types.task_execution_folders_listed_detail
    import capo_datasync.types.task_execution_result_detail
    import capo_datasync.types.task_execution_status
    import capo_datasync.types.task_mode
    import capo_datasync.types.task_report_config
    import capo_datasync.types.time


class DescribeTaskExecutionResponse(TypedDict, closed=True):
    task_execution_arn: NotRequired[
        "capo_datasync.types.task_execution_arn.TaskExecutionArn"
    ]
    """<p>The ARN of the task execution that you wanted information about. <code>TaskExecutionArn</code> is hierarchical and includes <code>TaskArn</code> for the task that was executed. </p> <p>For example, a <code>TaskExecution</code> value with the ARN <code>arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2/execution/exec-08ef1e88ec491019b</code> executed the task with the ARN <code>arn:aws:datasync:us-east-1:111222333444:task/task-0208075f79cedf4a2</code>. </p>"""
    status: NotRequired["capo_datasync.types.task_execution_status.TaskExecutionStatus"]
    """<p>The status of the task execution. </p>"""
    options: NotRequired["capo_datasync.types.options.Options"]
    excludes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>A list of filter rules that exclude specific data during your transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Filtering data transferred by DataSync</a>.</p>"""
    includes: NotRequired["capo_datasync.types.filter_list.FilterList"]
    """<p>A list of filter rules that include specific data during your transfer. For more information and examples, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html">Filtering data transferred by DataSync</a>.</p>"""
    manifest_config: NotRequired["capo_datasync.types.manifest_config.ManifestConfig"]
    """<p>The configuration of the manifest that lists the files or objects to transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">Specifying what DataSync transfers by using a manifest</a>.</p>"""
    start_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that DataSync sends the request to start the task execution. For non-queued tasks, <code>LaunchTime</code> and <code>StartTime</code> are typically the same. For queued tasks, <code>LaunchTime</code> is typically later than <code>StartTime</code> because previously queued tasks must finish running before newer tasks can begin.</p>"""
    estimated_files_to_transfer: "capo_datasync.types.long.long"
    """<p>The number of files, objects, and directories that DataSync expects to transfer over the network. This value is calculated while DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">prepares</a> the transfer.</p> <p>How this gets calculated depends primarily on your task’s <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode">transfer mode</a> configuration:</p> <ul> <li> <p>If <code>TranserMode</code> is set to <code>CHANGED</code> - The calculation is based on comparing the content of the source and destination locations and determining the difference that needs to be transferred. The difference can include:</p> <ul> <li> <p>Anything that's added or modified at the source location.</p> </li> <li> <p>Anything that's in both locations and modified at the destination after an initial transfer (unless <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode">OverwriteMode</a> is set to <code>NEVER</code>).</p> </li> <li> <p> <b>(Basic task mode only)</b> The number of items that DataSync expects to delete (if <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PreserveDeletedFiles">PreserveDeletedFiles</a> is set to <code>REMOVE</code>).</p> </li> </ul> </li> <li> <p>If <code>TranserMode</code> is set to <code>ALL</code> - The calculation is based only on the items that DataSync finds at the source location.</p> </li> </ul> <note> <p>For <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-EstimatedFoldersToTransfer">EstimatedFoldersToTransfer</a>. </p> </note>"""
    estimated_bytes_to_transfer: "capo_datasync.types.long.long"
    """<p>The number of logical bytes that DataSync expects to write to the destination location.</p>"""
    files_transferred: "capo_datasync.types.long.long"
    """<p>The number of files, objects, and directories that DataSync actually transfers over the network. This value is updated periodically during your task execution when something is read from the source and sent over the network.</p> <p>If DataSync fails to transfer something, this value can be less than <code>EstimatedFilesToTransfer</code>. In some cases, this value can also be greater than <code>EstimatedFilesToTransfer</code>. This element is implementation-specific for some location types, so don't use it as an exact indication of what's transferring or to monitor your task execution.</p> <note> <p>For <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersTransferred">FoldersTransferred</a>. </p> </note>"""
    bytes_written: "capo_datasync.types.long.long"
    """<p>The number of logical bytes that DataSync actually writes to the destination location.</p>"""
    bytes_transferred: "capo_datasync.types.long.long"
    """<p>The number of bytes that DataSync sends to the network before compression (if compression is possible). For the number of bytes transferred over the network, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesCompressed">BytesCompressed</a>. </p>"""
    bytes_compressed: "capo_datasync.types.long.long"
    """<p>The number of physical bytes that DataSync transfers over the network after compression (if compression is possible). This number is typically less than <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-BytesTransferred">BytesTransferred</a> unless the data isn't compressible.</p>"""
    result: NotRequired[
        "capo_datasync.types.task_execution_result_detail.TaskExecutionResultDetail"
    ]
    """<p>The result of the task execution.</p>"""
    task_report_config: NotRequired[
        "capo_datasync.types.task_report_config.TaskReportConfig"
    ]
    """<p>The configuration of your task report, which provides detailed information about for your DataSync transfer. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">Creating a task report</a>.</p>"""
    files_deleted: "capo_datasync.types.long.long"
    """<p>The number of files, objects, and directories that DataSync actually deletes in your destination location. If you don't configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>For <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersDeleted">FoldersDeleted</a>. </p> </note>"""
    files_skipped: "capo_datasync.types.long.long"
    """<p>The number of files, objects, and directories that DataSync skips during your transfer.</p> <note> <p>For <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersSkipped">FoldersSkipped</a>. </p> </note>"""
    files_verified: "capo_datasync.types.long.long"
    """<p>The number of files, objects, and directories that DataSync verifies during your transfer.</p> <note> <p>When you configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-data-verification-options.html">verify only the data that's transferred</a>, DataSync doesn't verify directories in some situations or files that fail to transfer.</p> <p>For <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-FoldersVerified">FoldersVerified</a>. </p> </note>"""
    report_result: NotRequired["capo_datasync.types.report_result.ReportResult"]
    """<p>Indicates whether DataSync generated a complete <a href="https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html">task report</a> for your transfer.</p>"""
    estimated_files_to_delete: "capo_datasync.types.long.long"
    """<p>The number of files, objects, and directories that DataSync expects to delete in your destination location. If you don't configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>For <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>, this counter only includes files or objects. Directories are counted in <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html#DataSync-DescribeTaskExecution-response-EstimatedFoldersToDelete">EstimatedFoldersToDelete</a>. </p> </note>"""
    task_mode: NotRequired["capo_datasync.types.task_mode.TaskMode"]
    """<p>The task mode that you're using. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Choosing a task mode for your data transfer</a>.</p>"""
    files_prepared: "capo_datasync.types.long.long"
    """<p>The number of files or objects that DataSync will attempt to transfer after comparing your source and destination locations.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note> <p>This counter isn't applicable if you configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-transfer-mode">transfer all data</a>. In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.</p>"""
    files_listed: NotRequired[
        "capo_datasync.types.task_execution_files_listed_detail.TaskExecutionFilesListedDetail"
    ]
    """<p>The number of files or objects that DataSync finds at your locations.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    files_failed: NotRequired[
        "capo_datasync.types.task_execution_files_failed_detail.TaskExecutionFilesFailedDetail"
    ]
    """<p>The number of files or objects that DataSync fails to prepare, transfer, verify, and delete during your task execution.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    estimated_folders_to_delete: NotRequired["capo_datasync.types.item_count.ItemCount"]
    """<p>The number of directories that DataSync expects to delete in your destination location. If you don't configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    estimated_folders_to_transfer: NotRequired[
        "capo_datasync.types.item_count.ItemCount"
    ]
    """<p>The number of directories that DataSync expects to transfer over the network. This value is calculated as DataSync <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#understand-task-execution-statuses">prepares</a> directories to transfer.</p> <p>How this gets calculated depends primarily on your task’s <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-TransferMode">transfer mode</a> configuration:</p> <ul> <li> <p>If <code>TranserMode</code> is set to <code>CHANGED</code> - The calculation is based on comparing the content of the source and destination locations and determining the difference that needs to be transferred. The difference can include:</p> <ul> <li> <p>Anything that's added or modified at the source location.</p> </li> <li> <p>Anything that's in both locations and modified at the destination after an initial transfer (unless <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-OverwriteMode">OverwriteMode</a> is set to <code>NEVER</code>).</p> </li> </ul> </li> <li> <p>If <code>TranserMode</code> is set to <code>ALL</code> - The calculation is based only on the items that DataSync finds at the source location.</p> </li> </ul> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    folders_skipped: NotRequired["capo_datasync.types.item_count.ItemCount"]
    """<p>The number of directories that DataSync skips during your transfer.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    folders_prepared: NotRequired["capo_datasync.types.item_count.ItemCount"]
    """<p>The number of directories that DataSync will attempt to transfer after comparing your source and destination locations.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note> <p>This counter isn't applicable if you configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-transfer-mode">transfer all data</a>. In that scenario, DataSync copies everything from the source to the destination without comparing differences between the locations.</p>"""
    folders_transferred: NotRequired["capo_datasync.types.item_count.ItemCount"]
    """<p>The number of directories that DataSync actually transfers over the network. This value is updated periodically during your task execution when something is read from the source and sent over the network.</p> <p>If DataSync fails to transfer something, this value can be less than <code>EstimatedFoldersToTransfer</code>. In some cases, this value can also be greater than <code>EstimatedFoldersToTransfer</code>. </p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    folders_verified: NotRequired["capo_datasync.types.item_count.ItemCount"]
    """<p>The number of directories that DataSync verifies during your transfer.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    folders_deleted: NotRequired["capo_datasync.types.item_count.ItemCount"]
    """<p>The number of directories that DataSync actually deletes in your destination location. If you don't configure your task to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html">delete data in the destination that isn't in the source</a>, the value is always <code>0</code>.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    folders_listed: NotRequired[
        "capo_datasync.types.task_execution_folders_listed_detail.TaskExecutionFoldersListedDetail"
    ]
    """<p>The number of directories that DataSync finds at your locations.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    folders_failed: NotRequired[
        "capo_datasync.types.task_execution_folders_failed_detail.TaskExecutionFoldersFailedDetail"
    ]
    """<p>The number of directories that DataSync fails to list, prepare, transfer, verify, and delete during your task execution.</p> <note> <p>Applies only to <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note>"""
    launch_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the task execution actually begins. For non-queued tasks, <code>LaunchTime</code> and <code>StartTime</code> are typically the same. For queued tasks, <code>LaunchTime</code> is typically later than <code>StartTime</code> because previously queued tasks must finish running before newer tasks can begin.</p>"""
    end_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the transfer task ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTaskExecutionResponse) -> dict:
    out: dict = {}
    if "task_execution_arn" in value:
        out["TaskExecutionArn"] = value["task_execution_arn"]
    if "status" in value:
        import capo_datasync.types.task_execution_status

        out["Status"] = (
            capo_datasync.types.task_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "options" in value:
        import capo_datasync.types.options

        out["Options"] = capo_datasync.types.options.serialize_aws_json_1_1(
            value["options"]
        )
    if "excludes" in value:
        import capo_datasync.types.filter_list

        out["Excludes"] = capo_datasync.types.filter_list.serialize_aws_json_1_1(
            value["excludes"]
        )
    if "includes" in value:
        import capo_datasync.types.filter_list

        out["Includes"] = capo_datasync.types.filter_list.serialize_aws_json_1_1(
            value["includes"]
        )
    if "manifest_config" in value:
        import capo_datasync.types.manifest_config

        out["ManifestConfig"] = (
            capo_datasync.types.manifest_config.serialize_aws_json_1_1(
                value["manifest_config"]
            )
        )
    if "start_time" in value:
        import capo_datasync.types.time

        out["StartTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["start_time"]
        )
    out["EstimatedFilesToTransfer"] = value.get("estimated_files_to_transfer", 0)
    out["EstimatedBytesToTransfer"] = value.get("estimated_bytes_to_transfer", 0)
    out["FilesTransferred"] = value.get("files_transferred", 0)
    out["BytesWritten"] = value.get("bytes_written", 0)
    out["BytesTransferred"] = value.get("bytes_transferred", 0)
    out["BytesCompressed"] = value.get("bytes_compressed", 0)
    if "result" in value:
        import capo_datasync.types.task_execution_result_detail

        out["Result"] = (
            capo_datasync.types.task_execution_result_detail.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "task_report_config" in value:
        import capo_datasync.types.task_report_config

        out["TaskReportConfig"] = (
            capo_datasync.types.task_report_config.serialize_aws_json_1_1(
                value["task_report_config"]
            )
        )
    out["FilesDeleted"] = value.get("files_deleted", 0)
    out["FilesSkipped"] = value.get("files_skipped", 0)
    out["FilesVerified"] = value.get("files_verified", 0)
    if "report_result" in value:
        import capo_datasync.types.report_result

        out["ReportResult"] = capo_datasync.types.report_result.serialize_aws_json_1_1(
            value["report_result"]
        )
    out["EstimatedFilesToDelete"] = value.get("estimated_files_to_delete", 0)
    if "task_mode" in value:
        import capo_datasync.types.task_mode

        out["TaskMode"] = capo_datasync.types.task_mode.serialize_aws_json_1_1(
            value["task_mode"]
        )
    out["FilesPrepared"] = value.get("files_prepared", 0)
    if "files_listed" in value:
        import capo_datasync.types.task_execution_files_listed_detail

        out["FilesListed"] = (
            capo_datasync.types.task_execution_files_listed_detail.serialize_aws_json_1_1(
                value["files_listed"]
            )
        )
    if "files_failed" in value:
        import capo_datasync.types.task_execution_files_failed_detail

        out["FilesFailed"] = (
            capo_datasync.types.task_execution_files_failed_detail.serialize_aws_json_1_1(
                value["files_failed"]
            )
        )
    if "estimated_folders_to_delete" in value:
        out["EstimatedFoldersToDelete"] = value["estimated_folders_to_delete"]
    if "estimated_folders_to_transfer" in value:
        out["EstimatedFoldersToTransfer"] = value["estimated_folders_to_transfer"]
    if "folders_skipped" in value:
        out["FoldersSkipped"] = value["folders_skipped"]
    if "folders_prepared" in value:
        out["FoldersPrepared"] = value["folders_prepared"]
    if "folders_transferred" in value:
        out["FoldersTransferred"] = value["folders_transferred"]
    if "folders_verified" in value:
        out["FoldersVerified"] = value["folders_verified"]
    if "folders_deleted" in value:
        out["FoldersDeleted"] = value["folders_deleted"]
    if "folders_listed" in value:
        import capo_datasync.types.task_execution_folders_listed_detail

        out["FoldersListed"] = (
            capo_datasync.types.task_execution_folders_listed_detail.serialize_aws_json_1_1(
                value["folders_listed"]
            )
        )
    if "folders_failed" in value:
        import capo_datasync.types.task_execution_folders_failed_detail

        out["FoldersFailed"] = (
            capo_datasync.types.task_execution_folders_failed_detail.serialize_aws_json_1_1(
                value["folders_failed"]
            )
        )
    if "launch_time" in value:
        import capo_datasync.types.time

        out["LaunchTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["launch_time"]
        )
    if "end_time" in value:
        import capo_datasync.types.time

        out["EndTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["end_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTaskExecutionResponse:
    out: DescribeTaskExecutionResponse = {}  # type: ignore[typeddict-item]
    if data.get("TaskExecutionArn") is not None:
        out["task_execution_arn"] = data["TaskExecutionArn"]
    if data.get("Status") is not None:
        import capo_datasync.types.task_execution_status

        out["status"] = (
            capo_datasync.types.task_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Options") is not None:
        import capo_datasync.types.options

        out["options"] = capo_datasync.types.options.deserialize_aws_json_1_1(
            data["Options"]
        )
    if data.get("Excludes") is not None:
        import capo_datasync.types.filter_list

        out["excludes"] = capo_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Excludes"]
        )
    if data.get("Includes") is not None:
        import capo_datasync.types.filter_list

        out["includes"] = capo_datasync.types.filter_list.deserialize_aws_json_1_1(
            data["Includes"]
        )
    if data.get("ManifestConfig") is not None:
        import capo_datasync.types.manifest_config

        out["manifest_config"] = (
            capo_datasync.types.manifest_config.deserialize_aws_json_1_1(
                data["ManifestConfig"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_datasync.types.time

        out["start_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("EstimatedFilesToTransfer") is not None:
        out["estimated_files_to_transfer"] = data["EstimatedFilesToTransfer"]
    else:
        out["estimated_files_to_transfer"] = 0
    if data.get("EstimatedBytesToTransfer") is not None:
        out["estimated_bytes_to_transfer"] = data["EstimatedBytesToTransfer"]
    else:
        out["estimated_bytes_to_transfer"] = 0
    if data.get("FilesTransferred") is not None:
        out["files_transferred"] = data["FilesTransferred"]
    else:
        out["files_transferred"] = 0
    if data.get("BytesWritten") is not None:
        out["bytes_written"] = data["BytesWritten"]
    else:
        out["bytes_written"] = 0
    if data.get("BytesTransferred") is not None:
        out["bytes_transferred"] = data["BytesTransferred"]
    else:
        out["bytes_transferred"] = 0
    if data.get("BytesCompressed") is not None:
        out["bytes_compressed"] = data["BytesCompressed"]
    else:
        out["bytes_compressed"] = 0
    if data.get("Result") is not None:
        import capo_datasync.types.task_execution_result_detail

        out["result"] = (
            capo_datasync.types.task_execution_result_detail.deserialize_aws_json_1_1(
                data["Result"]
            )
        )
    if data.get("TaskReportConfig") is not None:
        import capo_datasync.types.task_report_config

        out["task_report_config"] = (
            capo_datasync.types.task_report_config.deserialize_aws_json_1_1(
                data["TaskReportConfig"]
            )
        )
    if data.get("FilesDeleted") is not None:
        out["files_deleted"] = data["FilesDeleted"]
    else:
        out["files_deleted"] = 0
    if data.get("FilesSkipped") is not None:
        out["files_skipped"] = data["FilesSkipped"]
    else:
        out["files_skipped"] = 0
    if data.get("FilesVerified") is not None:
        out["files_verified"] = data["FilesVerified"]
    else:
        out["files_verified"] = 0
    if data.get("ReportResult") is not None:
        import capo_datasync.types.report_result

        out["report_result"] = (
            capo_datasync.types.report_result.deserialize_aws_json_1_1(
                data["ReportResult"]
            )
        )
    if data.get("EstimatedFilesToDelete") is not None:
        out["estimated_files_to_delete"] = data["EstimatedFilesToDelete"]
    else:
        out["estimated_files_to_delete"] = 0
    if data.get("TaskMode") is not None:
        import capo_datasync.types.task_mode

        out["task_mode"] = capo_datasync.types.task_mode.deserialize_aws_json_1_1(
            data["TaskMode"]
        )
    if data.get("FilesPrepared") is not None:
        out["files_prepared"] = data["FilesPrepared"]
    else:
        out["files_prepared"] = 0
    if data.get("FilesListed") is not None:
        import capo_datasync.types.task_execution_files_listed_detail

        out["files_listed"] = (
            capo_datasync.types.task_execution_files_listed_detail.deserialize_aws_json_1_1(
                data["FilesListed"]
            )
        )
    if data.get("FilesFailed") is not None:
        import capo_datasync.types.task_execution_files_failed_detail

        out["files_failed"] = (
            capo_datasync.types.task_execution_files_failed_detail.deserialize_aws_json_1_1(
                data["FilesFailed"]
            )
        )
    if data.get("EstimatedFoldersToDelete") is not None:
        out["estimated_folders_to_delete"] = data["EstimatedFoldersToDelete"]
    if data.get("EstimatedFoldersToTransfer") is not None:
        out["estimated_folders_to_transfer"] = data["EstimatedFoldersToTransfer"]
    if data.get("FoldersSkipped") is not None:
        out["folders_skipped"] = data["FoldersSkipped"]
    if data.get("FoldersPrepared") is not None:
        out["folders_prepared"] = data["FoldersPrepared"]
    if data.get("FoldersTransferred") is not None:
        out["folders_transferred"] = data["FoldersTransferred"]
    if data.get("FoldersVerified") is not None:
        out["folders_verified"] = data["FoldersVerified"]
    if data.get("FoldersDeleted") is not None:
        out["folders_deleted"] = data["FoldersDeleted"]
    if data.get("FoldersListed") is not None:
        import capo_datasync.types.task_execution_folders_listed_detail

        out["folders_listed"] = (
            capo_datasync.types.task_execution_folders_listed_detail.deserialize_aws_json_1_1(
                data["FoldersListed"]
            )
        )
    if data.get("FoldersFailed") is not None:
        import capo_datasync.types.task_execution_folders_failed_detail

        out["folders_failed"] = (
            capo_datasync.types.task_execution_folders_failed_detail.deserialize_aws_json_1_1(
                data["FoldersFailed"]
            )
        )
    if data.get("LaunchTime") is not None:
        import capo_datasync.types.time

        out["launch_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["LaunchTime"]
        )
    if data.get("EndTime") is not None:
        import capo_datasync.types.time

        out["end_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    return out
