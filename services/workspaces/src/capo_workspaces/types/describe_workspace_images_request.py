"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.image_type
    import capo_workspaces.types.limit
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.workspace_image_id_list


class DescribeWorkspaceImagesRequest(TypedDict, closed=True):
    image_ids: NotRequired[
        "capo_workspaces.types.workspace_image_id_list.WorkspaceImageIdList"
    ]
    """<p>The identifier of the image.</p>"""
    image_type: NotRequired["capo_workspaces.types.image_type.ImageType"]
    """<p>The type (owned or shared) of the image.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceImagesRequest) -> dict:
    out: dict = {}
    if "image_ids" in value:
        import capo_workspaces.types.workspace_image_id_list

        out["ImageIds"] = (
            capo_workspaces.types.workspace_image_id_list.serialize_aws_json_1_1(
                value["image_ids"]
            )
        )
    if "image_type" in value:
        import capo_workspaces.types.image_type

        out["ImageType"] = capo_workspaces.types.image_type.serialize_aws_json_1_1(
            value["image_type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceImagesRequest:
    out: DescribeWorkspaceImagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageIds") is not None:
        import capo_workspaces.types.workspace_image_id_list

        out["image_ids"] = (
            capo_workspaces.types.workspace_image_id_list.deserialize_aws_json_1_1(
                data["ImageIds"]
            )
        )
    if data.get("ImageType") is not None:
        import capo_workspaces.types.image_type

        out["image_type"] = capo_workspaces.types.image_type.deserialize_aws_json_1_1(
            data["ImageType"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeWorkspaceImagesRequest) -> dict:
    out: dict = {}
    if "image_ids" in value:
        import capo_workspaces.types.workspace_image_id_list

        out["ImageIds"] = capo_workspaces.types.workspace_image_id_list.serialize_cbor(
            value["image_ids"]
        )
    if "image_type" in value:
        import capo_workspaces.types.image_type

        out["ImageType"] = capo_workspaces.types.image_type.serialize_cbor(
            value["image_type"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> DescribeWorkspaceImagesRequest:
    out: DescribeWorkspaceImagesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageIds") is not None:
        import capo_workspaces.types.workspace_image_id_list

        out["image_ids"] = (
            capo_workspaces.types.workspace_image_id_list.deserialize_cbor(
                data["ImageIds"]
            )
        )
    if data.get("ImageType") is not None:
        import capo_workspaces.types.image_type

        out["image_type"] = capo_workspaces.types.image_type.deserialize_cbor(
            data["ImageType"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
