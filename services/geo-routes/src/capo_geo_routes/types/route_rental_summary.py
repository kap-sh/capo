"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_rental_overview_summary
    import capo_geo_routes.types.route_rental_travel_only_summary


class RouteRentalSummary(TypedDict, closed=True):
    overview: NotRequired[
        "capo_geo_routes.types.route_rental_overview_summary.RouteRentalOverviewSummary"
    ]
    """<p>Summary including duration and distance for the entire leg.</p>"""
    travel_only: NotRequired[
        "capo_geo_routes.types.route_rental_travel_only_summary.RouteRentalTravelOnlySummary"
    ]
    """<p>Summary including duration and distance for the travel portion of the leg only.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalSummary) -> dict:
    out: dict = {}
    if "overview" in value:
        import capo_geo_routes.types.route_rental_overview_summary

        out["Overview"] = (
            capo_geo_routes.types.route_rental_overview_summary.serialize_json(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import capo_geo_routes.types.route_rental_travel_only_summary

        out["TravelOnly"] = (
            capo_geo_routes.types.route_rental_travel_only_summary.serialize_json(
                value["travel_only"]
            )
        )
    return out


def deserialize_json(data: dict) -> RouteRentalSummary:
    out: RouteRentalSummary = {}  # type: ignore[typeddict-item]
    if data.get("Overview") is not None:
        import capo_geo_routes.types.route_rental_overview_summary

        out["overview"] = (
            capo_geo_routes.types.route_rental_overview_summary.deserialize_json(
                data["Overview"]
            )
        )
    if data.get("TravelOnly") is not None:
        import capo_geo_routes.types.route_rental_travel_only_summary

        out["travel_only"] = (
            capo_geo_routes.types.route_rental_travel_only_summary.deserialize_json(
                data["TravelOnly"]
            )
        )
    return out


def redact_sensitive(value: RouteRentalSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "overview" in value:
        import capo_geo_routes.types.route_rental_overview_summary

        out["overview"] = (
            capo_geo_routes.types.route_rental_overview_summary.redact_sensitive(
                value["overview"]
            )
        )
    if "travel_only" in value:
        import capo_geo_routes.types.route_rental_travel_only_summary

        out["travel_only"] = (
            capo_geo_routes.types.route_rental_travel_only_summary.redact_sensitive(
                value["travel_only"]
            )
        )
    return out
