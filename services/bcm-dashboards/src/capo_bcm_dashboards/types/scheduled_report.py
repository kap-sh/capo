"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#ScheduledReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_arn
    import capo_bcm_dashboards.types.date_time_range
    import capo_bcm_dashboards.types.description
    import capo_bcm_dashboards.types.generic_time_stamp
    import capo_bcm_dashboards.types.health_status
    import capo_bcm_dashboards.types.schedule_config
    import capo_bcm_dashboards.types.scheduled_report_arn
    import capo_bcm_dashboards.types.scheduled_report_name
    import capo_bcm_dashboards.types.service_role_arn
    import capo_bcm_dashboards.types.widget_id_list


class ScheduledReport(TypedDict, closed=True):
    arn: NotRequired[
        "capo_bcm_dashboards.types.scheduled_report_arn.ScheduledReportArn"
    ]
    """<p>The ARN of the scheduled report.</p>"""
    name: "capo_bcm_dashboards.types.scheduled_report_name.ScheduledReportName"
    """<p>The name of the scheduled report.</p>"""
    dashboard_arn: "capo_bcm_dashboards.types.dashboard_arn.DashboardArn"
    """<p>The ARN of the dashboard associated with the scheduled report.</p>"""
    scheduled_report_execution_role_arn: (
        "capo_bcm_dashboards.types.service_role_arn.ServiceRoleArn"
    )
    """<p>The ARN of the IAM role that the scheduled report uses to execute. Amazon Web Services Billing and Cost Management Dashboards will assume this IAM role while executing the scheduled report.</p>"""
    schedule_config: "capo_bcm_dashboards.types.schedule_config.ScheduleConfig"
    """<p>The schedule configuration that defines when and how often the report is generated.</p>"""
    description: NotRequired["capo_bcm_dashboards.types.description.Description"]
    """<p>A description of the scheduled report's purpose or contents.</p>"""
    widget_ids: NotRequired["capo_bcm_dashboards.types.widget_id_list.WidgetIdList"]
    """<p>The list of widget identifiers included in the scheduled report.</p>"""
    widget_date_range_override: NotRequired[
        "capo_bcm_dashboards.types.date_time_range.DateTimeRange"
    ]
    """<p>The date range override applied to widgets in the scheduled report.</p>"""
    created_at: NotRequired[
        "capo_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The timestamp when the scheduled report was created.</p>"""
    updated_at: NotRequired[
        "capo_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The timestamp when the scheduled report was last modified.</p>"""
    last_execution_at: NotRequired[
        "capo_bcm_dashboards.types.generic_time_stamp.GenericTimeStamp"
    ]
    """<p>The timestamp of the most recent execution of the scheduled report.</p>"""
    health_status: NotRequired["capo_bcm_dashboards.types.health_status.HealthStatus"]
    """<p>The health status of the scheduled report at last refresh time.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledReport) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["dashboardArn"] = value["dashboard_arn"]
    out["scheduledReportExecutionRoleArn"] = value[
        "scheduled_report_execution_role_arn"
    ]
    import capo_bcm_dashboards.types.schedule_config

    out["scheduleConfig"] = (
        capo_bcm_dashboards.types.schedule_config.serialize_aws_json_1_0(
            value["schedule_config"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
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
    if "created_at" in value:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["createdAt"] = (
            capo_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["updatedAt"] = (
            capo_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "last_execution_at" in value:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["lastExecutionAt"] = (
            capo_bcm_dashboards.types.generic_time_stamp.serialize_aws_json_1_0(
                value["last_execution_at"]
            )
        )
    if "health_status" in value:
        import capo_bcm_dashboards.types.health_status

        out["healthStatus"] = (
            capo_bcm_dashboards.types.health_status.serialize_aws_json_1_0(
                value["health_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledReport:
    out: ScheduledReport = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dashboardArn") is not None:
        out["dashboard_arn"] = data["dashboardArn"]
    else:
        out["dashboard_arn"] = ""
    if data.get("scheduledReportExecutionRoleArn") is not None:
        out["scheduled_report_execution_role_arn"] = data[
            "scheduledReportExecutionRoleArn"
        ]
    else:
        out["scheduled_report_execution_role_arn"] = ""
    if data.get("scheduleConfig") is not None:
        import capo_bcm_dashboards.types.schedule_config

        out["schedule_config"] = (
            capo_bcm_dashboards.types.schedule_config.deserialize_aws_json_1_0(
                data["scheduleConfig"]
            )
        )
    else:
        raise DeserializationError("ScheduledReport.schedule_config required")
    if data.get("description") is not None:
        out["description"] = data["description"]
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
    if data.get("createdAt") is not None:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["created_at"] = (
            capo_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["updated_at"] = (
            capo_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if data.get("lastExecutionAt") is not None:
        import capo_bcm_dashboards.types.generic_time_stamp

        out["last_execution_at"] = (
            capo_bcm_dashboards.types.generic_time_stamp.deserialize_aws_json_1_0(
                data["lastExecutionAt"]
            )
        )
    if data.get("healthStatus") is not None:
        import capo_bcm_dashboards.types.health_status

        out["health_status"] = (
            capo_bcm_dashboards.types.health_status.deserialize_aws_json_1_0(
                data["healthStatus"]
            )
        )
    return out
