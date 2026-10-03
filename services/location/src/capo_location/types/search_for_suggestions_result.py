"""Generated from Smithy shape ``com.amazonaws.location#SearchForSuggestionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.place_category_list
    import capo_location.types.place_id
    import capo_location.types.place_supplemental_category_list
    import capo_location.types.sensitive_string


class SearchForSuggestionsResult(TypedDict, closed=True):
    text: "capo_location.types.sensitive_string.SensitiveString"
    """<p>The text of the place suggestion, typically formatted as an address string.</p>"""
    place_id: NotRequired["capo_location.types.place_id.PlaceId"]
    """<p>The unique identifier of the Place. You can use this with the <code>GetPlace</code> operation to find the place again later, or to get full information for the Place.</p> <p>The <code>GetPlace</code> request must use the same <code>PlaceIndex</code> resource as the <code>SearchPlaceIndexForSuggestions</code> that generated the Place ID.</p> <note> <p>For <code>SearchPlaceIndexForSuggestions</code> operations, the <code>PlaceId</code> is returned by place indexes that use Esri, Grab, or HERE as data providers.</p> </note>"""
    categories: NotRequired["capo_location.types.place_category_list.PlaceCategoryList"]
    """<p>The Amazon Location categories that describe the Place.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>"""
    supplemental_categories: NotRequired[
        "capo_location.types.place_supplemental_category_list.PlaceSupplementalCategoryList"
    ]
    """<p>Categories from the data provider that describe the Place that are not mapped to any Amazon Location categories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchForSuggestionsResult) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "place_id" in value:
        out["PlaceId"] = value["place_id"]
    if "categories" in value:
        import capo_location.types.place_category_list

        out["Categories"] = capo_location.types.place_category_list.serialize_json(
            value["categories"]
        )
    if "supplemental_categories" in value:
        import capo_location.types.place_supplemental_category_list

        out["SupplementalCategories"] = (
            capo_location.types.place_supplemental_category_list.serialize_json(
                value["supplemental_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchForSuggestionsResult:
    out: SearchForSuggestionsResult = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("SearchForSuggestionsResult.text required")
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    if data.get("Categories") is not None:
        import capo_location.types.place_category_list

        out["categories"] = capo_location.types.place_category_list.deserialize_json(
            data["Categories"]
        )
    if data.get("SupplementalCategories") is not None:
        import capo_location.types.place_supplemental_category_list

        out["supplemental_categories"] = (
            capo_location.types.place_supplemental_category_list.deserialize_json(
                data["SupplementalCategories"]
            )
        )
    return out
