"""Generated from Smithy shape ``com.amazonaws.iotwireless#GnssCapture``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.gnss_nav
    import capo_iot_wireless.types.gpst


class GnssCapture(TypedDict, closed=True):
    payload: "capo_iot_wireless.types.gnss_nav.GnssNav"
    """<p>Payload that contains the GNSS scan result, or NAV message, in hexadecimal notation.</p>"""
    capture_time: NotRequired["capo_iot_wireless.types.gpst.GPST"]
    """<p>Optional parameter that gives an estimate of the time when the GNSS scan information is taken, in seconds GPS time (GPST). If capture time is not specified, the local server time is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GnssCapture) -> dict:
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
    return out


def deserialize_json(data: dict) -> GnssCapture:
    out: GnssCapture = {}  # type: ignore[typeddict-item]
    if data.get("Payload") is not None:
        out["payload"] = data["Payload"]
    else:
        out["payload"] = ""
    if data.get("CaptureTime") is not None:
        out["capture_time"] = float(data["CaptureTime"])
    return out
