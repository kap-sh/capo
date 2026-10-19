"""Generated from Smithy shape ``com.amazonaws.geoplaces#FoodType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string


class FoodType(TypedDict, closed=True):
    localized_name: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>Localized name of the food type.</p>"""
    id: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The Food Type Id.</p>"""
    primary: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if this food type is the primary offered by the place. For example, if a location serves fast food, but also dessert, he primary would likely be fast food.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoodType) -> dict:
    out: dict = {}
    out["LocalizedName"] = value["localized_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "primary" in value:
        out["Primary"] = value["primary"]
    return out


def deserialize_json(data: dict) -> FoodType:
    out: FoodType = {}  # type: ignore[typeddict-item]
    if data.get("LocalizedName") is not None:
        out["localized_name"] = data["LocalizedName"]
    else:
        out["localized_name"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    return out


def redact_sensitive(value: FoodType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "localized_name" in value:
        out["localized_name"] = "*** Sensitive Data Redacted ***"
    if "id" in value:
        out["id"] = "*** Sensitive Data Redacted ***"
    if "primary" in value:
        out["primary"] = "*** Sensitive Data Redacted ***"
    return out
