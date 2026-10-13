"""Generated from Smithy shape ``com.amazonaws.location#TrackingFilterGeometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.linear_rings


class TrackingFilterGeometry(TypedDict, closed=True):
    polygon: NotRequired["capo_location.types.linear_rings.LinearRings"]
    """<p>The set of arrays which define the polygon. A polygon can have between 4 and 1000 vertices.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrackingFilterGeometry) -> dict:
    out: dict = {}
    if "polygon" in value:
        import capo_location.types.linear_rings

        out["Polygon"] = capo_location.types.linear_rings.serialize_json(
            value["polygon"]
        )
    return out


def deserialize_json(data: dict) -> TrackingFilterGeometry:
    out: TrackingFilterGeometry = {}  # type: ignore[typeddict-item]
    if data.get("Polygon") is not None:
        import capo_location.types.linear_rings

        out["polygon"] = capo_location.types.linear_rings.deserialize_json(
            data["Polygon"]
        )
    return out


def redact_sensitive(value: TrackingFilterGeometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "polygon" in value:
        import capo_location.types.linear_rings

        out["polygon"] = capo_location.types.linear_rings.redact_sensitive(
            value["polygon"]
        )
    return out
