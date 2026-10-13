"""Generated from Smithy shape ``com.amazonaws.geoplaces#ContactDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.category_list
    import capo_geo_places.types.sensitive_string


class ContactDetails(TypedDict, closed=True):
    label: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The contact's label.</p>"""
    value: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The contact's value.</p>"""
    categories: NotRequired["capo_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong too.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactDetails) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "value" in value:
        out["Value"] = value["value"]
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["Categories"] = capo_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> ContactDetails:
    out: ContactDetails = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Categories") is not None:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    return out


def redact_sensitive(value: ContactDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "label" in value:
        out["label"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        out["value"] = "*** Sensitive Data Redacted ***"
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.redact_sensitive(
            value["categories"]
        )
    return out
