"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransponder``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class RouteTransponder(TypedDict, closed=True):
    system_name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>Names of the toll system collecting the toll.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransponder) -> dict:
    out: dict = {}
    if "system_name" in value:
        out["SystemName"] = value["system_name"]
    return out


def deserialize_json(data: dict) -> RouteTransponder:
    out: RouteTransponder = {}  # type: ignore[typeddict-item]
    if data.get("SystemName") is not None:
        out["system_name"] = data["SystemName"]
    return out


def redact_sensitive(value: RouteTransponder) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "system_name" in value:
        out["system_name"] = "*** Sensitive Data Redacted ***"
    return out
