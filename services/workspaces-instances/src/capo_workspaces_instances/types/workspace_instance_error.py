"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#WorkspaceInstanceError``."""

from typing_extensions import NotRequired, TypedDict


class WorkspaceInstanceError(TypedDict, closed=True):
    error_code: NotRequired["str"]
    """<p>Unique error code for the WorkSpace Instance error.</p>"""
    error_message: NotRequired["str"]
    """<p>Detailed description of the WorkSpace Instance error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkspaceInstanceError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkspaceInstanceError:
    out: WorkspaceInstanceError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspaceInstanceError) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> WorkspaceInstanceError:
    out: WorkspaceInstanceError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
