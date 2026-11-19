"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspacesPoolResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspaces_pool


class CreateWorkspacesPoolResult(TypedDict, closed=True):
    workspaces_pool: NotRequired["capo_workspaces.types.workspaces_pool.WorkspacesPool"]
    """<p>Indicates the pool to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspacesPoolResult) -> dict:
    out: dict = {}
    if "workspaces_pool" in value:
        import capo_workspaces.types.workspaces_pool

        out["WorkspacesPool"] = (
            capo_workspaces.types.workspaces_pool.serialize_aws_json_1_1(
                value["workspaces_pool"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspacesPoolResult:
    out: CreateWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspacesPool") is not None:
        import capo_workspaces.types.workspaces_pool

        out["workspaces_pool"] = (
            capo_workspaces.types.workspaces_pool.deserialize_aws_json_1_1(
                data["WorkspacesPool"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateWorkspacesPoolResult) -> dict:
    out: dict = {}
    if "workspaces_pool" in value:
        import capo_workspaces.types.workspaces_pool

        out["WorkspacesPool"] = capo_workspaces.types.workspaces_pool.serialize_cbor(
            value["workspaces_pool"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateWorkspacesPoolResult:
    out: CreateWorkspacesPoolResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspacesPool") is not None:
        import capo_workspaces.types.workspaces_pool

        out["workspaces_pool"] = capo_workspaces.types.workspaces_pool.deserialize_cbor(
            data["WorkspacesPool"]
        )
    return out
