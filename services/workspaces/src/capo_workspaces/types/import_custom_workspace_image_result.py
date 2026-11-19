"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportCustomWorkspaceImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.custom_workspace_image_import_state
    import capo_workspaces.types.workspace_image_id


class ImportCustomWorkspaceImageResult(TypedDict, closed=True):
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the WorkSpace image.</p>"""
    state: NotRequired[
        "capo_workspaces.types.custom_workspace_image_import_state.CustomWorkspaceImageImportState"
    ]
    """<p>The state of the WorkSpace image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportCustomWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "state" in value:
        import capo_workspaces.types.custom_workspace_image_import_state

        out["State"] = (
            capo_workspaces.types.custom_workspace_image_import_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportCustomWorkspaceImageResult:
    out: ImportCustomWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("State") is not None:
        import capo_workspaces.types.custom_workspace_image_import_state

        out["state"] = (
            capo_workspaces.types.custom_workspace_image_import_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportCustomWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "state" in value:
        import capo_workspaces.types.custom_workspace_image_import_state

        out["State"] = (
            capo_workspaces.types.custom_workspace_image_import_state.serialize_cbor(
                value["state"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ImportCustomWorkspaceImageResult:
    out: ImportCustomWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("State") is not None:
        import capo_workspaces.types.custom_workspace_image_import_state

        out["state"] = (
            capo_workspaces.types.custom_workspace_image_import_state.deserialize_cbor(
                data["State"]
            )
        )
    return out
