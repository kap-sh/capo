"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceImagePermissionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.image_permissions
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspace_image_id


class DescribeWorkspaceImagePermissionsResult(TypedDict, closed=True):
    image_id: NotRequired["capo_workspaces.types.workspace_image_id.WorkspaceImageId"]
    """<p>The identifier of the image.</p>"""
    image_permissions: NotRequired[
        "capo_workspaces.types.image_permissions.ImagePermissions"
    ]
    """<p>The identifiers of the Amazon Web Services accounts that the image has been shared with.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceImagePermissionsResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "image_permissions" in value:
        import capo_workspaces.types.image_permissions

        out["ImagePermissions"] = (
            capo_workspaces.types.image_permissions.serialize_aws_json_1_1(
                value["image_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceImagePermissionsResult:
    out: DescribeWorkspaceImagePermissionsResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("ImagePermissions") is not None:
        import capo_workspaces.types.image_permissions

        out["image_permissions"] = (
            capo_workspaces.types.image_permissions.deserialize_aws_json_1_1(
                data["ImagePermissions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceImagePermissionsResult) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "image_permissions" in value:
        import capo_workspaces.types.image_permissions

        out["ImagePermissions"] = (
            capo_workspaces.types.image_permissions.serialize_cbor(
                value["image_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspaceImagePermissionsResult:
    out: DescribeWorkspaceImagePermissionsResult = {}  # type: ignore[typeddict-item]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("ImagePermissions") is not None:
        import capo_workspaces.types.image_permissions

        out["image_permissions"] = (
            capo_workspaces.types.image_permissions.deserialize_cbor(
                data["ImagePermissions"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
