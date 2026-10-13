"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleLicensePlate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_string


class RouteVehicleLicensePlate(TypedDict, closed=True):
    last_character: NotRequired[
        "capo_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>The last character of the License Plate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleLicensePlate) -> dict:
    out: dict = {}
    if "last_character" in value:
        out["LastCharacter"] = value["last_character"]
    return out


def deserialize_json(data: dict) -> RouteVehicleLicensePlate:
    out: RouteVehicleLicensePlate = {}  # type: ignore[typeddict-item]
    if data.get("LastCharacter") is not None:
        out["last_character"] = data["LastCharacter"]
    return out


def redact_sensitive(value: RouteVehicleLicensePlate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "last_character" in value:
        out["last_character"] = "*** Sensitive Data Redacted ***"
    return out
