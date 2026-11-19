"""Generated from Smithy shape ``com.amazonaws.workspaces#StartWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_id


class StartWorkspacesPoolRequest(TypedDict, closed=True):
    pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkspacesPoolRequest:
    out: StartWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_cbor(data: dict) -> StartWorkspacesPoolRequest:
    out: StartWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    return out
