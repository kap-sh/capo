"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteAddressHighlights``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.country_highlights
    import capo_geo_places.types.highlight_list
    import capo_geo_places.types.intersection_highlights_list
    import capo_geo_places.types.region_highlights
    import capo_geo_places.types.sub_region_highlights


class AutocompleteAddressHighlights(TypedDict, closed=True):
    label: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending indexes for result items where they are identified to match the input query. This should be used to provide emphasis to output display to make selecting the correct result from a list easier for end users.</p>"""
    country: NotRequired["capo_geo_places.types.country_highlights.CountryHighlights"]
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: NotRequired["capo_geo_places.types.region_highlights.RegionHighlights"]
    """<p>The region or state results should be to be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: NotRequired[
        "capo_geo_places.types.sub_region_highlights.SubRegionHighlights"
    ]
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>The city or locality results should be present in. </p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>The district or division of a city the results should be present in.</p>"""
    sub_district: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Indicates the starting and ending index of the title in the text query that match the found title. </p>"""
    street: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>The name of the street results should be present in.</p>"""
    block: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Name of the block. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>Name of sub-block. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    intersection: NotRequired[
        "capo_geo_places.types.intersection_highlights_list.IntersectionHighlightsList"
    ]
    """<p>Name of the streets in the intersection. For example: e.g. ["Friedrichstraße","Unter den Linden"]</p>"""
    postal_code: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess. </p>"""
    address_number: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>The house number or address results should have. </p>"""
    building: NotRequired["capo_geo_places.types.highlight_list.HighlightList"]
    """<p>The name of the building at the address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteAddressHighlights) -> dict:
    out: dict = {}
    if "label" in value:
        import capo_geo_places.types.highlight_list

        out["Label"] = capo_geo_places.types.highlight_list.serialize_json(
            value["label"]
        )
    if "country" in value:
        import capo_geo_places.types.country_highlights

        out["Country"] = capo_geo_places.types.country_highlights.serialize_json(
            value["country"]
        )
    if "region" in value:
        import capo_geo_places.types.region_highlights

        out["Region"] = capo_geo_places.types.region_highlights.serialize_json(
            value["region"]
        )
    if "sub_region" in value:
        import capo_geo_places.types.sub_region_highlights

        out["SubRegion"] = capo_geo_places.types.sub_region_highlights.serialize_json(
            value["sub_region"]
        )
    if "locality" in value:
        import capo_geo_places.types.highlight_list

        out["Locality"] = capo_geo_places.types.highlight_list.serialize_json(
            value["locality"]
        )
    if "district" in value:
        import capo_geo_places.types.highlight_list

        out["District"] = capo_geo_places.types.highlight_list.serialize_json(
            value["district"]
        )
    if "sub_district" in value:
        import capo_geo_places.types.highlight_list

        out["SubDistrict"] = capo_geo_places.types.highlight_list.serialize_json(
            value["sub_district"]
        )
    if "street" in value:
        import capo_geo_places.types.highlight_list

        out["Street"] = capo_geo_places.types.highlight_list.serialize_json(
            value["street"]
        )
    if "block" in value:
        import capo_geo_places.types.highlight_list

        out["Block"] = capo_geo_places.types.highlight_list.serialize_json(
            value["block"]
        )
    if "sub_block" in value:
        import capo_geo_places.types.highlight_list

        out["SubBlock"] = capo_geo_places.types.highlight_list.serialize_json(
            value["sub_block"]
        )
    if "intersection" in value:
        import capo_geo_places.types.intersection_highlights_list

        out["Intersection"] = (
            capo_geo_places.types.intersection_highlights_list.serialize_json(
                value["intersection"]
            )
        )
    if "postal_code" in value:
        import capo_geo_places.types.highlight_list

        out["PostalCode"] = capo_geo_places.types.highlight_list.serialize_json(
            value["postal_code"]
        )
    if "address_number" in value:
        import capo_geo_places.types.highlight_list

        out["AddressNumber"] = capo_geo_places.types.highlight_list.serialize_json(
            value["address_number"]
        )
    if "building" in value:
        import capo_geo_places.types.highlight_list

        out["Building"] = capo_geo_places.types.highlight_list.serialize_json(
            value["building"]
        )
    return out


def deserialize_json(data: dict) -> AutocompleteAddressHighlights:
    out: AutocompleteAddressHighlights = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        import capo_geo_places.types.highlight_list

        out["label"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Label"]
        )
    if data.get("Country") is not None:
        import capo_geo_places.types.country_highlights

        out["country"] = capo_geo_places.types.country_highlights.deserialize_json(
            data["Country"]
        )
    if data.get("Region") is not None:
        import capo_geo_places.types.region_highlights

        out["region"] = capo_geo_places.types.region_highlights.deserialize_json(
            data["Region"]
        )
    if data.get("SubRegion") is not None:
        import capo_geo_places.types.sub_region_highlights

        out["sub_region"] = (
            capo_geo_places.types.sub_region_highlights.deserialize_json(
                data["SubRegion"]
            )
        )
    if data.get("Locality") is not None:
        import capo_geo_places.types.highlight_list

        out["locality"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Locality"]
        )
    if data.get("District") is not None:
        import capo_geo_places.types.highlight_list

        out["district"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["District"]
        )
    if data.get("SubDistrict") is not None:
        import capo_geo_places.types.highlight_list

        out["sub_district"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["SubDistrict"]
        )
    if data.get("Street") is not None:
        import capo_geo_places.types.highlight_list

        out["street"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Street"]
        )
    if data.get("Block") is not None:
        import capo_geo_places.types.highlight_list

        out["block"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Block"]
        )
    if data.get("SubBlock") is not None:
        import capo_geo_places.types.highlight_list

        out["sub_block"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["SubBlock"]
        )
    if data.get("Intersection") is not None:
        import capo_geo_places.types.intersection_highlights_list

        out["intersection"] = (
            capo_geo_places.types.intersection_highlights_list.deserialize_json(
                data["Intersection"]
            )
        )
    if data.get("PostalCode") is not None:
        import capo_geo_places.types.highlight_list

        out["postal_code"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["PostalCode"]
        )
    if data.get("AddressNumber") is not None:
        import capo_geo_places.types.highlight_list

        out["address_number"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["AddressNumber"]
        )
    if data.get("Building") is not None:
        import capo_geo_places.types.highlight_list

        out["building"] = capo_geo_places.types.highlight_list.deserialize_json(
            data["Building"]
        )
    return out
