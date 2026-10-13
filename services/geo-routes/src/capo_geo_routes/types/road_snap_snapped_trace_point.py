"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapSnappedTracePoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position
    import capo_geo_routes.types.sensitive_double


class RoadSnapSnappedTracePoint(TypedDict, closed=True):
    confidence: "capo_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Confidence value for the correctness of this point match.</p>"""
    original_position: "capo_geo_routes.types.position.Position"
    """<p>Position of the TracePoint provided within the request, at the same index.</p>"""
    snapped_position: "capo_geo_routes.types.position.Position"
    """<p>Snapped position of the TracePoint provided within the request, at the same index. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapSnappedTracePoint) -> dict:
    out: dict = {}
    out["Confidence"] = (
        "NaN"
        if value["confidence"] != value["confidence"]
        else "Infinity"
        if value["confidence"] == float("inf")
        else "-Infinity"
        if value["confidence"] == float("-inf")
        else value["confidence"]
    )
    import capo_geo_routes.types.position

    out["OriginalPosition"] = capo_geo_routes.types.position.serialize_json(
        value["original_position"]
    )
    import capo_geo_routes.types.position

    out["SnappedPosition"] = capo_geo_routes.types.position.serialize_json(
        value["snapped_position"]
    )
    return out


def deserialize_json(data: dict) -> RoadSnapSnappedTracePoint:
    out: RoadSnapSnappedTracePoint = {}  # type: ignore[typeddict-item]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    else:
        raise DeserializationError("RoadSnapSnappedTracePoint.confidence required")
    if data.get("OriginalPosition") is not None:
        import capo_geo_routes.types.position

        out["original_position"] = capo_geo_routes.types.position.deserialize_json(
            data["OriginalPosition"]
        )
    else:
        raise DeserializationError(
            "RoadSnapSnappedTracePoint.original_position required"
        )
    if data.get("SnappedPosition") is not None:
        import capo_geo_routes.types.position

        out["snapped_position"] = capo_geo_routes.types.position.deserialize_json(
            data["SnappedPosition"]
        )
    else:
        raise DeserializationError(
            "RoadSnapSnappedTracePoint.snapped_position required"
        )
    return out


def redact_sensitive(value: RoadSnapSnappedTracePoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "confidence" in value:
        out["confidence"] = "*** Sensitive Data Redacted ***"
    if "original_position" in value:
        out["original_position"] = "*** Sensitive Data Redacted ***"
    if "snapped_position" in value:
        out["snapped_position"] = "*** Sensitive Data Redacted ***"
    return out
