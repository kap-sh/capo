"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSignpostLabel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.localized_string
    import capo_geo_routes.types.route_number


class RouteSignpostLabel(TypedDict, closed=True):
    route_number: NotRequired["capo_geo_routes.types.route_number.RouteNumber"]
    """<p>Route number of the road.</p>"""
    text: NotRequired["capo_geo_routes.types.localized_string.LocalizedString"]
    """<p>The Signpost text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteSignpostLabel) -> dict:
    out: dict = {}
    if "route_number" in value:
        import capo_geo_routes.types.route_number

        out["RouteNumber"] = capo_geo_routes.types.route_number.serialize_json(
            value["route_number"]
        )
    if "text" in value:
        import capo_geo_routes.types.localized_string

        out["Text"] = capo_geo_routes.types.localized_string.serialize_json(
            value["text"]
        )
    return out


def deserialize_json(data: dict) -> RouteSignpostLabel:
    out: RouteSignpostLabel = {}  # type: ignore[typeddict-item]
    if data.get("RouteNumber") is not None:
        import capo_geo_routes.types.route_number

        out["route_number"] = capo_geo_routes.types.route_number.deserialize_json(
            data["RouteNumber"]
        )
    if data.get("Text") is not None:
        import capo_geo_routes.types.localized_string

        out["text"] = capo_geo_routes.types.localized_string.deserialize_json(
            data["Text"]
        )
    return out


def redact_sensitive(value: RouteSignpostLabel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "route_number" in value:
        import capo_geo_routes.types.route_number

        out["route_number"] = capo_geo_routes.types.route_number.redact_sensitive(
            value["route_number"]
        )
    if "text" in value:
        import capo_geo_routes.types.localized_string

        out["text"] = capo_geo_routes.types.localized_string.redact_sensitive(
            value["text"]
        )
    return out
