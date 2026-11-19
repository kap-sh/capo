"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceSnapshotsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.snapshot_list


class DescribeWorkspaceSnapshotsResult(TypedDict, closed=True):
    rebuild_snapshots: NotRequired["capo_workspaces.types.snapshot_list.SnapshotList"]
    """<p>Information about the snapshots that can be used to rebuild a WorkSpace. These snapshots include the user volume.</p>"""
    restore_snapshots: NotRequired["capo_workspaces.types.snapshot_list.SnapshotList"]
    """<p>Information about the snapshots that can be used to restore a WorkSpace. These snapshots include both the root volume and the user volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceSnapshotsResult) -> dict:
    out: dict = {}
    if "rebuild_snapshots" in value:
        import capo_workspaces.types.snapshot_list

        out["RebuildSnapshots"] = (
            capo_workspaces.types.snapshot_list.serialize_aws_json_1_1(
                value["rebuild_snapshots"]
            )
        )
    if "restore_snapshots" in value:
        import capo_workspaces.types.snapshot_list

        out["RestoreSnapshots"] = (
            capo_workspaces.types.snapshot_list.serialize_aws_json_1_1(
                value["restore_snapshots"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceSnapshotsResult:
    out: DescribeWorkspaceSnapshotsResult = {}  # type: ignore[typeddict-item]
    if data.get("RebuildSnapshots") is not None:
        import capo_workspaces.types.snapshot_list

        out["rebuild_snapshots"] = (
            capo_workspaces.types.snapshot_list.deserialize_aws_json_1_1(
                data["RebuildSnapshots"]
            )
        )
    if data.get("RestoreSnapshots") is not None:
        import capo_workspaces.types.snapshot_list

        out["restore_snapshots"] = (
            capo_workspaces.types.snapshot_list.deserialize_aws_json_1_1(
                data["RestoreSnapshots"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceSnapshotsResult) -> dict:
    out: dict = {}
    if "rebuild_snapshots" in value:
        import capo_workspaces.types.snapshot_list

        out["RebuildSnapshots"] = capo_workspaces.types.snapshot_list.serialize_cbor(
            value["rebuild_snapshots"]
        )
    if "restore_snapshots" in value:
        import capo_workspaces.types.snapshot_list

        out["RestoreSnapshots"] = capo_workspaces.types.snapshot_list.serialize_cbor(
            value["restore_snapshots"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspaceSnapshotsResult:
    out: DescribeWorkspaceSnapshotsResult = {}  # type: ignore[typeddict-item]
    if data.get("RebuildSnapshots") is not None:
        import capo_workspaces.types.snapshot_list

        out["rebuild_snapshots"] = capo_workspaces.types.snapshot_list.deserialize_cbor(
            data["RebuildSnapshots"]
        )
    if data.get("RestoreSnapshots") is not None:
        import capo_workspaces.types.snapshot_list

        out["restore_snapshots"] = capo_workspaces.types.snapshot_list.deserialize_cbor(
            data["RestoreSnapshots"]
        )
    return out
