"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTracePoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.heading
    import capo_geo_routes.types.position
    import capo_geo_routes.types.speed_kilometers_per_hour
    import capo_geo_routes.types.timestamp_with_timezone_offset


class RoadSnapTracePoint(TypedDict, closed=True):
    heading: "capo_geo_routes.types.heading.Heading"
    """<p>GPS Heading at the position.</p>"""
    position: "capo_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    speed: "capo_geo_routes.types.speed_kilometers_per_hour.SpeedKilometersPerHour"
    """<p>Speed at the specified trace point .</p> <p> <b>Unit</b>: <code>kilometers per hour</code> </p>"""
    timestamp: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Timestamp of the event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTracePoint) -> dict:
    out: dict = {}
    out["Heading"] = (
        "NaN"
        if value.get("heading", 0) != value.get("heading", 0)
        else "Infinity"
        if value.get("heading", 0) == float("inf")
        else "-Infinity"
        if value.get("heading", 0) == float("-inf")
        else value.get("heading", 0)
    )
    import capo_geo_routes.types.position

    out["Position"] = capo_geo_routes.types.position.serialize_json(value["position"])
    out["Speed"] = (
        "NaN"
        if value.get("speed", 0) != value.get("speed", 0)
        else "Infinity"
        if value.get("speed", 0) == float("inf")
        else "-Infinity"
        if value.get("speed", 0) == float("-inf")
        else value.get("speed", 0)
    )
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
    return out


def deserialize_json(data: dict) -> RoadSnapTracePoint:
    out: RoadSnapTracePoint = {}  # type: ignore[typeddict-item]
    if data.get("Heading") is not None:
        out["heading"] = float(data["Heading"])
    else:
        out["heading"] = 0
    if data.get("Position") is not None:
        import capo_geo_routes.types.position

        out["position"] = capo_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RoadSnapTracePoint.position required")
    if data.get("Speed") is not None:
        out["speed"] = float(data["Speed"])
    else:
        out["speed"] = 0
    if data.get("Timestamp") is not None:
        out["timestamp"] = data["Timestamp"]
    return out


def redact_sensitive(value: RoadSnapTracePoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "heading" in value:
        out["heading"] = "*** Sensitive Data Redacted ***"
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    if "speed" in value:
        out["speed"] = "*** Sensitive Data Redacted ***"
    if "timestamp" in value:
        out["timestamp"] = "*** Sensitive Data Redacted ***"
    return out
