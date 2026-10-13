"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollSystem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class RouteTollSystem(TypedDict, closed=True):
    name: NotRequired["capo_geo_routes.types.sensitive_string.SensitiveString"]
    """<p>The toll system name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollSystem) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> RouteTollSystem:
    out: RouteTollSystem = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: RouteTollSystem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
