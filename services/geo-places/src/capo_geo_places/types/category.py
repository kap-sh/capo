"""Generated from Smithy shape ``com.amazonaws.geoplaces#Category``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string


class Category(TypedDict, closed=True):
    id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The category ID.</p>"""
    name: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The category name.</p>"""
    localized_name: NotRequired[
        "capo_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>Localized name of the category type.</p>"""
    primary: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Boolean which indicates if this category is the primary offered by the place.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Category) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "localized_name" in value:
        out["LocalizedName"] = value["localized_name"]
    if "primary" in value:
        out["Primary"] = value["primary"]
    return out


def deserialize_json(data: dict) -> Category:
    out: Category = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Category.id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Category.name required")
    if data.get("LocalizedName") is not None:
        out["localized_name"] = data["LocalizedName"]
    if data.get("Primary") is not None:
        out["primary"] = data["Primary"]
    return out


def redact_sensitive(value: Category) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "id" in value:
        out["id"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "localized_name" in value:
        out["localized_name"] = "*** Sensitive Data Redacted ***"
    if "primary" in value:
        out["primary"] = "*** Sensitive Data Redacted ***"
    return out
