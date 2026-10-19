"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_image_id


class DeleteWorkspaceImageRequest(TypedDict, closed=True):
    image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWorkspaceImageRequest:
    out: DeleteWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    else:
        out["image_id"] = ""
    return out
