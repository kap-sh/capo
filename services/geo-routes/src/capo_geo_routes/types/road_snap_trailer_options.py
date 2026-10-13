"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTrailerOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_integer


class RoadSnapTrailerOptions(TypedDict, closed=True):
    trailer_count: NotRequired[
        "capo_geo_routes.types.sensitive_integer.SensitiveInteger"
    ]
    """<p>Number of trailers attached to the vehicle.</p> <p>Default value: <code>0</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTrailerOptions) -> dict:
    out: dict = {}
    if "trailer_count" in value:
        out["TrailerCount"] = value["trailer_count"]
    return out


def deserialize_json(data: dict) -> RoadSnapTrailerOptions:
    out: RoadSnapTrailerOptions = {}  # type: ignore[typeddict-item]
    if data.get("TrailerCount") is not None:
        out["trailer_count"] = data["TrailerCount"]
    return out


def redact_sensitive(value: RoadSnapTrailerOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "trailer_count" in value:
        out["trailer_count"] = "*** Sensitive Data Redacted ***"
    return out
