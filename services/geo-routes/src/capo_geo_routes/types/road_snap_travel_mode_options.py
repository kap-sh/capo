"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTravelModeOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.road_snap_truck_options


class RoadSnapTravelModeOptions(TypedDict, closed=True):
    truck: NotRequired[
        "capo_geo_routes.types.road_snap_truck_options.RoadSnapTruckOptions"
    ]
    """<p>Travel mode options when the provided travel mode is <code>Truck</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTravelModeOptions) -> dict:
    out: dict = {}
    if "truck" in value:
        import capo_geo_routes.types.road_snap_truck_options

        out["Truck"] = capo_geo_routes.types.road_snap_truck_options.serialize_json(
            value["truck"]
        )
    return out


def deserialize_json(data: dict) -> RoadSnapTravelModeOptions:
    out: RoadSnapTravelModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Truck") is not None:
        import capo_geo_routes.types.road_snap_truck_options

        out["truck"] = capo_geo_routes.types.road_snap_truck_options.deserialize_json(
            data["Truck"]
        )
    return out


def redact_sensitive(value: RoadSnapTravelModeOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "truck" in value:
        import capo_geo_routes.types.road_snap_truck_options

        out["truck"] = capo_geo_routes.types.road_snap_truck_options.redact_sensitive(
            value["truck"]
        )
    return out
