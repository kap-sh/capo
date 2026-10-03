"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.bounding_box
    import capo_location.types.distance_unit
    import capo_location.types.sensitive_double


class CalculateRouteSummary(TypedDict, closed=True):
    route_b_box: "capo_location.types.bounding_box.BoundingBox"
    """<p>Specifies a geographical box surrounding a route. Used to zoom into a route when displaying it in a map. For example, <code>[min x, min y, max x, max y]</code>.</p> <p>The first 2 <code>bbox</code> parameters describe the lower southwest corner: </p> <ul> <li> <p>The first <code>bbox</code> position is the X coordinate or longitude of the lower southwest corner. </p> </li> <li> <p>The second <code>bbox</code> position is the Y coordinate or latitude of the lower southwest corner. </p> </li> </ul> <p>The next 2 <code>bbox</code> parameters describe the upper northeast corner: </p> <ul> <li> <p>The third <code>bbox</code> position is the X coordinate, or longitude of the upper northeast corner. </p> </li> <li> <p>The fourth <code>bbox</code> position is the Y coordinate, or latitude of the upper northeast corner. </p> </li> </ul>"""
    data_source: "str"
    """<p>The data provider of traffic and road network data used to calculate the route. Indicates one of the available providers:</p> <ul> <li> <p> <code>Esri</code> </p> </li> <li> <p> <code>Grab</code> </p> </li> <li> <p> <code>Here</code> </p> </li> </ul> <p>For more information about data providers, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Amazon Location Service data providers</a>.</p>"""
    distance: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The total distance covered by the route. The sum of the distance travelled between every stop on the route.</p> <note> <p>If Esri is the data source for the route calculator, the route distance can’t be greater than 400 km. If the route exceeds 400 km, the response is a <code>400 RoutesValidationException</code> error.</p> </note>"""
    duration_seconds: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The total travel time for the route measured in seconds. The sum of the travel time between every stop on the route.</p>"""
    distance_unit: "capo_location.types.distance_unit.DistanceUnit"
    """<p>The unit of measurement for route distances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteSummary) -> dict:
    out: dict = {}
    import capo_location.types.bounding_box

    out["RouteBBox"] = capo_location.types.bounding_box.serialize_json(
        value["route_b_box"]
    )
    out["DataSource"] = value["data_source"]
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
    out["DistanceUnit"] = value["distance_unit"]
    return out


def deserialize_json(data: dict) -> CalculateRouteSummary:
    out: CalculateRouteSummary = {}  # type: ignore[typeddict-item]
    if data.get("RouteBBox") is not None:
        import capo_location.types.bounding_box

        out["route_b_box"] = capo_location.types.bounding_box.deserialize_json(
            data["RouteBBox"]
        )
    else:
        raise DeserializationError("CalculateRouteSummary.route_b_box required")
    if data.get("DataSource") is not None:
        out["data_source"] = data["DataSource"]
    else:
        raise DeserializationError("CalculateRouteSummary.data_source required")
    if data.get("Distance") is not None:
        out["distance"] = float(data["Distance"])
    else:
        raise DeserializationError("CalculateRouteSummary.distance required")
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = float(data["DurationSeconds"])
    else:
        raise DeserializationError("CalculateRouteSummary.duration_seconds required")
    if data.get("DistanceUnit") is not None:
        out["distance_unit"] = data["DistanceUnit"]
    else:
        raise DeserializationError("CalculateRouteSummary.distance_unit required")
    return out
