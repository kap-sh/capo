"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerrySpan``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.country_code3
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.localized_string_list
    import capo_geo_routes.types.sensitive_string


class RouteFerrySpan(TypedDict, closed=True):
    country: NotRequired["capo_geo_routes.types.country_code3.CountryCode3"]
    """<p>3 letter Country code corresponding to the Span.</p>"""
    distance: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>Distance of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p> <p> <b>Unit</b>: <code>meters</code> </p>"""
    duration: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>Duration of the computed span. This feature doesn't split a span, but is always computed on a span split by other properties.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    geometry_offset: NotRequired["int"]
    """<p>Offset in the leg geometry corresponding to the start of this span.</p>"""
    names: NotRequired[
        "capo_geo_routes.types.localized_string_list.LocalizedStringList"
    ]
    """<p>Names of the ferry span in available languages.</p>"""
    region: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>2-3 letter Region code corresponding to the Span. This is either a province or a state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerrySpan) -> dict:
    out: dict = {}
    if "country" in value:
        out["Country"] = value["country"]
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "geometry_offset" in value:
        out["GeometryOffset"] = value["geometry_offset"]
    if "names" in value:
        import capo_geo_routes.types.localized_string_list

        out["Names"] = capo_geo_routes.types.localized_string_list.serialize_json(
            value["names"]
        )
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> RouteFerrySpan:
    out: RouteFerrySpan = {}  # type: ignore[typeddict-item]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Duration") is not None:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if data.get("GeometryOffset") is not None:
        out["geometry_offset"] = data["GeometryOffset"]
    if data.get("Names") is not None:
        import capo_geo_routes.types.localized_string_list

        out["names"] = capo_geo_routes.types.localized_string_list.deserialize_json(
            data["Names"]
        )
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out


def redact_sensitive(value: RouteFerrySpan) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "country" in value:
        out["country"] = "*** Sensitive Data Redacted ***"
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "duration" in value:
        out["duration"] = "*** Sensitive Data Redacted ***"
    if "names" in value:
        import capo_geo_routes.types.localized_string_list

        out["names"] = capo_geo_routes.types.localized_string_list.redact_sensitive(
            value["names"]
        )
    if "region" in value:
        out["region"] = "*** Sensitive Data Redacted ***"
    return out
