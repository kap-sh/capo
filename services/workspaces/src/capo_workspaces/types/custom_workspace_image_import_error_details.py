"""Generated from Smithy shape ``com.amazonaws.workspaces#CustomWorkspaceImageImportErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.error_code
    import capo_workspaces.types.image_error_message


class CustomWorkspaceImageImportErrorDetails(TypedDict, closed=True):
    error_code: NotRequired["capo_workspaces.types.error_code.ErrorCode"]
    """<p>The error code that is returned for the image import.</p>"""
    error_message: NotRequired[
        "capo_workspaces.types.image_error_message.ImageErrorMessage"
    ]
    """<p>The text of the error message that is returned for the image import.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomWorkspaceImageImportErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomWorkspaceImageImportErrorDetails:
    out: CustomWorkspaceImageImportErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomWorkspaceImageImportErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> CustomWorkspaceImageImportErrorDetails:
    out: CustomWorkspaceImageImportErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
