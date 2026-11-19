"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.error_message
    import capo_workspaces.types.workspaces_pool_error_code


class WorkspacesPoolError(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_workspaces.types.workspaces_pool_error_code.WorkspacesPoolErrorCode"
    ]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_workspaces.types.error_message.ErrorMessage"]
    """<p>The error message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesPoolError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_workspaces.types.workspaces_pool_error_code

        out["ErrorCode"] = (
            capo_workspaces.types.workspaces_pool_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesPoolError:
    out: WorkspacesPoolError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_workspaces.types.workspaces_pool_error_code

        out["error_code"] = (
            capo_workspaces.types.workspaces_pool_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WorkspacesPoolError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_workspaces.types.workspaces_pool_error_code

        out["ErrorCode"] = (
            capo_workspaces.types.workspaces_pool_error_code.serialize_cbor(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> WorkspacesPoolError:
    out: WorkspacesPoolError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_workspaces.types.workspaces_pool_error_code

        out["error_code"] = (
            capo_workspaces.types.workspaces_pool_error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
