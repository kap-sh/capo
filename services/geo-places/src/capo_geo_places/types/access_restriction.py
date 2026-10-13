"""Generated from Smithy shape ``com.amazonaws.geoplaces#AccessRestriction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.category_list
    import capo_geo_places.types.sensitive_boolean


class AccessRestriction(TypedDict, closed=True):
    restricted: NotRequired["capo_geo_places.types.sensitive_boolean.SensitiveBoolean"]
    """<p>The restriction.</p>"""
    categories: NotRequired["capo_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong too.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessRestriction) -> dict:
    out: dict = {}
    if "restricted" in value:
        out["Restricted"] = value["restricted"]
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["Categories"] = capo_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> AccessRestriction:
    out: AccessRestriction = {}  # type: ignore[typeddict-item]
    if data.get("Restricted") is not None:
        out["restricted"] = data["Restricted"]
    if data.get("Categories") is not None:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    return out


def redact_sensitive(value: AccessRestriction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "restricted" in value:
        out["restricted"] = "*** Sensitive Data Redacted ***"
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.redact_sensitive(
            value["categories"]
        )
    return out
