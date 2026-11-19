"""Generated from Smithy shape ``com.amazonaws.datasync#TaskExecutionFilesFailedDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.long


class TaskExecutionFilesFailedDetail(TypedDict, closed=True):
    prepare: "capo_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to prepare during your task execution.</p>"""
    transfer: "capo_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to transfer during your task execution.</p>"""
    verify: "capo_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to verify during your task execution.</p>"""
    delete: "capo_datasync.types.long.long"
    """<p>The number of files or objects that DataSync fails to delete during your task execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskExecutionFilesFailedDetail) -> dict:
    out: dict = {}
    out["Prepare"] = value.get("prepare", 0)
    out["Transfer"] = value.get("transfer", 0)
    out["Verify"] = value.get("verify", 0)
    out["Delete"] = value.get("delete", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskExecutionFilesFailedDetail:
    out: TaskExecutionFilesFailedDetail = {}  # type: ignore[typeddict-item]
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
def serialize_cbor(value: TaskExecutionFilesFailedDetail) -> dict:
    out: dict = {}
    out["Prepare"] = value.get("prepare", 0)
    out["Transfer"] = value.get("transfer", 0)
    out["Verify"] = value.get("verify", 0)
    out["Delete"] = value.get("delete", 0)
    return out


def deserialize_cbor(data: dict) -> TaskExecutionFilesFailedDetail:
    out: TaskExecutionFilesFailedDetail = {}  # type: ignore[typeddict-item]
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
