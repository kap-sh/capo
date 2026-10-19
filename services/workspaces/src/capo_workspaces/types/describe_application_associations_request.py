"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeApplicationAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.application_associated_resource_type_list
    import capo_workspaces.types.limit
    import capo_workspaces.types.pagination_token
    import capo_workspaces.types.work_space_application_id


class DescribeApplicationAssociationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of associations to return.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results.</p>"""
    application_id: (
        "capo_workspaces.types.work_space_application_id.WorkSpaceApplicationId"
    )
    """<p>The identifier of the specified application.</p>"""
    associated_resource_types: "capo_workspaces.types.application_associated_resource_type_list.ApplicationAssociatedResourceTypeList"
    """<p>The resource type of the associated resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationAssociationsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["ApplicationId"] = value["application_id"]
    import capo_workspaces.types.application_associated_resource_type_list

    out["AssociatedResourceTypes"] = (
        capo_workspaces.types.application_associated_resource_type_list.serialize_aws_json_1_1(
            value["associated_resource_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationAssociationsRequest:
    out: DescribeApplicationAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        out["application_id"] = ""
    if data.get("AssociatedResourceTypes") is not None:
        import capo_workspaces.types.application_associated_resource_type_list

        out["associated_resource_types"] = (
            capo_workspaces.types.application_associated_resource_type_list.deserialize_aws_json_1_1(
                data["AssociatedResourceTypes"]
            )
        )
    else:
        out["associated_resource_types"] = []
    return out
