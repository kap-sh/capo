"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CreateDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_name
    import capo_bcm_dashboards.types.description
    import capo_bcm_dashboards.types.resource_tag_list
    import capo_bcm_dashboards.types.widget_list


class CreateDashboardRequest(TypedDict, closed=True):
    name: "capo_bcm_dashboards.types.dashboard_name.DashboardName"
    """<p>The name of the dashboard. The name must be unique within your account.</p>"""
    description: NotRequired["capo_bcm_dashboards.types.description.Description"]
    """<p>A description of the dashboard's purpose or contents.</p>"""
    widgets: "capo_bcm_dashboards.types.widget_list.WidgetList"
    """<p>An array of widget configurations that define the visualizations to be displayed in the dashboard. Each dashboard can contain up to 20 widgets.</p>"""
    resource_tags: NotRequired[
        "capo_bcm_dashboards.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The tags to apply to the dashboard resource for organization and management.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDashboardRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bcm_dashboards.types.widget_list

    out["widgets"] = capo_bcm_dashboards.types.widget_list.serialize_aws_json_1_0(
        value["widgets"]
    )
    if "resource_tags" in value:
        import capo_bcm_dashboards.types.resource_tag_list

        out["resourceTags"] = (
            capo_bcm_dashboards.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDashboardRequest:
    out: CreateDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("widgets") is not None:
        import capo_bcm_dashboards.types.widget_list

        out["widgets"] = capo_bcm_dashboards.types.widget_list.deserialize_aws_json_1_0(
            data["widgets"]
        )
    else:
        out["widgets"] = []
    if data.get("resourceTags") is not None:
        import capo_bcm_dashboards.types.resource_tag_list

        out["resource_tags"] = (
            capo_bcm_dashboards.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
