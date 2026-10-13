"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_overview_summary
    import capo_geo_routes.types.route_vehicle_travel_only_summary


class RouteVehicleSummary(TypedDict, closed=True):
    overview: NotRequired[
        "capo_geo_routes.types.route_vehicle_overview_summary.RouteVehicleOverviewSummary"
    ]
    """<p>Summarized details for the leg including before travel, travel and after travel steps.</p>"""
    travel_only: NotRequired[
        "capo_geo_routes.types.route_vehicle_travel_only_summary.RouteVehicleTravelOnlySummary"
    ]
    """<p>Summarized details for the leg including travel steps only. The Distance for the travel only portion of the journey is in meters</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleSummary) -> dict:
    out: dict = {}
    if "overview" in value:
        import capo_geo_routes.types.route_vehicle_overview_summary

        out["Overview"] = (
            capo_geo_routes.types.route_vehicle_overview_summary.serialize_json(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import capo_geo_routes.types.route_vehicle_travel_only_summary

        out["TravelOnly"] = (
            capo_geo_routes.types.route_vehicle_travel_only_summary.serialize_json(
                value["travel_only"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteVehicleSummary:
    out: RouteVehicleSummary = {}  # type: ignore[typeddict-item]
    if data.get("Overview") is not None:
        import capo_geo_routes.types.route_vehicle_overview_summary

        out["overview"] = (
            capo_geo_routes.types.route_vehicle_overview_summary.deserialize_json(
                data["Overview"]
            )
        )
    if data.get("TravelOnly") is not None:
        import capo_geo_routes.types.route_vehicle_travel_only_summary

        out["travel_only"] = (
            capo_geo_routes.types.route_vehicle_travel_only_summary.deserialize_json(
                data["TravelOnly"]
            )
        )
    return out


def redact_sensitive(value: RouteVehicleSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "overview" in value:
        import capo_geo_routes.types.route_vehicle_overview_summary

        out["overview"] = (
            capo_geo_routes.types.route_vehicle_overview_summary.redact_sensitive(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import capo_geo_routes.types.route_vehicle_travel_only_summary

        out["travel_only"] = (
            capo_geo_routes.types.route_vehicle_travel_only_summary.redact_sensitive(
                value["travel_only"]
            )
        )
    return out
