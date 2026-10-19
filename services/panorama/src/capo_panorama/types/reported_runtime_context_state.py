"""Generated from Smithy shape ``com.amazonaws.panorama#ReportedRuntimeContextState``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.desired_state
    import capo_panorama.types.device_reported_status
    import capo_panorama.types.runtime_context_name
    import capo_panorama.types.time_stamp


class ReportedRuntimeContextState(TypedDict, closed=True):
    desired_state: "capo_panorama.types.desired_state.DesiredState"
    """<p>The application's desired state.</p>"""
    runtime_context_name: "capo_panorama.types.runtime_context_name.RuntimeContextName"
    """<p>The device's name.</p>"""
    device_reported_status: (
        "capo_panorama.types.device_reported_status.DeviceReportedStatus"
    )
    """<p>The application's reported status.</p>"""
    device_reported_time: "capo_panorama.types.time_stamp.TimeStamp"
    """<p>When the device reported the application's state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportedRuntimeContextState) -> dict:
    out: dict = {}
    out["DesiredState"] = value["desired_state"]
    out["RuntimeContextName"] = value["runtime_context_name"]
    out["DeviceReportedStatus"] = value["device_reported_status"]
    import capo_panorama.types.time_stamp

    out["DeviceReportedTime"] = capo_panorama.types.time_stamp.serialize_json(
        value["device_reported_time"]
    )
    return out


def deserialize_json(data: dict) -> ReportedRuntimeContextState:
    out: ReportedRuntimeContextState = {}  # type: ignore[typeddict-item]
    if data.get("DesiredState") is not None:
        out["desired_state"] = data["DesiredState"]
    else:
        out["desired_state"] = ""
    if data.get("RuntimeContextName") is not None:
        out["runtime_context_name"] = data["RuntimeContextName"]
    else:
        out["runtime_context_name"] = ""
    if data.get("DeviceReportedStatus") is not None:
        out["device_reported_status"] = data["DeviceReportedStatus"]
    else:
        out["device_reported_status"] = ""
    if data.get("DeviceReportedTime") is not None:
        import capo_panorama.types.time_stamp

        out["device_reported_time"] = capo_panorama.types.time_stamp.deserialize_json(
            data["DeviceReportedTime"]
        )
    else:
        import datetime

        out["device_reported_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
