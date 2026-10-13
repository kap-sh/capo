"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateIsolinesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.geometry_format
    import capo_geo_routes.types.isoline_list
    import capo_geo_routes.types.position
    import capo_geo_routes.types.timestamp_with_timezone_offset


class CalculateIsolinesResponse(TypedDict, closed=True):
    arrival_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Time of arrival at the destination, used for traffic calculations. This attribute is returned only if the <code>Destination</code> and <code>ArrivalTime</code> attributes were provided in the request.</p> <p>Time format: <code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    departure_time: NotRequired[
        "capo_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Time of departure from the origin, used for traffic calculations. This attribute is returned when <code>Origin</code> was provided in the request and either a specific departure time was requested (<code>DepartureTime</code>) or <code>DepartNow</code> was set to true.</p> <p>Time format: <code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    isoline_geometry_format: "capo_geo_routes.types.geometry_format.GeometryFormat"
    """<p>The format of the returned geometries, matching the format specified in the request. Either <code> FlexiblePolyline</code> for compact encoding or <code>Simple</code> for GeoJSON-compatible coordinates.</p> <p>Default value:<code>FlexiblePolyline</code> </p>"""
    isolines: "capo_geo_routes.types.isoline_list.IsolineList"
    """<p>Reachable areas, or isolines, for each threshold specified in the request.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket applied to this calculation. Different buckets apply based on the travel mode and thresholds used.</p>"""
    snapped_destination: NotRequired["capo_geo_routes.types.position.Position"]
    """<p>The actual point on the road network used for calculations, which may differ from the requested destination if <code>Destination</code> was not directly on a road.</p>"""
    snapped_origin: NotRequired["capo_geo_routes.types.position.Position"]
    """<p>The actual point on the road network used for calculations, which may differ from the requested origin if <code>Origin</code> was not directly on a road.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateIsolinesResponse) -> dict:
    out: dict = {}
    if "arrival_time" in value:
        out["ArrivalTime"] = value["arrival_time"]
    if "departure_time" in value:
        out["DepartureTime"] = value["departure_time"]
    import capo_geo_routes.types.geometry_format

    out["IsolineGeometryFormat"] = capo_geo_routes.types.geometry_format.serialize_json(
        value["isoline_geometry_format"]
    )
    import capo_geo_routes.types.isoline_list

    out["Isolines"] = capo_geo_routes.types.isoline_list.serialize_json(
        value["isolines"]
    )
    if "snapped_destination" in value:
        import capo_geo_routes.types.position

        out["SnappedDestination"] = capo_geo_routes.types.position.serialize_json(
            value["snapped_destination"]
        )
    if "snapped_origin" in value:
        import capo_geo_routes.types.position

        out["SnappedOrigin"] = capo_geo_routes.types.position.serialize_json(
            value["snapped_origin"]
        )
    return out


def deserialize_json(data: dict) -> CalculateIsolinesResponse:
    out: CalculateIsolinesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ArrivalTime") is not None:
        out["arrival_time"] = data["ArrivalTime"]
    if data.get("DepartureTime") is not None:
        out["departure_time"] = data["DepartureTime"]
    if data.get("IsolineGeometryFormat") is not None:
        import capo_geo_routes.types.geometry_format

        out["isoline_geometry_format"] = (
            capo_geo_routes.types.geometry_format.deserialize_json(
                data["IsolineGeometryFormat"]
            )
        )
    else:
        raise DeserializationError(
            "CalculateIsolinesResponse.isoline_geometry_format required"
        )
    if data.get("Isolines") is not None:
        import capo_geo_routes.types.isoline_list

        out["isolines"] = capo_geo_routes.types.isoline_list.deserialize_json(
            data["Isolines"]
        )
    else:
        raise DeserializationError("CalculateIsolinesResponse.isolines required")
    if data.get("SnappedDestination") is not None:
        import capo_geo_routes.types.position

        out["snapped_destination"] = capo_geo_routes.types.position.deserialize_json(
            data["SnappedDestination"]
        )
    if data.get("SnappedOrigin") is not None:
        import capo_geo_routes.types.position

        out["snapped_origin"] = capo_geo_routes.types.position.deserialize_json(
            data["SnappedOrigin"]
        )
    return out


def redact_sensitive(value: CalculateIsolinesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "arrival_time" in value:
        out["arrival_time"] = "*** Sensitive Data Redacted ***"
    if "departure_time" in value:
        out["departure_time"] = "*** Sensitive Data Redacted ***"
    if "isolines" in value:
        import capo_geo_routes.types.isoline_list

        out["isolines"] = capo_geo_routes.types.isoline_list.redact_sensitive(
            value["isolines"]
        )
    if "snapped_destination" in value:
        out["snapped_destination"] = "*** Sensitive Data Redacted ***"
    if "snapped_origin" in value:
        out["snapped_origin"] = "*** Sensitive Data Redacted ***"
    return out
