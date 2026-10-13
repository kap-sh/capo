"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.route_toll_price_summary


class RouteTollSummary(TypedDict, closed=True):
    total: NotRequired[
        "capo_geo_routes.types.route_toll_price_summary.RouteTollPriceSummary"
    ]
    """<p>Total toll summary for the complete route. Total is the only summary available today.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollSummary) -> dict:
    out: dict = {}
    if "total" in value:
        import capo_geo_routes.types.route_toll_price_summary

        out["Total"] = capo_geo_routes.types.route_toll_price_summary.serialize_json(
            value["total"]
        )
    return out


def deserialize_json(data: dict) -> RouteTollSummary:
    out: RouteTollSummary = {}  # type: ignore[typeddict-item]
    if data.get("Total") is not None:
        import capo_geo_routes.types.route_toll_price_summary

        out["total"] = capo_geo_routes.types.route_toll_price_summary.deserialize_json(
            data["Total"]
        )
    return out


def redact_sensitive(value: RouteTollSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "total" in value:
        import capo_geo_routes.types.route_toll_price_summary

        out["total"] = capo_geo_routes.types.route_toll_price_summary.redact_sensitive(
            value["total"]
        )
    return out
