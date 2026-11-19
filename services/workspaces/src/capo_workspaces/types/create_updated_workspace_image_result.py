"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateUpdatedWorkspaceImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_image_id


class CreateUpdatedWorkspaceImageResult(TypedDict, closed=True):
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the new updated WorkSpace image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUpdatedWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUpdatedWorkspaceImageResult:
    out: CreateUpdatedWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateUpdatedWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_cbor(data: dict) -> CreateUpdatedWorkspaceImageResult:
    out: CreateUpdatedWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    return out
