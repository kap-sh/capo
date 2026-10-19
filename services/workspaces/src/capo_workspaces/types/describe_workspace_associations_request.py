"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.work_space_associated_resource_type_list
    import capo_workspaces.types.workspace_id


class DescribeWorkspaceAssociationsRequest(TypedDict, closed=True):
    workspace_id: "capo_workspaces.types.workspace_id.WorkspaceId"
    """<p>The identifier of the WorkSpace.</p>"""
    associated_resource_types: "capo_workspaces.types.work_space_associated_resource_type_list.WorkSpaceAssociatedResourceTypeList"
    """<p>The resource types of the associated resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceAssociationsRequest) -> dict:
    out: dict = {}
    out["WorkspaceId"] = value["workspace_id"]
    import capo_workspaces.types.work_space_associated_resource_type_list

    out["AssociatedResourceTypes"] = (
        capo_workspaces.types.work_space_associated_resource_type_list.serialize_aws_json_1_1(
            value["associated_resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceAssociationsRequest:
    out: DescribeWorkspaceAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkspaceId") is not None:
        out["workspace_id"] = data["WorkspaceId"]
    else:
        out["workspace_id"] = ""
    if data.get("AssociatedResourceTypes") is not None:
        import capo_workspaces.types.work_space_associated_resource_type_list

        out["associated_resource_types"] = (
            capo_workspaces.types.work_space_associated_resource_type_list.deserialize_aws_json_1_1(
                data["AssociatedResourceTypes"]
            )
        )
    else:
        out["associated_resource_types"] = []
    return out
