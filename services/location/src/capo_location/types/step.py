"""Generated from Smithy shape ``com.amazonaws.location#Step``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.position
    import capo_location.types.sensitive_double


class Step(TypedDict, closed=True):
    start_position: "capo_location.types.position.Position"
    """<p>The starting position of a step. If the position is the first step in the leg, this position is the same as the start position of the leg.</p>"""
    end_position: "capo_location.types.position.Position"
    """<p>The end position of a step. If the position the last step in the leg, this position is the same as the end position of the leg.</p>"""
    distance: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The travel distance between the step's <code>StartPosition</code> and <code>EndPosition</code>.</p>"""
    duration_seconds: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The estimated travel time, in seconds, from the step's <code>StartPosition</code> to the <code>EndPosition</code>. . The travel mode and departure time that you specify in the request determines the calculated time.</p>"""
    geometry_offset: NotRequired["int"]
    """<p>Represents the start position, or index, in a sequence of steps within the leg's line string geometry. For example, the index of the first step in a leg geometry is <code>0</code>. </p> <p>Included in the response for queries that set <code>IncludeLegGeometry</code> to <code>True</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Step) -> dict:
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
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    return out


def deserialize_json(data: dict) -> Step:
    out: Step = {}  # type: ignore[typeddict-item]
    if data.get("StartPosition") is not None:
        import capo_location.types.position

        out["start_position"] = capo_location.types.position.deserialize_json(
            data["StartPosition"]
        )
    else:
        raise DeserializationError("Step.start_position required")
    if data.get("EndPosition") is not None:
        import capo_location.types.position

        out["end_position"] = capo_location.types.position.deserialize_json(
            data["EndPosition"]
        )
    else:
        raise DeserializationError("Step.end_position required")
    if data.get("Distance") is not None:
        out["distance"] = float(data["Distance"])
    else:
        raise DeserializationError("Step.distance required")
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = float(data["DurationSeconds"])
    else:
        raise DeserializationError("Step.duration_seconds required")
    if data.get("GeometryOffset") is not None:
        out["geometry_offset"] = data["GeometryOffset"]
    return out


def redact_sensitive(value: Step) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "start_position" in value:
        out["start_position"] = "*** Sensitive Data Redacted ***"
    if "end_position" in value:
        out["end_position"] = "*** Sensitive Data Redacted ***"
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration_seconds" in value:
        out["duration_seconds"] = "*** Sensitive Data Redacted ***"
    return out
