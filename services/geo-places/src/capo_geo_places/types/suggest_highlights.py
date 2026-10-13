"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestHighlights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.highlight_list
    import capo_geo_places.types.suggest_address_highlights


class SuggestHighlights(TypedDict, closed=True):
    title: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the title in the text query that match the found title. </p>"""
    address: NotRequired[
        "capo_geo_places.types.suggest_address_highlights.SuggestAddressHighlights"
    ]
    """<p>The place's address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestHighlights) -> dict:
    out: dict = {}
    if "title" in value:
        import capo_geo_places.types.highlight_list

        out["Title"] = capo_geo_places.types.highlight_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.suggest_address_highlights

        out["Address"] = (
            capo_geo_places.types.suggest_address_highlights.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> SuggestHighlights:
    out: SuggestHighlights = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        import capo_geo_places.types.highlight_list

        out["title"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Title"]
        )
    if data.get("Address") is not None:
        import capo_geo_places.types.suggest_address_highlights

        out["address"] = (
            capo_geo_places.types.suggest_address_highlights.deserialize_json(
                data["Address"]
            )
        )
    return out


def redact_sensitive(value: SuggestHighlights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        import capo_geo_places.types.highlight_list

        out["title"] = capo_geo_places.types.highlight_list.redact_sensitive(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.suggest_address_highlights

        out["address"] = (
            capo_geo_places.types.suggest_address_highlights.redact_sensitive(
                value["address"]
            )
        )
    return out
