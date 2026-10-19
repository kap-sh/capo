"""Generated from Smithy shape ``com.amazonaws.cloudtrail#UpdateDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_arn
    import capo_cloudtrail.types.refresh_schedule
    import capo_cloudtrail.types.request_widget_list
    import capo_cloudtrail.types.termination_protection_enabled


class UpdateDashboardRequest(TypedDict, closed=True):
    dashboard_id: "capo_cloudtrail.types.dashboard_arn.DashboardArn"
    """<p> The name or ARN of the dashboard. </p>"""
    widgets: NotRequired["capo_cloudtrail.types.request_widget_list.RequestWidgetList"]
    """<p> An array of widgets for the dashboard. A custom dashboard can have a maximum of 10 widgets. </p> <p>To add new widgets, pass in an array that includes the existing widgets along with any new widgets. Run the <code>GetDashboard</code> operation to get the list of widgets for the dashboard.</p> <p>To remove widgets, pass in an array that includes the existing widgets minus the widgets you want removed.</p>"""
    refresh_schedule: NotRequired[
        "capo_cloudtrail.types.refresh_schedule.RefreshSchedule"
    ]
    """<p> The refresh schedule configuration for the dashboard. </p>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p> Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDashboardRequest) -> dict:
    out: dict = {}
    out["DashboardId"] = value["dashboard_id"]
    if "widgets" in value:
        import capo_cloudtrail.types.request_widget_list

        out["Widgets"] = (
            capo_cloudtrail.types.request_widget_list.serialize_aws_json_1_1(
                value["widgets"]
            )
        )
    if "refresh_schedule" in value:
        import capo_cloudtrail.types.refresh_schedule

        out["RefreshSchedule"] = (
            capo_cloudtrail.types.refresh_schedule.serialize_aws_json_1_1(
                value["refresh_schedule"]
            )
        )
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDashboardRequest:
    out: UpdateDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("DashboardId") is not None:
        out["dashboard_id"] = data["DashboardId"]
    else:
        out["dashboard_id"] = ""
    if data.get("Widgets") is not None:
        import capo_cloudtrail.types.request_widget_list

        out["widgets"] = (
            capo_cloudtrail.types.request_widget_list.deserialize_aws_json_1_1(
                data["Widgets"]
            )
        )
    if data.get("RefreshSchedule") is not None:
        import capo_cloudtrail.types.refresh_schedule

        out["refresh_schedule"] = (
            capo_cloudtrail.types.refresh_schedule.deserialize_aws_json_1_1(
                data["RefreshSchedule"]
            )
        )
    if data.get("TerminationProtectionEnabled") is not None:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    return out
