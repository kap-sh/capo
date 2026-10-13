"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAttribution``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.route_attribution_type
    import capo_geo_routes.types.route_web_link


class RouteAttribution(TypedDict, closed=True):
    attribution_type: NotRequired[
        "capo_geo_routes.types.route_attribution_type.RouteAttributionType"
    ]
    """<p>The type of the attribution link.</p>"""
    web_link: "capo_geo_routes.types.route_web_link.RouteWebLink"
    """<p>The URL to an external resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAttribution) -> dict:
    out: dict = {}
    if "attribution_type" in value:
        import capo_geo_routes.types.route_attribution_type

        out["AttributionType"] = (
            capo_geo_routes.types.route_attribution_type.serialize_json(
                value["attribution_type"]
            )
        )
    import capo_geo_routes.types.route_web_link

    out["WebLink"] = capo_geo_routes.types.route_web_link.serialize_json(
        value["web_link"]
    )
    return out


def deserialize_json(data: dict) -> RouteAttribution:
    out: RouteAttribution = {}  # type: ignore[typeddict-item]
    if data.get("AttributionType") is not None:
        import capo_geo_routes.types.route_attribution_type

        out["attribution_type"] = (
            capo_geo_routes.types.route_attribution_type.deserialize_json(
                data["AttributionType"]
            )
        )
    if data.get("WebLink") is not None:
        import capo_geo_routes.types.route_web_link

        out["web_link"] = capo_geo_routes.types.route_web_link.deserialize_json(
            data["WebLink"]
        )
    else:
        raise DeserializationError("RouteAttribution.web_link required")
    return out


def redact_sensitive(value: RouteAttribution) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attribution_type" in value:
        out["attribution_type"] = "*** Sensitive Data Redacted ***"
    if "web_link" in value:
        import capo_geo_routes.types.route_web_link

        out["web_link"] = capo_geo_routes.types.route_web_link.redact_sensitive(
            value["web_link"]
        )
    return out
