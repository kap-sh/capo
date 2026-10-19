"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduledReportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn
    import capo_bcm_dashboards.types.generic_string
    import capo_bcm_dashboards.types.health_status
    import capo_bcm_dashboards.types.schedule_state
    import capo_bcm_dashboards.types.scheduled_report_arn
    import capo_bcm_dashboards.types.scheduled_report_name
    import capo_bcm_dashboards.types.widget_id_list


class ScheduledReportSummary(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the scheduled report.</p>"""
    name: "capo_bcm_dashboards.types.scheduled_report_name.ScheduledReportName"
    """<p>The name of the scheduled report.</p>"""
    dashboard_arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard associated with the scheduled report.</p>"""
    schedule_expression: "capo_bcm_dashboards.types.generic_string.GenericString"
    """<p>The schedule expression that defines when the report runs.</p>"""
    state: "capo_bcm_dashboards.types.schedule_state.ScheduleState"
    """<p>The state of the schedule: <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    health_status: "capo_bcm_dashboards.types.health_status.HealthStatus"
    """<p>The health status of the scheduled report as of its last refresh time.</p>"""
    schedule_expression_time_zone: NotRequired[
        "capo_bcm_dashboards.types.generic_string.GenericString"
    ]
    """<p>The time zone for the schedule expression, for example, <code>UTC</code>.</p>"""
    widget_ids: NotRequired["capo_bcm_dashboards.types.widget_id_list.WidgetIdList"]
    """<p>The list of widget identifiers included in the scheduled report.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledReportSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["dashboardArn"] = value["dashboard_arn"]
    out["scheduleExpression"] = value["schedule_expression"]
    import capo_bcm_dashboards.types.schedule_state

    out["state"] = capo_bcm_dashboards.types.schedule_state.serialize_aws_json_1_0(
        value["state"]
    )
    import capo_bcm_dashboards.types.health_status

    out["healthStatus"] = (
        capo_bcm_dashboards.types.health_status.serialize_aws_json_1_0(
            value["health_status"]
        )
    )
    if "schedule_expression_time_zone" in value:
        out["scheduleExpressionTimeZone"] = value["schedule_expression_time_zone"]
    if "widget_ids" in value:
        import capo_bcm_dashboards.types.widget_id_list

        out["widgetIds"] = (
            capo_bcm_dashboards.types.widget_id_list.serialize_aws_json_1_0(
                value["widget_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledReportSummary:
    out: ScheduledReportSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dashboardArn") is not None:
        out["dashboard_arn"] = data["dashboardArn"]
    else:
        out["dashboard_arn"] = ""
    if data.get("scheduleExpression") is not None:
        out["schedule_expression"] = data["scheduleExpression"]
    else:
        out["schedule_expression"] = ""
    if data.get("state") is not None:
        import capo_bcm_dashboards.types.schedule_state

        out["state"] = (
            capo_bcm_dashboards.types.schedule_state.deserialize_aws_json_1_0(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_bcm_dashboards.types.schedule_state.ScheduleState", ""
        )
    if data.get("healthStatus") is not None:
        import capo_bcm_dashboards.types.health_status

        out["health_status"] = (
            capo_bcm_dashboards.types.health_status.deserialize_aws_json_1_0(
                data["healthStatus"]
            )
        )
    else:
        raise DeserializationError("ScheduledReportSummary.health_status required")
    if data.get("scheduleExpressionTimeZone") is not None:
        out["schedule_expression_time_zone"] = data["scheduleExpressionTimeZone"]
    if data.get("widgetIds") is not None:
        import capo_bcm_dashboards.types.widget_id_list

        out["widget_ids"] = (
            capo_bcm_dashboards.types.widget_id_list.deserialize_aws_json_1_0(
                data["widgetIds"]
            )
        )
    return out
