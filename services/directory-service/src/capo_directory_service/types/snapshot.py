"""Generated from Smithy shape ``com.amazonaws.directoryservice#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.snapshot_id
    import capo_directory_service.types.snapshot_name
    import capo_directory_service.types.snapshot_status
    import capo_directory_service.types.snapshot_type
    import capo_directory_service.types.start_time


class Snapshot(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>The directory identifier.</p>"""
    snapshot_id: NotRequired["capo_directory_service.types.snapshot_id.SnapshotId"]
    """<p>The snapshot identifier.</p>"""
    type: NotRequired["capo_directory_service.types.snapshot_type.SnapshotType"]
    """<p>The snapshot type.</p>"""
    name: NotRequired["capo_directory_service.types.snapshot_name.SnapshotName"]
    """<p>The descriptive name of the snapshot.</p>"""
    status: NotRequired["capo_directory_service.types.snapshot_status.SnapshotStatus"]
    """<p>The snapshot status.</p>"""
    start_time: NotRequired["capo_directory_service.types.start_time.StartTime"]
    """<p>The date and time that the snapshot was taken.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "type" in value:
        import capo_directory_service.types.snapshot_type

        out["Type"] = capo_directory_service.types.snapshot_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_directory_service.types.snapshot_status

        out["Status"] = (
            capo_directory_service.types.snapshot_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_directory_service.types.start_time

        out["StartTime"] = (
            capo_directory_service.types.start_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("Type") is not None:
        import capo_directory_service.types.snapshot_type

        out["type"] = (
            capo_directory_service.types.snapshot_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_directory_service.types.snapshot_status

        out["status"] = (
            capo_directory_service.types.snapshot_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_directory_service.types.start_time

        out["start_time"] = (
            capo_directory_service.types.start_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Snapshot) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "type" in value:
        import capo_directory_service.types.snapshot_type

        out["Type"] = capo_directory_service.types.snapshot_type.serialize_cbor(
            value["type"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_directory_service.types.snapshot_status

        out["Status"] = capo_directory_service.types.snapshot_status.serialize_cbor(
            value["status"]
        )
    if "start_time" in value:
        import capo_directory_service.types.start_time

        out["StartTime"] = capo_directory_service.types.start_time.serialize_cbor(
            value["start_time"]
        )
    return out


def deserialize_cbor(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("Type") is not None:
        import capo_directory_service.types.snapshot_type

        out["type"] = capo_directory_service.types.snapshot_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_directory_service.types.snapshot_status

        out["status"] = capo_directory_service.types.snapshot_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("StartTime") is not None:
        import capo_directory_service.types.start_time

        out["start_time"] = capo_directory_service.types.start_time.deserialize_cbor(
            data["StartTime"]
        )
    return out
