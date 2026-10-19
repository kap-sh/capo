"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateWorkspaceImagePermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aws_account
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.workspace_image_id


class UpdateWorkspaceImagePermissionRequest(TypedDict, closed=True):
    image_id: "capo_workspaces.types.workspace_image_id.WorkspaceImageId"
    """<p>The identifier of the image.</p>"""
    allow_copy_image: "capo_workspaces.types.boolean_object.BooleanObject"
    """<p>The permission to copy the image. This permission can be revoked only after an image has been shared.</p>"""
    shared_account_id: "capo_workspaces.types.aws_account.AwsAccount"
    """<p>The identifier of the Amazon Web Services account to share or unshare the image with.</p> <important> <p>Before sharing the image, confirm that you are sharing to the correct Amazon Web Services account ID.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkspaceImagePermissionRequest) -> dict:
    out: dict = {}
    out["ImageId"] = value["image_id"]
    out["AllowCopyImage"] = value["allow_copy_image"]
    out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkspaceImagePermissionRequest:
    out: UpdateWorkspaceImagePermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    else:
        out["image_id"] = ""
    if data.get("AllowCopyImage") is not None:
        out["allow_copy_image"] = data["AllowCopyImage"]
    else:
        out["allow_copy_image"] = False
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    else:
        out["shared_account_id"] = ""
    return out
