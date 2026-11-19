"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportWorkspaceImageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_image_id


class ImportWorkspaceImageResult(TypedDict, closed=True):
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the WorkSpace image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportWorkspaceImageResult:
    out: ImportWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImportWorkspaceImageResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    return out


def deserialize_cbor(data: dict) -> ImportWorkspaceImageResult:
    out: ImportWorkspaceImageResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    return out
