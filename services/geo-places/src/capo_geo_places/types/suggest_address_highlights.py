"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestAddressHighlights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.highlight_list


class SuggestAddressHighlights(TypedDict, closed=True):
    label: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending indexes of the places in the result which were identified to match the textQuery. This result is useful for providing emphasis to results where the user query directly matched to make selecting the correct result from a list easier for an end user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestAddressHighlights) -> dict:
    out: dict = {}
    if "label" in value:
        import capo_geo_places.types.highlight_list

        out["Label"] = capo_geo_places.types.highlight_list.serialize_json(
            value["label"]
        )
    return out


def deserialize_json(data: dict) -> SuggestAddressHighlights:
    out: SuggestAddressHighlights = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        import capo_geo_places.types.highlight_list

        out["label"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Label"]
        )
    return out


def redact_sensitive(value: SuggestAddressHighlights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "label" in value:
        import capo_geo_places.types.highlight_list

        out["label"] = capo_geo_places.types.highlight_list.redact_sensitive(
            value["label"]
        )
    return out
