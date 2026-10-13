"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteNumber``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.language_tag
    import capo_geo_routes.types.route_direction
    import capo_geo_routes.types.sensitive_string


class RouteNumber(TypedDict, closed=True):
    direction: NotRequired["capo_geo_routes.types.route_direction.RouteDirection"]
    """<p>Directional identifier of the route.</p>"""
    language: NotRequired["capo_geo_routes.types.language_tag.LanguageTag"]
    """<p>List of languages for instructions corresponding to the route number.</p>"""
    value: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>The route number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteNumber) -> dict:
    out: dict = {}
    if "direction" in value:
        import capo_geo_routes.types.route_direction

        out["Direction"] = capo_geo_routes.types.route_direction.serialize_json(
            value["direction"]
        )
    if "language" in value:
        out["Language"] = value["language"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> RouteNumber:
    out: RouteNumber = {}  # type: ignore[typeddict-item]
    if data.get("Direction") is not None:
        import capo_geo_routes.types.route_direction

        out["direction"] = capo_geo_routes.types.route_direction.deserialize_json(
            data["Direction"]
        )
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("RouteNumber.value required")
    return out


def redact_sensitive(value: RouteNumber) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "direction" in value:
        out["direction"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    return out
