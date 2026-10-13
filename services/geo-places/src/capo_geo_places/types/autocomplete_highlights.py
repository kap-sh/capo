"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteHighlights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.autocomplete_address_highlights
    import capo_geo_places.types.highlight_list


class AutocompleteHighlights(TypedDict, closed=True):
    title: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates where the title field in the result matches the input query.</p>"""
    address: NotRequired[
        "capo_geo_places.types.autocomplete_address_highlights.AutocompleteAddressHighlights"
    ]
    """<p>Describes how part of the result address match the input query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteHighlights) -> dict:
    out: dict = {}
    if "title" in value:
        import capo_geo_places.types.highlight_list

        out["Title"] = capo_geo_places.types.highlight_list.serialize_json(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.autocomplete_address_highlights

        out["Address"] = (
            capo_geo_places.types.autocomplete_address_highlights.serialize_json(
                value["address"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteHighlights:
    out: AutocompleteHighlights = {}  # type: ignore[typeddict-item]
    if data.get("Title") is not None:
        import capo_geo_places.types.highlight_list

        out["title"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Title"]
        )
    if data.get("Address") is not None:
        import capo_geo_places.types.autocomplete_address_highlights

        out["address"] = (
            capo_geo_places.types.autocomplete_address_highlights.deserialize_json(
                data["Address"]
            )
        )
    return out


def redact_sensitive(value: AutocompleteHighlights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        import capo_geo_places.types.highlight_list

        out["title"] = capo_geo_places.types.highlight_list.redact_sensitive(
            value["title"]
        )
    if "address" in value:
        import capo_geo_places.types.autocomplete_address_highlights

        out["address"] = (
            capo_geo_places.types.autocomplete_address_highlights.redact_sensitive(
                value["address"]
            )
        )
    return out
