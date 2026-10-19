"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationMaintenanceConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_maintenance_window_start_time


class ApplicationMaintenanceConfigurationUpdate(TypedDict, closed=True):
    application_maintenance_window_start_time_update: "capo_kinesis_analytics_v2.types.application_maintenance_window_start_time.ApplicationMaintenanceWindowStartTime"
    """<p>The updated start time for the maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationMaintenanceConfigurationUpdate) -> dict:
    out: dict = {}
    out["ApplicationMaintenanceWindowStartTimeUpdate"] = value[
        "application_maintenance_window_start_time_update"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationMaintenanceConfigurationUpdate:
    out: ApplicationMaintenanceConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationMaintenanceWindowStartTimeUpdate") is not None:
        out["application_maintenance_window_start_time_update"] = data[
            "ApplicationMaintenanceWindowStartTimeUpdate"
        ]
    else:
        out["application_maintenance_window_start_time_update"] = ""
    return out
