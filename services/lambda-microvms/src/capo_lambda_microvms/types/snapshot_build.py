"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#SnapshotBuild``."""

from typing_extensions import NotRequired, TypedDict


class SnapshotBuild(TypedDict, closed=True):
    memory_snapshot_size_in_bytes: NotRequired["int"]
    """<p>The size of the memory snapshot in bytes.</p>"""
    code_install_size_in_bytes: NotRequired["int"]
    """<p>The size of the installed code in bytes.</p>"""
    disk_snapshot_size_in_bytes: NotRequired["int"]
    """<p>The size of the disk snapshot in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotBuild) -> dict:
    out: dict = {}
    if "memory_snapshot_size_in_bytes" in value:
        out["memorySnapshotSizeInBytes"] = value["memory_snapshot_size_in_bytes"]
    if "code_install_size_in_bytes" in value:
        out["codeInstallSizeInBytes"] = value["code_install_size_in_bytes"]
    if "disk_snapshot_size_in_bytes" in value:
        out["diskSnapshotSizeInBytes"] = value["disk_snapshot_size_in_bytes"]
    return out


def deserialize_json(data: dict) -> SnapshotBuild:
    out: SnapshotBuild = {}  # type: ignore[typeddict-item]
    if data.get("memorySnapshotSizeInBytes") is not None:
        out["memory_snapshot_size_in_bytes"] = data["memorySnapshotSizeInBytes"]
    if data.get("codeInstallSizeInBytes") is not None:
        out["code_install_size_in_bytes"] = data["codeInstallSizeInBytes"]
    if data.get("diskSnapshotSizeInBytes") is not None:
        out["disk_snapshot_size_in_bytes"] = data["diskSnapshotSizeInBytes"]
    return out
