"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAllowOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_boolean


class RouteAllowOptions(TypedDict, closed=True):
    hot: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Allow Hot (High Occupancy Toll) lanes while calculating the route.</p> <p>Default value: <code>false</code> </p>"""
    hov: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Allow Hov (High Occupancy vehicle) lanes while calculating the route.</p> <p>Default value: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAllowOptions) -> dict:
    out: dict = {}
    if "hot" in value:
        out["Hot"] = value["hot"]
    if "hov" in value:
        out["Hov"] = value["hov"]
    return out


def deserialize_json(data: dict) -> RouteAllowOptions:
    out: RouteAllowOptions = {}  # type: ignore[typeddict-item]
    if data.get("Hot") is not None:
        out["hot"] = data["Hot"]
    if data.get("Hov") is not None:
        out["hov"] = data["Hov"]
    return out


def redact_sensitive(value: RouteAllowOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "hot" in value:
        out["hot"] = "*** Sensitive Data Redacted ***"
    if "hov" in value:
        out["hov"] = "*** Sensitive Data Redacted ***"
    return out
