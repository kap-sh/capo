"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.bounding_box
    import capo_geo_places.types.country_code_list
    import capo_geo_places.types.filter_business_chain_list
    import capo_geo_places.types.filter_category_list
    import capo_geo_places.types.filter_food_type_list


class SearchNearbyFilter(TypedDict, closed=True):
    bounding_box: NotRequired["capo_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set 4 coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    include_countries: NotRequired[
        "capo_geo_places.types.country_code_list.CountryCodeList"
    ]
    """<p>A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.</p>"""
    include_categories: NotRequired[
        "capo_geo_places.types.filter_category_list.FilterCategoryList"
    ]
    """<p>Categories of results that results must belong too.</p>"""
    exclude_categories: NotRequired[
        "capo_geo_places.types.filter_category_list.FilterCategoryList"
    ]
    """<p>Categories of results that results are excluded from.</p>"""
    include_business_chains: NotRequired[
        "capo_geo_places.types.filter_business_chain_list.FilterBusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    exclude_business_chains: NotRequired[
        "capo_geo_places.types.filter_business_chain_list.FilterBusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    include_food_types: NotRequired[
        "capo_geo_places.types.filter_food_type_list.FilterFoodTypeList"
    ]
    """<p>Food types that results are included from.</p>"""
    exclude_food_types: NotRequired[
        "capo_geo_places.types.filter_food_type_list.FilterFoodTypeList"
    ]
    """<p>Food types that results are excluded from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyFilter) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_geo_places.types.bounding_box

        out["BoundingBox"] = capo_geo_places.types.bounding_box.serialize_json(
            value["bounding_box"]
        )
    if "include_countries" in value:
        import capo_geo_places.types.country_code_list

        out["IncludeCountries"] = (
            capo_geo_places.types.country_code_list.serialize_json(
                value["include_countries"]
            )
        )
    if "include_categories" in value:
        import capo_geo_places.types.filter_category_list

        out["IncludeCategories"] = (
            capo_geo_places.types.filter_category_list.serialize_json(
                value["include_categories"]
            )
        )
    if "exclude_categories" in value:
        import capo_geo_places.types.filter_category_list

        out["ExcludeCategories"] = (
            capo_geo_places.types.filter_category_list.serialize_json(
                value["exclude_categories"]
            )
        )
    if "include_business_chains" in value:
        import capo_geo_places.types.filter_business_chain_list

        out["IncludeBusinessChains"] = (
            capo_geo_places.types.filter_business_chain_list.serialize_json(
                value["include_business_chains"]
            )
        )
    if "exclude_business_chains" in value:
        import capo_geo_places.types.filter_business_chain_list

        out["ExcludeBusinessChains"] = (
            capo_geo_places.types.filter_business_chain_list.serialize_json(
                value["exclude_business_chains"]
            )
        )
    if "include_food_types" in value:
        import capo_geo_places.types.filter_food_type_list

        out["IncludeFoodTypes"] = (
            capo_geo_places.types.filter_food_type_list.serialize_json(
                value["include_food_types"]
            )
        )
    if "exclude_food_types" in value:
        import capo_geo_places.types.filter_food_type_list

        out["ExcludeFoodTypes"] = (
            capo_geo_places.types.filter_food_type_list.serialize_json(
                value["exclude_food_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchNearbyFilter:
    out: SearchNearbyFilter = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_geo_places.types.bounding_box

        out["bounding_box"] = capo_geo_places.types.bounding_box.deserialize_json(
            data["BoundingBox"]
        )
    if data.get("IncludeCountries") is not None:
        import capo_geo_places.types.country_code_list

        out["include_countries"] = (
            capo_geo_places.types.country_code_list.deserialize_json(
                data["IncludeCountries"]
            )
        )
    if data.get("IncludeCategories") is not None:
        import capo_geo_places.types.filter_category_list

        out["include_categories"] = (
            capo_geo_places.types.filter_category_list.deserialize_json(
                data["IncludeCategories"]
            )
        )
    if data.get("ExcludeCategories") is not None:
        import capo_geo_places.types.filter_category_list

        out["exclude_categories"] = (
            capo_geo_places.types.filter_category_list.deserialize_json(
                data["ExcludeCategories"]
            )
        )
    if data.get("IncludeBusinessChains") is not None:
        import capo_geo_places.types.filter_business_chain_list

        out["include_business_chains"] = (
            capo_geo_places.types.filter_business_chain_list.deserialize_json(
                data["IncludeBusinessChains"]
            )
        )
    if data.get("ExcludeBusinessChains") is not None:
        import capo_geo_places.types.filter_business_chain_list

        out["exclude_business_chains"] = (
            capo_geo_places.types.filter_business_chain_list.deserialize_json(
                data["ExcludeBusinessChains"]
            )
        )
    if data.get("IncludeFoodTypes") is not None:
        import capo_geo_places.types.filter_food_type_list

        out["include_food_types"] = (
            capo_geo_places.types.filter_food_type_list.deserialize_json(
                data["IncludeFoodTypes"]
            )
        )
    if data.get("ExcludeFoodTypes") is not None:
        import capo_geo_places.types.filter_food_type_list

        out["exclude_food_types"] = (
            capo_geo_places.types.filter_food_type_list.deserialize_json(
                data["ExcludeFoodTypes"]
            )
        )
    return out


def redact_sensitive(value: SearchNearbyFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bounding_box" in value:
        out["bounding_box"] = "*** Sensitive Data Redacted ***"
    if "include_countries" in value:
        import capo_geo_places.types.country_code_list

        out["include_countries"] = (
            capo_geo_places.types.country_code_list.redact_sensitive(
                value["include_countries"]
            )
        )
    if "include_categories" in value:
        import capo_geo_places.types.filter_category_list

        out["include_categories"] = (
            capo_geo_places.types.filter_category_list.redact_sensitive(
                value["include_categories"]
            )
        )
    if "exclude_categories" in value:
        import capo_geo_places.types.filter_category_list

        out["exclude_categories"] = (
            capo_geo_places.types.filter_category_list.redact_sensitive(
                value["exclude_categories"]
            )
        )
    if "include_business_chains" in value:
        import capo_geo_places.types.filter_business_chain_list

        out["include_business_chains"] = (
            capo_geo_places.types.filter_business_chain_list.redact_sensitive(
                value["include_business_chains"]
            )
        )
    if "exclude_business_chains" in value:
        import capo_geo_places.types.filter_business_chain_list

        out["exclude_business_chains"] = (
            capo_geo_places.types.filter_business_chain_list.redact_sensitive(
                value["exclude_business_chains"]
            )
        )
    if "include_food_types" in value:
        import capo_geo_places.types.filter_food_type_list

        out["include_food_types"] = (
            capo_geo_places.types.filter_food_type_list.redact_sensitive(
                value["include_food_types"]
            )
        )
    if "exclude_food_types" in value:
        import capo_geo_places.types.filter_food_type_list

        out["exclude_food_types"] = (
            capo_geo_places.types.filter_food_type_list.redact_sensitive(
                value["exclude_food_types"]
            )
        )
    return out
