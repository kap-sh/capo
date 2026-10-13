"""Generated from Smithy shape ``com.amazonaws.geoplaces#CrossReference``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.category_list
    import capo_geo_places.types.sensitive_string


class CrossReference(TypedDict, closed=True):
    source: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The name of the third-party data supplier (for example, <code>Yelp</code> or <code>TripAdvisor</code>).</p>"""
    source_place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The place identifier assigned by the third-party supplier.</p>"""
    source_categories: NotRequired["capo_geo_places.types.category_list.CategoryList"]
    """<p>The list of place category identifiers this supplier reference relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossReference) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    out["SourcePlaceId"] = value["source_place_id"]
    if "source_categories" in value:
        import capo_geo_places.types.category_list

        out["SourceCategories"] = capo_geo_places.types.category_list.serialize_json(
            value["source_categories"]
        )
    return out


def deserialize_json(data: dict) -> CrossReference:
    out: CrossReference = {}  # type: ignore[typeddict-item]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("CrossReference.source required")
    if data.get("SourcePlaceId") is not None:
        out["source_place_id"] = data["SourcePlaceId"]
    else:
        raise DeserializationError("CrossReference.source_place_id required")
    if data.get("SourceCategories") is not None:
        import capo_geo_places.types.category_list

        out["source_categories"] = capo_geo_places.types.category_list.deserialize_json(
            data["SourceCategories"]
        )
    return out


def redact_sensitive(value: CrossReference) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        out["source"] = "*** Sensitive Data Redacted ***"
    if "source_place_id" in value:
        out["source_place_id"] = "*** Sensitive Data Redacted ***"
    if "source_categories" in value:
        import capo_geo_places.types.category_list

        out["source_categories"] = capo_geo_places.types.category_list.redact_sensitive(
            value["source_categories"]
        )
    return out
