"""Generated from Smithy shape ``com.amazonaws.workspaces#StartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_id


class StartRequest(TypedDict, closed=True):
    workspace_id: NotRequired["capo_workspaces.types.workspace_id.WorkspaceId"]
    """<p>The identifier of the WorkSpace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartRequest) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartRequest:
    out: StartRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartRequest) -> dict:
    out: dict = {}
    if "workspace_id" in value:
        out["WorkspaceId"] = value["workspace_id"]
    return out


def deserialize_cbor(data: dict) -> StartRequest:
    out: StartRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    return out
