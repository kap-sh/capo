"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.link_sharing_configuration
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.update_resource_permission_list


class DescribeDashboardPermissionsResponse(TypedDict, closed=True):
    dashboard_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the dashboard.</p>"""
    dashboard_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A structure that contains the permissions for the dashboard.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    link_sharing_configuration: NotRequired[
        "capo_quicksight.types.link_sharing_configuration.LinkSharingConfiguration"
    ]
    """<p>A structure that contains the configuration of a shareable link that grants access to the dashboard. Your users can use the link to view and interact with the dashboard, if the dashboard has been shared with them. For more information about sharing dashboards, see <a href="https://docs.aws.amazon.com/quicksight/latest/user/sharing-a-dashboard.html">Sharing Dashboards</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardPermissionsResponse) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "permissions" in value:
        import capo_quicksight.types.update_resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.update_resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "link_sharing_configuration" in value:
        import capo_quicksight.types.link_sharing_configuration

        out["LinkSharingConfiguration"] = (
            capo_quicksight.types.link_sharing_configuration.serialize_json(
                value["link_sharing_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDashboardPermissionsResponse:
    out: DescribeDashboardPermissionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    if data.get("DashboardArn") is not None:
        out["dashboard_arn"] = data["DashboardArn"]
    if data.get("Permissions") is not None:
        import capo_quicksight.types.update_resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.update_resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    if data.get("LinkSharingConfiguration") is not None:
        import capo_quicksight.types.link_sharing_configuration

        out["link_sharing_configuration"] = (
            capo_quicksight.types.link_sharing_configuration.deserialize_json(
                data["LinkSharingConfiguration"]
            )
        )
    return out
