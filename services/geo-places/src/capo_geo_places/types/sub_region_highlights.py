"""Generated from Smithy shape ``com.amazonaws.geoplaces#SubRegionHighlights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.highlight_list


class SubRegionHighlights(TypedDict, closed=True):
    code: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the sub-region in the text query that match the found title. </p>"""
    name: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the name in the text query that match the found title. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubRegionHighlights) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_geo_places.types.highlight_list

        out["Code"] = capo_geo_places.types.highlight_list.serialize_json(value["code"])
    if "name" in value:
        import capo_geo_places.types.highlight_list

        out["Name"] = capo_geo_places.types.highlight_list.serialize_json(value["name"])
    return out


def deserialize_json(data: dict) -> SubRegionHighlights:
    out: SubRegionHighlights = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_geo_places.types.highlight_list

        out["code"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Code"]
        )
    if data.get("Name") is not None:
        import capo_geo_places.types.highlight_list

        out["name"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Name"]
        )
    return out


def redact_sensitive(value: SubRegionHighlights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        import capo_geo_places.types.highlight_list

        out["code"] = capo_geo_places.types.highlight_list.redact_sensitive(
            value["code"]
        )
    if "name" in value:
        import capo_geo_places.types.highlight_list

        out["name"] = capo_geo_places.types.highlight_list.redact_sensitive(
            value["name"]
        )
    return out
