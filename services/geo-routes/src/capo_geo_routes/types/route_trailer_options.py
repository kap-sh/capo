"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTrailerOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_integer


class RouteTrailerOptions(TypedDict, closed=True):
    axle_count: NotRequired["capo_geo_routes.types.sensitive_integer.SensitiveInteger"]
    """<p>Total number of axles of the vehicle.</p>"""
    trailer_count: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of trailers attached to the vehicle.</p> <p>Default value: <code>0</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTrailerOptions) -> dict:
    out: dict = {}
    if "axle_count" in value:
        out["AxleCount"] = value["axle_count"]
    if "trailer_count" in value:
        out["TrailerCount"] = value["trailer_count"]
    return out


def deserialize_json(data: dict) -> RouteTrailerOptions:
    out: RouteTrailerOptions = {}  # type: ignore[typeddict-item]
    if data.get("AxleCount") is not None:
        out["axle_count"] = data["AxleCount"]
    if data.get("TrailerCount") is not None:
        out["trailer_count"] = data["TrailerCount"]
    return out


def redact_sensitive(value: RouteTrailerOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "axle_count" in value:
        out["axle_count"] = "*** Sensitive Data Redacted ***"
    if "trailer_count" in value:
        out["trailer_count"] = "*** Sensitive Data Redacted ***"
    return out
