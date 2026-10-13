"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPaymentSite``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.position23


class RouteTollPaymentSite(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>Name of the payment site.</p>"""
    position: "capo_geo_routes.types.position23.Position23"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPaymentSite) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import capo_geo_routes.types.position23

    out["Position"] = capo_geo_routes.types.position23.serialize_json(value["position"])
    return out


def deserialize_json(data: dict) -> RouteTollPaymentSite:
    out: RouteTollPaymentSite = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Position") is not None:
        import capo_geo_routes.types.position23

        out["position"] = capo_geo_routes.types.position23.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError("RouteTollPaymentSite.position required")
    return out


def redact_sensitive(value: RouteTollPaymentSite) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    return out
