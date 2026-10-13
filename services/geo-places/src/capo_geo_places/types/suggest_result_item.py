"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestResultItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.suggest_highlights
    import capo_geo_places.types.suggest_place_result
    import capo_geo_places.types.suggest_query_result
    import capo_geo_places.types.suggest_result_item_type


class SuggestResultItem(TypedDict, closed=True):
    title: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The display title that should be used when presenting this option to the end user.</p>"""
    suggest_result_item_type: (
        "capo_geo_places.types.suggest_result_item_type.SuggestResultItemType"
    )
    """<p>The result type. Place results represent the final result for a point of interest, Query results represent a follow up query which can be completed through the SearchText operation.</p>"""
    place: NotRequired["capo_geo_places.types.suggest_place_result.SuggestPlaceResult"]
    """<p>The suggested place by its unique ID.</p>"""
    query: NotRequired["capo_geo_places.types.suggest_query_result.SuggestQueryResult"]
    highlights: NotRequired[
        "capo_geo_places.types.suggest_highlights.SuggestHighlights"
    ]
    """<p>Describes how the parts of the response element matched the input query by returning the sections of the response which matched to input query terms. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestResultItem) -> dict:
    out: dict = {}
    out["Title"] = value["title"]
    import capo_geo_places.types.suggest_result_item_type

    out["SuggestResultItemType"] = (
        capo_geo_places.types.suggest_result_item_type.serialize_json(
            value["suggest_result_item_type"]
        )
    )
    if "place" in value:
        import capo_geo_places.types.suggest_place_result

        out["Place"] = capo_geo_places.types.suggest_place_result.serialize_json(
            value["place"]
        )
    if "query" in value:
        import capo_geo_places.types.suggest_query_result

        out["Query"] = capo_geo_places.types.suggest_query_result.serialize_json(
            value["query"]
        )
    if "highlights" in value:
        import capo_geo_places.types.suggest_highlights

        out["Highlights"] = capo_geo_places.types.suggest_highlights.serialize_json(
            value["highlights"]
        )
    return out


def deserialize_json(data: dict) -> SuggestResultItem:
    out: SuggestResultItem = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("SuggestResultItem.title required")
    if data.get("SuggestResultItemType") is not None:
        import capo_geo_places.types.suggest_result_item_type

        out["suggest_result_item_type"] = (
            capo_geo_places.types.suggest_result_item_type.deserialize_json(
                data["SuggestResultItemType"]
            )
        )
    else:
        raise DeserializationError(
            "SuggestResultItem.suggest_result_item_type required"
        )
    if data.get("Place") is not None:
        import capo_geo_places.types.suggest_place_result

        out["place"] = capo_geo_places.types.suggest_place_result.deserialize_json(
            data["Place"]
        )
    if data.get("Query") is not None:
        import capo_geo_places.types.suggest_query_result

        out["query"] = capo_geo_places.types.suggest_query_result.deserialize_json(
            data["Query"]
        )
    if data.get("Highlights") is not None:
        import capo_geo_places.types.suggest_highlights

        out["highlights"] = capo_geo_places.types.suggest_highlights.deserialize_json(
            data["Highlights"]
        )
    return out


def redact_sensitive(value: SuggestResultItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "place" in value:
        import capo_geo_places.types.suggest_place_result

        out["place"] = capo_geo_places.types.suggest_place_result.redact_sensitive(
            value["place"]
        )
    if "query" in value:
        import capo_geo_places.types.suggest_query_result

        out["query"] = capo_geo_places.types.suggest_query_result.redact_sensitive(
            value["query"]
        )
    if "highlights" in value:
        import capo_geo_places.types.suggest_highlights

        out["highlights"] = capo_geo_places.types.suggest_highlights.redact_sensitive(
            value["highlights"]
        )
    return out
