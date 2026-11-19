"""Generated from Smithy shape ``com.amazonaws.workspaces#ErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.description
    import capo_workspaces.types.workspace_image_error_detail_code


class ErrorDetails(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_workspaces.types.workspace_image_error_detail_code.WorkspaceImageErrorDetailCode"
    ]
    """<p>Indicates the error code returned.</p>"""
    error_message: NotRequired["capo_workspaces.types.description.Description"]
    """<p>The text of the error message related the error code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_workspaces.types.workspace_image_error_detail_code

        out["ErrorCode"] = (
            capo_workspaces.types.workspace_image_error_detail_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_workspaces.types.workspace_image_error_detail_code

        out["error_code"] = (
            capo_workspaces.types.workspace_image_error_detail_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_workspaces.types.workspace_image_error_detail_code

        out["ErrorCode"] = (
            capo_workspaces.types.workspace_image_error_detail_code.serialize_cbor(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_workspaces.types.workspace_image_error_detail_code

        out["error_code"] = (
            capo_workspaces.types.workspace_image_error_detail_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
