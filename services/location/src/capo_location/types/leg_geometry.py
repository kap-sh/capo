"""Generated from Smithy shape ``com.amazonaws.location#LegGeometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.line_string


class LegGeometry(TypedDict, closed=True):
    line_string: NotRequired["capo_location.types.line_string.LineString"]
    """<p>An ordered list of positions used to plot a route on a map. </p> <p>The first position is closest to the start position for the leg, and the last position is the closest to the end position for the leg.</p> <ul> <li> <p>For example, <code>[[-123.117, 49.284],[-123.115, 49.285],[-123.115, 49.285]]</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: LegGeometry) -> dict:
    out: dict = {}
    if "line_string" in value:
        import capo_location.types.line_string

        out["LineString"] = capo_location.types.line_string.serialize_json(
            value["line_string"]
        )
    return out


def deserialize_json(data: dict) -> LegGeometry:
    out: LegGeometry = {}  # type: ignore[typeddict-item]
    if data.get("LineString") is not None:
        import capo_location.types.line_string

        out["line_string"] = capo_location.types.line_string.deserialize_json(
            data["LineString"]
        )
    return out


def redact_sensitive(value: LegGeometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "line_string" in value:
        import capo_location.types.line_string

        out["line_string"] = capo_location.types.line_string.redact_sensitive(
            value["line_string"]
        )
    return out
