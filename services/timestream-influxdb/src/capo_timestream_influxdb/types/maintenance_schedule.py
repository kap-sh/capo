"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#MaintenanceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.iana_timezone
    import capo_timestream_influxdb.types.maintenance_window


class MaintenanceSchedule(TypedDict, closed=True):
    timezone: "capo_timestream_influxdb.types.iana_timezone.IanaTimezone"
    """<p>The IANA timezone identifier for the maintenance window. Format: Region/City or UTC. For example, America/New_York or UTC.</p>"""
    preferred_maintenance_window: (
        "capo_timestream_influxdb.types.maintenance_window.MaintenanceWindow"
    )
    """<p>The preferred maintenance window in the format ddd:HH:MM-ddd:HH:MM (UTC). Day must be one of: Mon, Tue, Wed, Thu, Fri, Sat, Sun. For example, Sun:02:00-Sun:06:00. Provide an empty string to let the system choose a window.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MaintenanceSchedule) -> dict:
    out: dict = {}
    out["timezone"] = value["timezone"]
    out["preferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MaintenanceSchedule:
    out: MaintenanceSchedule = {}  # type: ignore[typeddict-item]
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    else:
        out["timezone"] = ""
    if data.get("preferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["preferredMaintenanceWindow"]
    else:
        out["preferred_maintenance_window"] = ""
    return out
