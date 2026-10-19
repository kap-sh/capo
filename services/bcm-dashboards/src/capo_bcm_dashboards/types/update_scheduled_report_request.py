"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#UpdateScheduledReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn
    import capo_bcm_dashboards.types.date_time_range
    import capo_bcm_dashboards.types.description
    import capo_bcm_dashboards.types.schedule_config
    import capo_bcm_dashboards.types.scheduled_report_arn
    import capo_bcm_dashboards.types.scheduled_report_name
    import capo_bcm_dashboards.types.service_role_arn
    import capo_bcm_dashboards.types.widget_id_list


class UpdateScheduledReportRequest(TypedDict, closed=True):
    arn: "capo_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    """<p>The ARN of the scheduled report to update.</p>"""
    name: NotRequired[
        "capo_bcm_dashboards.types.scheduled_report_name.ScheduledReportName"
    ]
    """<p>The new name for the scheduled report.</p>"""
    description: NotRequired["capo_bcm_dashboards.types.description.Description"]
    """<p>The new description for the scheduled report.</p>"""
    dashboard_arn: NotRequired["capo_bcm_dashboards.types.dashboard_arn.DashboardArn"]
    """<p>The ARN of the dashboard to associate with the scheduled report.</p>"""
    scheduled_report_execution_role_arn: NotRequired[
        "capo_bcm_dashboards.types.service_role_arn.ServiceRoleArn"
    ]
    """<p>The ARN of the IAM role that the scheduled report uses to execute. Amazon Web Services Billing and Cost Management Dashboards will assume this IAM role while executing the scheduled report.</p>"""
    schedule_config: NotRequired[
        "capo_bcm_dashboards.types.schedule_config.ScheduleConfig"
    ]
    """<p>The updated schedule configuration for the report.</p>"""
    widget_ids: NotRequired["capo_bcm_dashboards.types.widget_id_list.WidgetIdList"]
    """<p>The list of widget identifiers to include in the scheduled report. If not specified, all widgets in the dashboard are included.</p>"""
    widget_date_range_override: NotRequired[
        "capo_bcm_dashboards.types.date_time_range.DateTimeRange"
    ]
    """<p>The date range override to apply to widgets in the scheduled report.</p>"""
    clear_widget_ids: NotRequired["bool"]
    """Set to true to clear existing widgetIds."""
    clear_widget_date_range_override: NotRequired["bool"]
    """Set to true to clear existing widgetDateRangeOverride."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateScheduledReportRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "dashboard_arn" in value:
        out["dashboardArn"] = value["dashboard_arn"]
    if "scheduled_report_execution_role_arn" in value:
        out["scheduledReportExecutionRoleArn"] = value[
            "scheduled_report_execution_role_arn"
        ]
    if "schedule_config" in value:
        import capo_bcm_dashboards.types.schedule_config

        out["scheduleConfig"] = (
            capo_bcm_dashboards.types.schedule_config.serialize_aws_json_1_0(
                value["schedule_config"]
            )
        )
    if "widget_ids" in value:
        import capo_bcm_dashboards.types.widget_id_list

        out["widgetIds"] = (
            capo_bcm_dashboards.types.widget_id_list.serialize_aws_json_1_0(
                value["widget_ids"]
            )
        )
    if "widget_date_range_override" in value:
        import capo_bcm_dashboards.types.date_time_range

        out["widgetDateRangeOverride"] = (
            capo_bcm_dashboards.types.date_time_range.serialize_aws_json_1_0(
                value["widget_date_range_override"]
            )
        )
    if "clear_widget_ids" in value:
        out["clearWidgetIds"] = value["clear_widget_ids"]
    if "clear_widget_date_range_override" in value:
        out["clearWidgetDateRangeOverride"] = value["clear_widget_date_range_override"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateScheduledReportRequest:
    out: UpdateScheduledReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateScheduledReportRequest.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dashboardArn") is not None:
        out["dashboard_arn"] = data["dashboardArn"]
    if data.get("scheduledReportExecutionRoleArn") is not None:
        out["scheduled_report_execution_role_arn"] = data[
            "scheduledReportExecutionRoleArn"
        ]
    if data.get("scheduleConfig") is not None:
        import capo_bcm_dashboards.types.schedule_config

        out["schedule_config"] = (
            capo_bcm_dashboards.types.schedule_config.deserialize_aws_json_1_0(
                data["scheduleConfig"]
            )
        )
    if data.get("widgetIds") is not None:
        import capo_bcm_dashboards.types.widget_id_list

        out["widget_ids"] = (
            capo_bcm_dashboards.types.widget_id_list.deserialize_aws_json_1_0(
                data["widgetIds"]
            )
        )
    if data.get("widgetDateRangeOverride") is not None:
        import capo_bcm_dashboards.types.date_time_range

        out["widget_date_range_override"] = (
            capo_bcm_dashboards.types.date_time_range.deserialize_aws_json_1_0(
                data["widgetDateRangeOverride"]
            )
        )
    if data.get("clearWidgetIds") is not None:
        out["clear_widget_ids"] = data["clearWidgetIds"]
    if data.get("clearWidgetDateRangeOverride") is not None:
        out["clear_widget_date_range_override"] = data["clearWidgetDateRangeOverride"]
    return out
