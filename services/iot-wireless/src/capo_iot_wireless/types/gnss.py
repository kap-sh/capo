"""Generated from Smithy shape ``com.amazonaws.iotwireless#Gnss``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.assist_position
    import capo_iot_wireless.types.capture_time_accuracy
    import capo_iot_wireless.types.coordinate
    import capo_iot_wireless.types.gnss_nav
    import capo_iot_wireless.types.gpst
    import capo_iot_wireless.types.use2_d_solver


class Gnss(TypedDict, closed=True):
    payload: "capo_iot_wireless.types.gnss_nav.GnssNav"
    """<p>Payload that contains the GNSS scan result, or NAV message, in hexadecimal notation.</p>"""
    capture_time: NotRequired["capo_iot_wireless.types.gpst.GPST"]
    """<p>Optional parameter that gives an estimate of the time when the GNSS scan information is taken, in seconds GPS time (GPST). If capture time is not specified, the local server time is used.</p>"""
    capture_time_accuracy: NotRequired[
        "capo_iot_wireless.types.capture_time_accuracy.CaptureTimeAccuracy"
    ]
    """<p>Optional value that gives the capture time estimate accuracy, in seconds. If capture time accuracy is not specified, default value of 300 is used.</p>"""
    assist_position: NotRequired[
        "capo_iot_wireless.types.assist_position.AssistPosition"
    ]
    """<p>Optional assistance position information, specified using latitude and longitude values in degrees. The coordinates are inside the WGS84 reference frame.</p>"""
    assist_altitude: NotRequired["capo_iot_wireless.types.coordinate.Coordinate"]
    """<p>Optional assistance altitude, which is the altitude of the device at capture time, specified in meters above the WGS84 reference ellipsoid.</p>"""
    use2_d_solver: "capo_iot_wireless.types.use2_d_solver.Use2DSolver"
    """<p>Optional parameter that forces 2D solve, which modifies the positioning algorithm to a 2D solution problem. When this parameter is specified, the assistance altitude should have an accuracy of at least 10 meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Gnss) -> dict:
    out: dict = {}
    out["Payload"] = value["payload"]
    if "capture_time" in value:
        out["CaptureTime"] = (
            "NaN"
            if value["capture_time"] != value["capture_time"]
            else "Infinity"
            if value["capture_time"] == float("inf")
            else "-Infinity"
            if value["capture_time"] == float("-inf")
            else value["capture_time"]
        )
    if "capture_time_accuracy" in value:
        out["CaptureTimeAccuracy"] = (
            "NaN"
            if value["capture_time_accuracy"] != value["capture_time_accuracy"]
            else "Infinity"
            if value["capture_time_accuracy"] == float("inf")
            else "-Infinity"
            if value["capture_time_accuracy"] == float("-inf")
            else value["capture_time_accuracy"]
        )
    if "assist_position" in value:
        import capo_iot_wireless.types.assist_position

        out["AssistPosition"] = capo_iot_wireless.types.assist_position.serialize_json(
            value["assist_position"]
        )
    if "assist_altitude" in value:
        out["AssistAltitude"] = (
            "NaN"
            if value["assist_altitude"] != value["assist_altitude"]
            else "Infinity"
            if value["assist_altitude"] == float("inf")
            else "-Infinity"
            if value["assist_altitude"] == float("-inf")
            else value["assist_altitude"]
        )
    out["Use2DSolver"] = value.get("use2_d_solver", False)
    return out


def deserialize_json(data: dict) -> Gnss:
    out: Gnss = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        out["payload"] = data["Payload"]
    else:
        out["payload"] = ""
    if data.get("CaptureTime") is not None:
        out["capture_time"] = float(data["CaptureTime"])
    if data.get("CaptureTimeAccuracy") is not None:
        out["capture_time_accuracy"] = float(data["CaptureTimeAccuracy"])
    if data.get("AssistPosition") is not None:
        import capo_iot_wireless.types.assist_position

        out["assist_position"] = (
            capo_iot_wireless.types.assist_position.deserialize_json(
                data["AssistPosition"]
            )
        )
    if data.get("AssistAltitude") is not None:
        out["assist_altitude"] = float(data["AssistAltitude"])
    if data.get("Use2DSolver") is not None:
        out["use2_d_solver"] = data["Use2DSolver"]
    else:
        out["use2_d_solver"] = False
    return out
