"""Generated from Smithy shape ``com.amazonaws.location#Leg``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.leg_geometry
    import capo_location.types.position
    import capo_location.types.sensitive_double
    import capo_location.types.step_list


class Leg(TypedDict, closed=True):
    start_position: "capo_location.types.position.Position"
    """<p>The starting position of the leg. Follows the format <code>[longitude,latitude]</code>.</p> <note> <p>If the <code>StartPosition</code> isn't located on a road, it's <a href="https://docs.aws.amazon.com/location/previous/developerguide/snap-to-nearby-road.html">snapped to a nearby road</a>. </p> </note>"""
    end_position: "capo_location.types.position.Position"
    """<p>The terminating position of the leg. Follows the format <code>[longitude,latitude]</code>.</p> <note> <p>If the <code>EndPosition</code> isn't located on a road, it's <a href="https://docs.aws.amazon.com/location/previous/developerguide/nap-to-nearby-road.html">snapped to a nearby road</a>. </p> </note>"""
    distance: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The distance between the leg's <code>StartPosition</code> and <code>EndPosition</code> along a calculated route. </p> <ul> <li> <p>The default measurement is <code>Kilometers</code> unless the request specifies a <code>DistanceUnit</code> of <code>Miles</code>.</p> </li> </ul>"""
    duration_seconds: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The estimated travel time between the leg's <code>StartPosition</code> and <code>EndPosition</code>. The travel mode and departure time that you specify in the request determines the calculated time.</p>"""
    geometry: NotRequired["capo_location.types.leg_geometry.LegGeometry"]
    """<p>Contains the calculated route's path as a linestring geometry.</p>"""
    steps: "capo_location.types.step_list.StepList"
    """<p>Contains a list of steps, which represent subsections of a leg. Each step provides instructions for how to move to the next step in the leg such as the step's start position, end position, travel distance, travel duration, and geometry offset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Leg) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["StartPosition"] = capo_location.types.position.serialize_json(
        value["start_position"]
    )
    import capo_location.types.position

    out["EndPosition"] = capo_location.types.position.serialize_json(
        value["end_position"]
    )
    out["Distance"] = (
        "NaN"
        if value["distance"] != value["distance"]
        else "Infinity"
        if value["distance"] == float("inf")
        else "-Infinity"
        if value["distance"] == float("-inf")
        else value["distance"]
    )
    out["DurationSeconds"] = (
        "NaN"
        if value["duration_seconds"] != value["duration_seconds"]
        else "Infinity"
        if value["duration_seconds"] == float("inf")
        else "-Infinity"
        if value["duration_seconds"] == float("-inf")
        else value["duration_seconds"]
    )
    if "geometry" in value:
        import capo_location.types.leg_geometry

        out["Geometry"] = capo_location.types.leg_geometry.serialize_json(
            value["geometry"]
        )
    import capo_location.types.step_list

    out["Steps"] = capo_location.types.step_list.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> Leg:
    out: Leg = {}  # type: ignore[typeddict-item]
    if data.get("StartPosition") is not None:
        import capo_location.types.position

        out["start_position"] = capo_location.types.position.deserialize_json(
            data["StartPosition"]
        )
    else:
        out["start_position"] = []
    if data.get("EndPosition") is not None:
        import capo_location.types.position

        out["end_position"] = capo_location.types.position.deserialize_json(
            data["EndPosition"]
        )
    else:
        out["end_position"] = []
    if data.get("Distance") is not None:
        out["distance"] = float(data["Distance"])
    else:
        out["distance"] = 0.0
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = float(data["DurationSeconds"])
    else:
        out["duration_seconds"] = 0.0
    if data.get("Geometry") is not None:
        import capo_location.types.leg_geometry

        out["geometry"] = capo_location.types.leg_geometry.deserialize_json(
            data["Geometry"]
        )
    if data.get("Steps") is not None:
        import capo_location.types.step_list

        out["steps"] = capo_location.types.step_list.deserialize_json(data["Steps"])
    else:
        out["steps"] = []
    return out


def redact_sensitive(value: Leg) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "start_position" in value:
        out["start_position"] = "*** Sensitive Data Redacted ***"
    if "end_position" in value:
        out["end_position"] = "*** Sensitive Data Redacted ***"
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration_seconds" in value:
        out["duration_seconds"] = "*** Sensitive Data Redacted ***"
    if "geometry" in value:
        import capo_location.types.leg_geometry

        out["geometry"] = capo_location.types.leg_geometry.redact_sensitive(
            value["geometry"]
        )
    if "steps" in value:
        import capo_location.types.step_list

        out["steps"] = capo_location.types.step_list.redact_sensitive(value["steps"])
    return out
