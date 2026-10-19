"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool_id


class TerminateWorkspacesPoolRequest(TypedDict, closed=True):
    pool_id: "capo_workspaces.types.workspaces_pool_id.WorkspacesPoolId"
    """<p>The identifier of the pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesPoolRequest) -> dict:
    out: dict = {}
    out["PoolId"] = value["pool_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesPoolRequest:
    out: TerminateWorkspacesPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolId") is not None:
        out["pool_id"] = data["PoolId"]
    else:
        out["pool_id"] = ""
    return out
