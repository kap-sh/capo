"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationMaintenanceConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_maintenance_window_end_time
    import capo_kinesis_analytics_v2.types.application_maintenance_window_start_time


class ApplicationMaintenanceConfigurationDescription(TypedDict, closed=True):
    application_maintenance_window_start_time: "capo_kinesis_analytics_v2.types.application_maintenance_window_start_time.ApplicationMaintenanceWindowStartTime"
    """<p>The start time for the maintenance window.</p>"""
    application_maintenance_window_end_time: "capo_kinesis_analytics_v2.types.application_maintenance_window_end_time.ApplicationMaintenanceWindowEndTime"
    """<p>The end time for the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ApplicationMaintenanceConfigurationDescription,
) -> dict:
    out: dict = {}
    out["ApplicationMaintenanceWindowStartTime"] = value[
        "application_maintenance_window_start_time"
    ]
    out["ApplicationMaintenanceWindowEndTime"] = value[
        "application_maintenance_window_end_time"
    ]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ApplicationMaintenanceConfigurationDescription:
    out: ApplicationMaintenanceConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationMaintenanceWindowStartTime") is not None:
        out["application_maintenance_window_start_time"] = data[
            "ApplicationMaintenanceWindowStartTime"
        ]
    else:
        out["application_maintenance_window_start_time"] = ""
    if data.get("ApplicationMaintenanceWindowEndTime") is not None:
        out["application_maintenance_window_end_time"] = data[
            "ApplicationMaintenanceWindowEndTime"
        ]
    else:
        out["application_maintenance_window_end_time"] = ""
    return out
