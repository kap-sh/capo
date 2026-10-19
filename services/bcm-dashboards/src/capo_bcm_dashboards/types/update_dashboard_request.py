"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#UpdateDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn
    import capo_bcm_dashboards.types.dashboard_name
    import capo_bcm_dashboards.types.description
    import capo_bcm_dashboards.types.widget_list


class UpdateDashboardRequest(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard to update.</p>"""
    name: "capo_bcm_dashboards.types.dashboard_name.DashboardName"
    """<p>The new name for the dashboard.</p>"""
    description: NotRequired["capo_bcm_dashboards.types.description.Description"]
    """<p>The new description for the dashboard.</p>"""
    widgets: NotRequired["capo_bcm_dashboards.types.widget_list.WidgetList"]
    """<p>The updated array of widget configurations for the dashboard. Replaces all existing widgets.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateDashboardRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "widgets" in value:
        import capo_bcm_dashboards.types.widget_list

        out["widgets"] = capo_bcm_dashboards.types.widget_list.serialize_aws_json_1_0(
            value["widgets"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateDashboardRequest:
    out: UpdateDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
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
    return out
