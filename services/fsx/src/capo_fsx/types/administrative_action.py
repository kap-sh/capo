"""Generated from Smithy shape ``com.amazonaws.fsx#AdministrativeAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.administrative_action_failure_details
    import capo_fsx.types.administrative_action_type
    import capo_fsx.types.error_message
    import capo_fsx.types.file_system
    import capo_fsx.types.progress_percent
    import capo_fsx.types.remaining_transfer_bytes
    import capo_fsx.types.request_time
    import capo_fsx.types.snapshot
    import capo_fsx.types.status
    import capo_fsx.types.total_transfer_bytes
    import capo_fsx.types.volume


class AdministrativeAction(TypedDict, closed=True):
    administrative_action_type: NotRequired[
        "capo_fsx.types.administrative_action_type.AdministrativeActionType"
    ]
    progress_percent: NotRequired["capo_fsx.types.progress_percent.ProgressPercent"]
    """<p>The percentage-complete status of a <code>STORAGE_OPTIMIZATION</code> or <code>DOWNLOAD_DATA_FROM_BACKUP</code> administrative action. Does not apply to any other administrative action type.</p>"""
    request_time: NotRequired["capo_fsx.types.request_time.RequestTime"]
    """<p>The time that the administrative action request was received.</p>"""
    status: NotRequired["capo_fsx.types.status.Status"]
    """<p>The status of the administrative action, as follows:</p> <ul> <li> <p> <code>FAILED</code> - Amazon FSx failed to process the administrative action successfully.</p> </li> <li> <p> <code>IN_PROGRESS</code> - Amazon FSx is processing the administrative action.</p> </li> <li> <p> <code>PENDING</code> - Amazon FSx is waiting to process the administrative action.</p> </li> <li> <p> <code>COMPLETED</code> - Amazon FSx has finished processing the administrative task.</p> <p>For a backup restore to a second-generation FSx for ONTAP file system, indicates that all data has been downloaded to the volume, and clients now have read-write access to volume.</p> </li> <li> <p> <code>UPDATED_OPTIMIZING</code> - For a storage-capacity increase update, Amazon FSx has updated the file system with the new storage capacity, and is now performing the storage-optimization process.</p> </li> <li> <p> <code>PENDING</code> - For a backup restore to a second-generation FSx for ONTAP file system, indicates that the file metadata is being downloaded onto the volume. The volume's Lifecycle state is CREATING.</p> </li> <li> <p> <code>IN_PROGRESS</code> - For a backup restore to a second-generation FSx for ONTAP file system, indicates that all metadata has been downloaded to the new volume and client can access data with read-only access while Amazon FSx downloads the file data to the volume. Track the progress of this process with the <code>ProgressPercent</code> element.</p> </li> </ul>"""
    target_file_system_values: NotRequired["capo_fsx.types.file_system.FileSystem"]
    """<p>The target value for the administration action, provided in the <code>UpdateFileSystem</code> operation. Returned for <code>FILE_SYSTEM_UPDATE</code> administrative actions. </p>"""
    failure_details: NotRequired[
        "capo_fsx.types.administrative_action_failure_details.AdministrativeActionFailureDetails"
    ]
    target_volume_values: NotRequired["capo_fsx.types.volume.Volume"]
    target_snapshot_values: NotRequired["capo_fsx.types.snapshot.Snapshot"]
    total_transfer_bytes: NotRequired[
        "capo_fsx.types.total_transfer_bytes.TotalTransferBytes"
    ]
    """<p>The number of bytes that have transferred for the FSx for OpenZFS snapshot that you're copying.</p>"""
    remaining_transfer_bytes: NotRequired[
        "capo_fsx.types.remaining_transfer_bytes.RemainingTransferBytes"
    ]
    """<p>The remaining bytes to transfer for the FSx for OpenZFS snapshot that you're copying.</p>"""
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdministrativeAction) -> dict:
    out: dict = {}
    if "administrative_action_type" in value:
        import capo_fsx.types.administrative_action_type

        out["AdministrativeActionType"] = (
            capo_fsx.types.administrative_action_type.serialize_aws_json_1_1(
                value["administrative_action_type"]
            )
        )
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    if "request_time" in value:
        import capo_fsx.types.request_time

        out["RequestTime"] = capo_fsx.types.request_time.serialize_aws_json_1_1(
            value["request_time"]
        )
    if "status" in value:
        import capo_fsx.types.status

        out["Status"] = capo_fsx.types.status.serialize_aws_json_1_1(value["status"])
    if "target_file_system_values" in value:
        import capo_fsx.types.file_system

        out["TargetFileSystemValues"] = (
            capo_fsx.types.file_system.serialize_aws_json_1_1(
                value["target_file_system_values"]
            )
        )
    if "failure_details" in value:
        import capo_fsx.types.administrative_action_failure_details

        out["FailureDetails"] = (
            capo_fsx.types.administrative_action_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "target_volume_values" in value:
        import capo_fsx.types.volume

        out["TargetVolumeValues"] = capo_fsx.types.volume.serialize_aws_json_1_1(
            value["target_volume_values"]
        )
    if "target_snapshot_values" in value:
        import capo_fsx.types.snapshot

        out["TargetSnapshotValues"] = capo_fsx.types.snapshot.serialize_aws_json_1_1(
            value["target_snapshot_values"]
        )
    if "total_transfer_bytes" in value:
        out["TotalTransferBytes"] = value["total_transfer_bytes"]
    if "remaining_transfer_bytes" in value:
        out["RemainingTransferBytes"] = value["remaining_transfer_bytes"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdministrativeAction:
    out: AdministrativeAction = {}  # type: ignore[typeddict-item]
    if data.get("AdministrativeActionType") is not None:
        import capo_fsx.types.administrative_action_type

        out["administrative_action_type"] = (
            capo_fsx.types.administrative_action_type.deserialize_aws_json_1_1(
                data["AdministrativeActionType"]
            )
        )
    if data.get("ProgressPercent") is not None:
        out["progress_percent"] = data["ProgressPercent"]
    if data.get("RequestTime") is not None:
        import capo_fsx.types.request_time

        out["request_time"] = capo_fsx.types.request_time.deserialize_aws_json_1_1(
            data["RequestTime"]
        )
    if data.get("Status") is not None:
        import capo_fsx.types.status

        out["status"] = capo_fsx.types.status.deserialize_aws_json_1_1(data["Status"])
    if data.get("TargetFileSystemValues") is not None:
        import capo_fsx.types.file_system

        out["target_file_system_values"] = (
            capo_fsx.types.file_system.deserialize_aws_json_1_1(
                data["TargetFileSystemValues"]
            )
        )
    if data.get("FailureDetails") is not None:
        import capo_fsx.types.administrative_action_failure_details

        out["failure_details"] = (
            capo_fsx.types.administrative_action_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if data.get("TargetVolumeValues") is not None:
        import capo_fsx.types.volume

        out["target_volume_values"] = capo_fsx.types.volume.deserialize_aws_json_1_1(
            data["TargetVolumeValues"]
        )
    if data.get("TargetSnapshotValues") is not None:
        import capo_fsx.types.snapshot

        out["target_snapshot_values"] = (
            capo_fsx.types.snapshot.deserialize_aws_json_1_1(
                data["TargetSnapshotValues"]
            )
        )
    if data.get("TotalTransferBytes") is not None:
        out["total_transfer_bytes"] = data["TotalTransferBytes"]
    if data.get("RemainingTransferBytes") is not None:
        out["remaining_transfer_bytes"] = data["RemainingTransferBytes"]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


def redact_sensitive(value: AdministrativeAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_file_system_values" in value:
        import capo_fsx.types.file_system

        out["target_file_system_values"] = capo_fsx.types.file_system.redact_sensitive(
            value["target_file_system_values"]
        )
    if "target_volume_values" in value:
        import capo_fsx.types.volume

        out["target_volume_values"] = capo_fsx.types.volume.redact_sensitive(
            value["target_volume_values"]
        )
    if "target_snapshot_values" in value:
        import capo_fsx.types.snapshot

        out["target_snapshot_values"] = capo_fsx.types.snapshot.redact_sensitive(
            value["target_snapshot_values"]
        )
    return out
