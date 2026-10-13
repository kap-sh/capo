"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAllowOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_boolean


class IsolineAllowOptions(TypedDict, closed=True):
    hot: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>When true, allows the use of HOT (high-occupancy toll) lanes, which may affect travel times and reachable areas.</p> <p>Default value: <code>false</code> </p>"""
    hov: NotRequired["capo_geo_routes.types.sensitive_boolean.SensitiveBoolean"]
    """<p>When true, allows the use of HOV (high-occupancy vehicle) lanes, which may affect travel times and reachable areas.</p> <p>Default value: <code>false</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAllowOptions) -> dict:
    out: dict = {}
    if "hot" in value:
        out["Hot"] = value["hot"]
    if "hov" in value:
        out["Hov"] = value["hov"]
    return out


def deserialize_json(data: dict) -> IsolineAllowOptions:
    out: IsolineAllowOptions = {}  # type: ignore[typeddict-item]
    if data.get("Hot") is not None:
        out["hot"] = data["Hot"]
    if data.get("Hov") is not None:
        out["hov"] = data["Hov"]
    return out


def redact_sensitive(value: IsolineAllowOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "hot" in value:
        out["hot"] = "*** Sensitive Data Redacted ***"
    if "hov" in value:
        out["hov"] = "*** Sensitive Data Redacted ***"
    return out
