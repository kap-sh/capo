"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionFoldersFailedDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.long


class TaskExecutionFoldersFailedDetail(TypedDict, closed=True):
    list: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync fails to list during your task execution.</p>"""
    prepare: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync fails to prepare during your task execution.</p>"""
    transfer: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync fails to transfer during your task execution.</p>"""
    verify: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync fails to verify during your task execution.</p>"""
    delete: "capo_datasync.types.long.long"
    """<p>The number of directories that DataSync fails to delete during your task execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionFoldersFailedDetail) -> dict:
    out: dict = {}
    out["List"] = value.get("list", 0)
    out["Prepare"] = value.get("prepare", 0)
    out["Transfer"] = value.get("transfer", 0)
    out["Verify"] = value.get("verify", 0)
    out["Delete"] = value.get("delete", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionFoldersFailedDetail:
    out: TaskExecutionFoldersFailedDetail = {}  # type: ignore[typeddict-item]
    if data.get("List") is not None:
        out["list"] = data["List"]
    else:
        out["list"] = 0
    if data.get("Prepare") is not None:
        out["prepare"] = data["Prepare"]
    else:
        out["prepare"] = 0
    if data.get("Transfer") is not None:
        out["transfer"] = data["Transfer"]
    else:
        out["transfer"] = 0
    if data.get("Verify") is not None:
        out["verify"] = data["Verify"]
    else:
        out["verify"] = 0
    if data.get("Delete") is not None:
        out["delete"] = data["Delete"]
    else:
        out["delete"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaskExecutionFoldersFailedDetail) -> dict:
    out: dict = {}
    out["List"] = value.get("list", 0)
    out["Prepare"] = value.get("prepare", 0)
    out["Transfer"] = value.get("transfer", 0)
    out["Verify"] = value.get("verify", 0)
    out["Delete"] = value.get("delete", 0)
    return out


def deserialize_cbor(data: dict) -> TaskExecutionFoldersFailedDetail:
    out: TaskExecutionFoldersFailedDetail = {}  # type: ignore[typeddict-item]
    if data.get("List") is not None:
        out["list"] = data["List"]
    else:
        out["list"] = 0
    if data.get("Prepare") is not None:
        out["prepare"] = data["Prepare"]
    else:
        out["prepare"] = 0
    if data.get("Transfer") is not None:
        out["transfer"] = data["Transfer"]
    else:
        out["transfer"] = 0
    if data.get("Verify") is not None:
        out["verify"] = data["Verify"]
    else:
        out["verify"] = 0
    if data.get("Delete") is not None:
        out["delete"] = data["Delete"]
    else:
        out["delete"] = 0
    return out
