"""Generated from Smithy shape ``com.amazonaws.datasync#Options``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.atime
    import capo_datasync.types.bytes_per_second
    import capo_datasync.types.gid
    import capo_datasync.types.log_level
    import capo_datasync.types.mtime
    import capo_datasync.types.object_tags
    import capo_datasync.types.overwrite_mode
    import capo_datasync.types.posix_permissions
    import capo_datasync.types.preserve_deleted_files
    import capo_datasync.types.preserve_devices
    import capo_datasync.types.smb_security_descriptor_copy_flags
    import capo_datasync.types.task_queueing
    import capo_datasync.types.transfer_mode
    import capo_datasync.types.uid
    import capo_datasync.types.verify_mode


class Options(TypedDict, closed=True):
    verify_mode: NotRequired["capo_datasync.types.verify_mode.VerifyMode"]
    """<p>Specifies if and how DataSync checks the integrity of your data at the end of your transfer.</p> <ul> <li> <p> <code>ONLY_FILES_TRANSFERRED</code> (recommended) - DataSync calculates the checksum of transferred data (including metadata) at the source location. At the end of the transfer, DataSync then compares this checksum to the checksum calculated on that data at the destination.</p> <note> <p>This is the default option for <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Enhanced mode tasks</a>.</p> </note> <p>We recommend this option when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 locations</a>.</p> </li> <li> <p> <code>POINT_IN_TIME_CONSISTENT</code> - At the end of the transfer, DataSync checks the entire source and destination to verify that both locations are fully synchronized.</p> <note> <p>The is the default option for <a href="https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html">Basic mode tasks</a> and isn't currently supported with Enhanced mode tasks.</p> </note> <p>If you use a <a href="https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html">manifest</a>, DataSync only scans and verifies what's listed in the manifest.</p> <p>You can't use this option when transferring to S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 locations</a>.</p> </li> <li> <p> <code>NONE</code> - DataSync performs data integrity checks only during your transfer. Unlike other options, there's no additional verification at the end of your transfer.</p> </li> </ul>"""
    overwrite_mode: NotRequired["capo_datasync.types.overwrite_mode.OverwriteMode"]
    """<p>Specifies whether DataSync should modify or preserve data at the destination location.</p> <ul> <li> <p> <code>ALWAYS</code> (default) - DataSync modifies data in the destination location when source data (including metadata) has changed.</p> <p>If DataSync overwrites objects, you might incur additional charges for certain Amazon S3 storage classes (for example, for retrieval or early deletion). For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Storage class considerations with Amazon S3 transfers</a>.</p> </li> <li> <p> <code>NEVER</code> - DataSync doesn't overwrite data in the destination location even if the source data has changed. You can use this option to protect against overwriting changes made to files or objects in the destination.</p> </li> </ul>"""
    atime: NotRequired["capo_datasync.types.atime.Atime"]
    """<p>Specifies whether to preserve metadata indicating the last time a file was read or written to.</p> <note> <p>The behavior of <code>Atime</code> isn't fully standard across platforms, so DataSync can only do this on a best-effort basis.</p> </note> <ul> <li> <p> <code>BEST_EFFORT</code> (default) - DataSync attempts to preserve the original <code>Atime</code> attribute on all source files (that is, the version before the <code>PREPARING</code> steps of the task execution). This option is recommended.</p> </li> <li> <p> <code>NONE</code> - Ignores <code>Atime</code>.</p> </li> </ul> <note> <p>The following applies only to Basic mode tasks:</p> <p>If <code>Atime</code> is set to <code>BEST_EFFORT</code>, <code>Mtime</code> must be set to <code>PRESERVE</code>. </p> <p>If <code>Atime</code> is set to <code>NONE</code>, <code>Mtime</code> must also be <code>NONE</code>. </p> <p>Enhanced mode tasks support configuring <code>Atime</code> independently of <code>Mtime</code>.</p> </note>"""
    mtime: NotRequired["capo_datasync.types.mtime.Mtime"]
    """<p>Specifies whether to preserve metadata indicating the last time that a file was written to before the <code>PREPARING</code> step of your task execution. This option is required when you need to run the a task more than once.</p> <ul> <li> <p> <code>PRESERVE</code> (default) - Preserves original <code>Mtime</code>, which is recommended.</p> </li> <li> <p> <code>NONE</code> - Ignores <code>Mtime</code>.</p> </li> </ul> <note> <p>The following applies only to Basic mode tasks:</p> <p>If <code>Mtime</code> is set to <code>PRESERVE</code>, <code>Atime</code> must be set to <code>BEST_EFFORT</code>.</p> <p>If <code>Mtime</code> is set to <code>NONE</code>, <code>Atime</code> must also be set to <code>NONE</code>. </p> <p>Enhanced mode tasks don't support <code>Mtime</code> set to <code>NONE</code>.</p> </note>"""
    uid: NotRequired["capo_datasync.types.uid.Uid"]
    """<p>Specifies the POSIX user ID (UID) of the file's owner.</p> <ul> <li> <p> <code>INT_VALUE</code> (default) - Preserves the integer value of UID and group ID (GID), which is recommended.</p> </li> <li> <p> <code>NONE</code> - Ignores UID and GID. </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/special-files.html#metadata-copied">Metadata copied by DataSync</a>.</p>"""
    gid: NotRequired["capo_datasync.types.gid.Gid"]
    """<p>Specifies the POSIX group ID (GID) of the file's owners.</p> <ul> <li> <p> <code>INT_VALUE</code> (default) - Preserves the integer value of user ID (UID) and GID, which is recommended.</p> </li> <li> <p> <code>NONE</code> - Ignores UID and GID.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html">Understanding how DataSync handles file and object metadata</a>.</p>"""
    preserve_deleted_files: NotRequired[
        "capo_datasync.types.preserve_deleted_files.PreserveDeletedFiles"
    ]
    """<p>Specifies whether files in the destination location that don't exist in the source should be preserved. This option can affect your Amazon S3 storage cost. If your task deletes objects, you might incur minimum storage duration charges for certain storage classes. For detailed information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html#using-storage-classes">Considerations when working with Amazon S3 storage classes in DataSync</a>.</p> <ul> <li> <p> <code>PRESERVE</code> (default) - Ignores such destination files, which is recommended. </p> </li> <li> <p> <code>REMOVE</code> - Deletes destination files that aren’t present in the source.</p> </li> </ul> <note> <p>If you set this parameter to <code>REMOVE</code>, you can't set <code>TransferMode</code> to <code>ALL</code>. When you transfer all data, DataSync doesn't scan your destination location and doesn't know what to delete.</p> </note>"""
    preserve_devices: NotRequired[
        "capo_datasync.types.preserve_devices.PreserveDevices"
    ]
    """<p>Specifies whether DataSync should preserve the metadata of block and character devices in the source location and recreate the files with that device name and metadata on the destination. DataSync copies only the name and metadata of such devices.</p> <note> <p>DataSync can't copy the actual contents of these devices because they're nonterminal and don't return an end-of-file (EOF) marker.</p> </note> <ul> <li> <p> <code>NONE</code> (default) - Ignores special devices (recommended).</p> </li> <li> <p> <code>PRESERVE</code> - Preserves character and block device metadata. This option currently isn't supported for Amazon EFS.</p> </li> </ul>"""
    posix_permissions: NotRequired[
        "capo_datasync.types.posix_permissions.PosixPermissions"
    ]
    """<p>Specifies which users or groups can access a file for a specific purpose such as reading, writing, or execution of the file.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html">Understanding how DataSync handles file and object metadata</a>.</p> <ul> <li> <p> <code>PRESERVE</code> (default) - Preserves POSIX-style permissions, which is recommended.</p> </li> <li> <p> <code>NONE</code> - Ignores POSIX-style permissions. </p> </li> </ul> <note> <p>DataSync can preserve extant permissions of a source location.</p> </note>"""
    bytes_per_second: NotRequired["capo_datasync.types.bytes_per_second.BytesPerSecond"]
    """<p>Limits the bandwidth used by a DataSync task. For example, if you want DataSync to use a maximum of 1 MB, set this value to <code>1048576</code> (<code>=1024*1024</code>).</p>"""
    task_queueing: NotRequired["capo_datasync.types.task_queueing.TaskQueueing"]
    """<p>Specifies whether your transfer tasks should be put into a queue during certain scenarios when <a href="https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html#running-multiple-tasks">running multiple tasks</a>. This is <code>ENABLED</code> by default.</p>"""
    log_level: NotRequired["capo_datasync.types.log_level.LogLevel"]
    """<p>Specifies the type of logs that DataSync publishes to a Amazon CloudWatch Logs log group. To specify the log group, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html#DataSync-CreateTask-request-CloudWatchLogGroupArn">CloudWatchLogGroupArn</a>.</p> <ul> <li> <p> <code>BASIC</code> - Publishes logs with only basic information (such as transfer errors).</p> </li> <li> <p> <code>TRANSFER</code> - Publishes logs for all files or objects that your DataSync task transfers and performs data-integrity checks on.</p> </li> <li> <p> <code>OFF</code> - No logs are published.</p> </li> </ul>"""
    transfer_mode: NotRequired["capo_datasync.types.transfer_mode.TransferMode"]
    """<p>Specifies whether DataSync transfers only the data (including metadata) that differs between locations following an initial copy or transfers all data every time you run the task. If you're planning on recurring transfers, you might only want to transfer what's changed since your previous task execution.</p> <ul> <li> <p> <code>CHANGED</code> (default) - After your initial full transfer, DataSync copies only the data and metadata that differs between the source and destination location.</p> </li> <li> <p> <code>ALL</code> - DataSync copies everything in the source to the destination without comparing differences between the locations.</p> </li> </ul>"""
    security_descriptor_copy_flags: NotRequired[
        "capo_datasync.types.smb_security_descriptor_copy_flags.SmbSecurityDescriptorCopyFlags"
    ]
    """<p>Specifies which components of the SMB security descriptor are copied from source to destination objects. </p> <p>This value is only used for transfers between SMB and Amazon FSx for Windows File Server locations or between two FSx for Windows File Server locations. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html">Understanding how DataSync handles file and object metadata</a>.</p> <ul> <li> <p> <code>OWNER_DACL</code> (default) - For each copied object, DataSync copies the following metadata:</p> <ul> <li> <p>The object owner.</p> </li> <li> <p>NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object.</p> <p>DataSync won't copy NTFS system access control lists (SACLs) with this option.</p> </li> </ul> </li> <li> <p> <code>OWNER_DACL_SACL</code> - For each copied object, DataSync copies the following metadata:</p> <ul> <li> <p>The object owner.</p> </li> <li> <p>NTFS discretionary access control lists (DACLs), which determine whether to grant access to an object.</p> </li> <li> <p>SACLs, which are used by administrators to log attempts to access a secured object.</p> <p>Copying SACLs requires granting additional permissions to the Windows user that DataSync uses to access your SMB location. For information about choosing a user with the right permissions, see required permissions for <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions">SMB</a>, <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html#create-fsx-windows-location-permissions">FSx for Windows File Server</a>, or <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb">FSx for ONTAP</a> (depending on the type of location in your transfer).</p> </li> </ul> </li> <li> <p> <code>NONE</code> - None of the SMB security descriptor components are copied. Destination objects are owned by the user that was provided for accessing the destination location. DACLs and SACLs are set based on the destination server’s configuration. </p> </li> </ul>"""
    object_tags: NotRequired["capo_datasync.types.object_tags.ObjectTags"]
    """<p>Specifies whether you want DataSync to <code>PRESERVE</code> object tags (default behavior) when transferring between object storage systems. If you want your DataSync task to ignore object tags, specify the <code>NONE</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Options) -> dict:
    out: dict = {}
    if "verify_mode" in value:
        import capo_datasync.types.verify_mode

        out["VerifyMode"] = capo_datasync.types.verify_mode.serialize_aws_json_1_1(
            value["verify_mode"]
        )
    if "overwrite_mode" in value:
        import capo_datasync.types.overwrite_mode

        out["OverwriteMode"] = (
            capo_datasync.types.overwrite_mode.serialize_aws_json_1_1(
                value["overwrite_mode"]
            )
        )
    if "atime" in value:
        import capo_datasync.types.atime

        out["Atime"] = capo_datasync.types.atime.serialize_aws_json_1_1(value["atime"])
    if "mtime" in value:
        import capo_datasync.types.mtime

        out["Mtime"] = capo_datasync.types.mtime.serialize_aws_json_1_1(value["mtime"])
    if "uid" in value:
        import capo_datasync.types.uid

        out["Uid"] = capo_datasync.types.uid.serialize_aws_json_1_1(value["uid"])
    if "gid" in value:
        import capo_datasync.types.gid

        out["Gid"] = capo_datasync.types.gid.serialize_aws_json_1_1(value["gid"])
    if "preserve_deleted_files" in value:
        import capo_datasync.types.preserve_deleted_files

        out["PreserveDeletedFiles"] = (
            capo_datasync.types.preserve_deleted_files.serialize_aws_json_1_1(
                value["preserve_deleted_files"]
            )
        )
    if "preserve_devices" in value:
        import capo_datasync.types.preserve_devices

        out["PreserveDevices"] = (
            capo_datasync.types.preserve_devices.serialize_aws_json_1_1(
                value["preserve_devices"]
            )
        )
    if "posix_permissions" in value:
        import capo_datasync.types.posix_permissions

        out["PosixPermissions"] = (
            capo_datasync.types.posix_permissions.serialize_aws_json_1_1(
                value["posix_permissions"]
            )
        )
    if "bytes_per_second" in value:
        out["BytesPerSecond"] = value["bytes_per_second"]
    if "task_queueing" in value:
        import capo_datasync.types.task_queueing

        out["TaskQueueing"] = capo_datasync.types.task_queueing.serialize_aws_json_1_1(
            value["task_queueing"]
        )
    if "log_level" in value:
        import capo_datasync.types.log_level

        out["LogLevel"] = capo_datasync.types.log_level.serialize_aws_json_1_1(
            value["log_level"]
        )
    if "transfer_mode" in value:
        import capo_datasync.types.transfer_mode

        out["TransferMode"] = capo_datasync.types.transfer_mode.serialize_aws_json_1_1(
            value["transfer_mode"]
        )
    if "security_descriptor_copy_flags" in value:
        import capo_datasync.types.smb_security_descriptor_copy_flags

        out["SecurityDescriptorCopyFlags"] = (
            capo_datasync.types.smb_security_descriptor_copy_flags.serialize_aws_json_1_1(
                value["security_descriptor_copy_flags"]
            )
        )
    if "object_tags" in value:
        import capo_datasync.types.object_tags

        out["ObjectTags"] = capo_datasync.types.object_tags.serialize_aws_json_1_1(
            value["object_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Options:
    out: Options = {}  # type: ignore[typeddict-item]
    if data.get("VerifyMode") is not None:
        import capo_datasync.types.verify_mode

        out["verify_mode"] = capo_datasync.types.verify_mode.deserialize_aws_json_1_1(
            data["VerifyMode"]
        )
    if data.get("OverwriteMode") is not None:
        import capo_datasync.types.overwrite_mode

        out["overwrite_mode"] = (
            capo_datasync.types.overwrite_mode.deserialize_aws_json_1_1(
                data["OverwriteMode"]
            )
        )
    if data.get("Atime") is not None:
        import capo_datasync.types.atime

        out["atime"] = capo_datasync.types.atime.deserialize_aws_json_1_1(data["Atime"])
    if data.get("Mtime") is not None:
        import capo_datasync.types.mtime

        out["mtime"] = capo_datasync.types.mtime.deserialize_aws_json_1_1(data["Mtime"])
    if data.get("Uid") is not None:
        import capo_datasync.types.uid

        out["uid"] = capo_datasync.types.uid.deserialize_aws_json_1_1(data["Uid"])
    if data.get("Gid") is not None:
        import capo_datasync.types.gid

        out["gid"] = capo_datasync.types.gid.deserialize_aws_json_1_1(data["Gid"])
    if data.get("PreserveDeletedFiles") is not None:
        import capo_datasync.types.preserve_deleted_files

        out["preserve_deleted_files"] = (
            capo_datasync.types.preserve_deleted_files.deserialize_aws_json_1_1(
                data["PreserveDeletedFiles"]
            )
        )
    if data.get("PreserveDevices") is not None:
        import capo_datasync.types.preserve_devices

        out["preserve_devices"] = (
            capo_datasync.types.preserve_devices.deserialize_aws_json_1_1(
                data["PreserveDevices"]
            )
        )
    if data.get("PosixPermissions") is not None:
        import capo_datasync.types.posix_permissions

        out["posix_permissions"] = (
            capo_datasync.types.posix_permissions.deserialize_aws_json_1_1(
                data["PosixPermissions"]
            )
        )
    if data.get("BytesPerSecond") is not None:
        out["bytes_per_second"] = data["BytesPerSecond"]
    if data.get("TaskQueueing") is not None:
        import capo_datasync.types.task_queueing

        out["task_queueing"] = (
            capo_datasync.types.task_queueing.deserialize_aws_json_1_1(
                data["TaskQueueing"]
            )
        )
    if data.get("LogLevel") is not None:
        import capo_datasync.types.log_level

        out["log_level"] = capo_datasync.types.log_level.deserialize_aws_json_1_1(
            data["LogLevel"]
        )
    if data.get("TransferMode") is not None:
        import capo_datasync.types.transfer_mode

        out["transfer_mode"] = (
            capo_datasync.types.transfer_mode.deserialize_aws_json_1_1(
                data["TransferMode"]
            )
        )
    if data.get("SecurityDescriptorCopyFlags") is not None:
        import capo_datasync.types.smb_security_descriptor_copy_flags

        out["security_descriptor_copy_flags"] = (
            capo_datasync.types.smb_security_descriptor_copy_flags.deserialize_aws_json_1_1(
                data["SecurityDescriptorCopyFlags"]
            )
        )
    if data.get("ObjectTags") is not None:
        import capo_datasync.types.object_tags

        out["object_tags"] = capo_datasync.types.object_tags.deserialize_aws_json_1_1(
            data["ObjectTags"]
        )
    return out
