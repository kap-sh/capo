"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspaceBundleResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_bundle


class CreateWorkspaceBundleResult(TypedDict, closed=True):
    workspace_bundle: NotRequired[
        "capo_workspaces.types.workspace_bundle.WorkspaceBundle"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspaceBundleResult) -> dict:
    out: dict = {}
    if "workspace_bundle" in value:
        import capo_workspaces.types.workspace_bundle

        out["WorkspaceBundle"] = (
            capo_workspaces.types.workspace_bundle.serialize_aws_json_1_1(
                value["workspace_bundle"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspaceBundleResult:
    out: CreateWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceBundle") is not None:
        import capo_workspaces.types.workspace_bundle

        out["workspace_bundle"] = (
            capo_workspaces.types.workspace_bundle.deserialize_aws_json_1_1(
                data["WorkspaceBundle"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateWorkspaceBundleResult) -> dict:
    out: dict = {}
    if "workspace_bundle" in value:
        import capo_workspaces.types.workspace_bundle

        out["WorkspaceBundle"] = capo_workspaces.types.workspace_bundle.serialize_cbor(
            value["workspace_bundle"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateWorkspaceBundleResult:
    out: CreateWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceBundle") is not None:
        import capo_workspaces.types.workspace_bundle

        out["workspace_bundle"] = (
            capo_workspaces.types.workspace_bundle.deserialize_cbor(
                data["WorkspaceBundle"]
            )
        )
    return out
