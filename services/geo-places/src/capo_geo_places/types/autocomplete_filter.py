"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.autocomplete_filter_place_type_list
    import capo_geo_places.types.bounding_box
    import capo_geo_places.types.country_code_list
    import capo_geo_places.types.filter_circle


class AutocompleteFilter(TypedDict, closed=True):
    bounding_box: NotRequired["capo_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    circle: NotRequired["capo_geo_places.types.filter_circle.FilterCircle"]
    include_countries: NotRequired[
        "capo_geo_places.types.country_code_list.CountryCodeList"
    ]
    """<p> A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.</p>"""
    include_place_types: NotRequired[
        "capo_geo_places.types.autocomplete_filter_place_type_list.AutocompleteFilterPlaceTypeList"
    ]
    """<p>The included place types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteFilter) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_geo_places.types.bounding_box

        out["BoundingBox"] = capo_geo_places.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "circle" in value:
        import capo_geo_places.types.filter_circle

        out["Circle"] = capo_geo_places.types.filter_circle.serialize_json(
            value["circle"]
        )
    if "include_countries" in value:
        import capo_geo_places.types.country_code_list

        out["IncludeCountries"] = (
            capo_geo_places.types.country_code_list.serialize_json(
                value["include_countries"]
            )
        )
    if "include_place_types" in value:
        import capo_geo_places.types.autocomplete_filter_place_type_list

        out["IncludePlaceTypes"] = (
            capo_geo_places.types.autocomplete_filter_place_type_list.serialize_json(
                value["include_place_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteFilter:
    out: AutocompleteFilter = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_geo_places.types.bounding_box

        out["bounding_box"] = capo_geo_places.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if data.get("Circle") is not None:
        import capo_geo_places.types.filter_circle

        out["circle"] = capo_geo_places.types.filter_circle.deserialize_json(
            data["Circle"]
        )
    if data.get("IncludeCountries") is not None:
        import capo_geo_places.types.country_code_list

        out["include_countries"] = (
            capo_geo_places.types.country_code_list.deserialize_json(
                data["IncludeCountries"]
            )
        )
    if data.get("IncludePlaceTypes") is not None:
        import capo_geo_places.types.autocomplete_filter_place_type_list

        out["include_place_types"] = (
            capo_geo_places.types.autocomplete_filter_place_type_list.deserialize_json(
                data["IncludePlaceTypes"]
            )
        )
    return out


def redact_sensitive(value: AutocompleteFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bounding_box" in value:
        out["bounding_box"] = "*** Sensitive Data Redacted ***"
    if "circle" in value:
        out["circle"] = "*** Sensitive Data Redacted ***"
    if "include_countries" in value:
        import capo_geo_places.types.country_code_list

        out["include_countries"] = (
            capo_geo_places.types.country_code_list.redact_sensitive(
                value["include_countries"]
            )
        )
    return out
