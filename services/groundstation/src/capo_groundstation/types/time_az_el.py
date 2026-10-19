"""Generated from Smithy shape ``com.amazonaws.groundstation#TimeAzEl``."""

from typing_extensions import TypedDict


class TimeAzEl(TypedDict, closed=True):
    dt: "float"
    """<p>Time offset in atomic seconds from the segment's reference epoch.</p> <p>All <code>dt</code> values within a segment must be in ascending order with no duplicates.</p> <p> <code>dt</code> values may be:</p> <ul> <li> <p>negative</p> </li> <li> <p>expressed as fractions of a second</p> </li> <li> <p>expressed in scientific notation</p> </li> </ul>"""
    az: "float"
    """<p>Azimuth angle at the specified time.</p> <p>Valid ranges by unit:</p> <ul> <li> <p> <code>DEGREE_ANGLE</code>: -180 to 360 degrees, measured clockwise from true north</p> </li> <li> <p> <code>RADIAN</code>: -π to 2π radians, measured clockwise from true north</p> </li> </ul>"""
    el: "float"
    """<p>Elevation angle at the specified time.</p> <p>Valid ranges by unit:</p> <ul> <li> <p> <code>DEGREE_ANGLE</code>: -90 to 90 degrees, where 0 is the horizon, 90 is zenith, and negative values are below the horizon </p> </li> <li> <p> <code>RADIAN</code>: -π/2 to π/2 radians, where 0 is the horizon, π/2 is zenith, and negative values are below the horizon </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeAzEl) -> dict:
    out: dict = {}
    out["dt"] = (
        "NaN"
        if value["dt"] != value["dt"]
        else "Infinity"
        if value["dt"] == float("inf")
        else "-Infinity"
        if value["dt"] == float("-inf")
        else value["dt"]
    )
    out["az"] = (
        "NaN"
        if value["az"] != value["az"]
        else "Infinity"
        if value["az"] == float("inf")
        else "-Infinity"
        if value["az"] == float("-inf")
        else value["az"]
    )
    out["el"] = (
        "NaN"
        if value["el"] != value["el"]
        else "Infinity"
        if value["el"] == float("inf")
        else "-Infinity"
        if value["el"] == float("-inf")
        else value["el"]
    )
    return out


def deserialize_json(data: dict) -> TimeAzEl:
    out: TimeAzEl = {}  # type: ignore[typeddict-item]
    if data.get("dt") is not None:
        out["dt"] = float(data["dt"])
    else:
        out["dt"] = 0.0
    if data.get("az") is not None:
        out["az"] = float(data["az"])
    else:
        out["az"] = 0.0
    if data.get("el") is not None:
        out["el"] = float(data["el"])
    else:
        out["el"] = 0.0
    return out
