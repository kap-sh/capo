"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalAgency``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class RouteRentalAgency(TypedDict, closed=True):
    name: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>Name of the agency.</p>"""
    url: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>URL to the agency's website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalAgency) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> RouteRentalAgency:
    out: RouteRentalAgency = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out


def redact_sensitive(value: RouteRentalAgency) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
