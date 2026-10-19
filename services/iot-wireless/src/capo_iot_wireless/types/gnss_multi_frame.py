"""Generated from Smithy shape ``com.amazonaws.iotwireless#GnssMultiFrame``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.assist_position
    import capo_iot_wireless.types.capture_time_accuracy
    import capo_iot_wireless.types.coordinate
    import capo_iot_wireless.types.gnss_captures
    import capo_iot_wireless.types.use2_d_solver


class GnssMultiFrame(TypedDict, closed=True):
    captures: "capo_iot_wireless.types.gnss_captures.GnssCaptures"
    """<p>List of GNSS scan captures. Each capture contains a payload from a single GNSS scan. The number of captures must be 2, 4, 8, 16, or 32.</p>"""
    capture_time_accuracy: NotRequired[
        "capo_iot_wireless.types.capture_time_accuracy.CaptureTimeAccuracy"
    ]
    """<p>Optional value that gives the capture time estimate accuracy, in seconds. If capture time accuracy is not specified, default value of 300 is used.</p>"""
    assist_position: NotRequired[
        "capo_iot_wireless.types.assist_position.AssistPosition"
    ]
    """<p>Optional assistance position information, specified using latitude and longitude values in degrees. The coordinates are inside the WGS84 reference frame.</p>"""
    assist_altitude: NotRequired["capo_iot_wireless.types.coordinate.Coordinate"]
    """<p>Optional assistance altitude, which is the altitude of the device at capture time, specified in meters above the WGS84 reference ellipsoid. This parameter is required when Use2DSolver is enabled.</p>"""
    use2_d_solver: "capo_iot_wireless.types.use2_d_solver.Use2DSolver"
    """<p>Optional parameter that forces 2D solve, which modifies the positioning algorithm to a 2D solution problem. When this parameter is specified, the assistance altitude should have an accuracy of at least 10 meters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GnssMultiFrame) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.gnss_captures

    out["Captures"] = capo_iot_wireless.types.gnss_captures.serialize_json(
        value["captures"]
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


def deserialize_json(data: dict) -> GnssMultiFrame:
    out: GnssMultiFrame = {}  # type: ignore[typeddict-item]
    if data.get("Captures") is not None:
        import capo_iot_wireless.types.gnss_captures

        out["captures"] = capo_iot_wireless.types.gnss_captures.deserialize_json(
            data["Captures"]
        )
    else:
        out["captures"] = []
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
