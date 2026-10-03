"""Generated from Smithy shape ``com.amazonaws.geoplaces#AddressComponentMatchScores``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.match_score
    import capo_geo_places.types.match_score_list
    import capo_geo_places.types.secondary_address_component_match_score_list


class AddressComponentMatchScores(TypedDict, closed=True):
    country: "capo_geo_places.types.match_score.MatchScore"
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: "capo_geo_places.types.match_score.MatchScore"
    """<p>The region or state results should be to be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: "capo_geo_places.types.match_score.MatchScore"
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: "capo_geo_places.types.match_score.MatchScore"
    """<p>The city or locality results should be present in. </p> <p>Example: <code>Vancouver</code>.</p>"""
    district: "capo_geo_places.types.match_score.MatchScore"
    """<p>The district or division of a city the results should be present in.</p>"""
    sub_district: "capo_geo_places.types.match_score.MatchScore"
    """<p>A subdivision of a district. </p> <p>Example: <code>Minden-Lübbecke</code> </p>"""
    postal_code: "capo_geo_places.types.match_score.MatchScore"
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess. </p>"""
    block: "capo_geo_places.types.match_score.MatchScore"
    """<p>Name of the block. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: "capo_geo_places.types.match_score.MatchScore"
    """<p>Name of sub-block. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    intersection: NotRequired["capo_geo_places.types.match_score_list.MatchScoreList"]
    """<p>Name of the streets in the intersection. </p> <p>Example: <code>["Friedrichstraße","Unter den Linden"]</code> </p>"""
    address_number: "capo_geo_places.types.match_score.MatchScore"
    """<p>The house number or address results should have. </p>"""
    building: "capo_geo_places.types.match_score.MatchScore"
    """<p>The name of the building at the address.</p>"""
    secondary_address_components: NotRequired[
        "capo_geo_places.types.secondary_address_component_match_score_list.SecondaryAddressComponentMatchScoreList"
    ]
    """<p>Match scores for the secondary address components in the result.</p> <note> <p>Coverage for this functionality is available in the following countries: AUS, AUT, BRA, CAN, ESP, FRA, GBR, IDN, IND, NZL, TUR, TWN, USA.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressComponentMatchScores) -> dict:
    out: dict = {}
    out["Country"] = (
        "NaN"
        if value.get("country", 0) != value.get("country", 0)
        else "Infinity"
        if value.get("country", 0) == float("inf")
        else "-Infinity"
        if value.get("country", 0) == float("-inf")
        else value.get("country", 0)
    )
    out["Region"] = (
        "NaN"
        if value.get("region", 0) != value.get("region", 0)
        else "Infinity"
        if value.get("region", 0) == float("inf")
        else "-Infinity"
        if value.get("region", 0) == float("-inf")
        else value.get("region", 0)
    )
    out["SubRegion"] = (
        "NaN"
        if value.get("sub_region", 0) != value.get("sub_region", 0)
        else "Infinity"
        if value.get("sub_region", 0) == float("inf")
        else "-Infinity"
        if value.get("sub_region", 0) == float("-inf")
        else value.get("sub_region", 0)
    )
    out["Locality"] = (
        "NaN"
        if value.get("locality", 0) != value.get("locality", 0)
        else "Infinity"
        if value.get("locality", 0) == float("inf")
        else "-Infinity"
        if value.get("locality", 0) == float("-inf")
        else value.get("locality", 0)
    )
    out["District"] = (
        "NaN"
        if value.get("district", 0) != value.get("district", 0)
        else "Infinity"
        if value.get("district", 0) == float("inf")
        else "-Infinity"
        if value.get("district", 0) == float("-inf")
        else value.get("district", 0)
    )
    out["SubDistrict"] = (
        "NaN"
        if value.get("sub_district", 0) != value.get("sub_district", 0)
        else "Infinity"
        if value.get("sub_district", 0) == float("inf")
        else "-Infinity"
        if value.get("sub_district", 0) == float("-inf")
        else value.get("sub_district", 0)
    )
    out["PostalCode"] = (
        "NaN"
        if value.get("postal_code", 0) != value.get("postal_code", 0)
        else "Infinity"
        if value.get("postal_code", 0) == float("inf")
        else "-Infinity"
        if value.get("postal_code", 0) == float("-inf")
        else value.get("postal_code", 0)
    )
    out["Block"] = (
        "NaN"
        if value.get("block", 0) != value.get("block", 0)
        else "Infinity"
        if value.get("block", 0) == float("inf")
        else "-Infinity"
        if value.get("block", 0) == float("-inf")
        else value.get("block", 0)
    )
    out["SubBlock"] = (
        "NaN"
        if value.get("sub_block", 0) != value.get("sub_block", 0)
        else "Infinity"
        if value.get("sub_block", 0) == float("inf")
        else "-Infinity"
        if value.get("sub_block", 0) == float("-inf")
        else value.get("sub_block", 0)
    )
    if "intersection" in value:
        import capo_geo_places.types.match_score_list

        out["Intersection"] = capo_geo_places.types.match_score_list.serialize_json(
            value["intersection"]
        )
    out["AddressNumber"] = (
        "NaN"
        if value.get("address_number", 0) != value.get("address_number", 0)
        else "Infinity"
        if value.get("address_number", 0) == float("inf")
        else "-Infinity"
        if value.get("address_number", 0) == float("-inf")
        else value.get("address_number", 0)
    )
    out["Building"] = (
        "NaN"
        if value.get("building", 0) != value.get("building", 0)
        else "Infinity"
        if value.get("building", 0) == float("inf")
        else "-Infinity"
        if value.get("building", 0) == float("-inf")
        else value.get("building", 0)
    )
    if "secondary_address_components" in value:
        import capo_geo_places.types.secondary_address_component_match_score_list

        out["SecondaryAddressComponents"] = (
            capo_geo_places.types.secondary_address_component_match_score_list.serialize_json(
                value["secondary_address_components"]
            )
        )
    return out


def deserialize_json(data: dict) -> AddressComponentMatchScores:
    out: AddressComponentMatchScores = {}  # type: ignore[typeddict-item]
    if data.get("Country") is not None:
        out["country"] = float(data["Country"])
    else:
        out["country"] = 0
    if data.get("Region") is not None:
        out["region"] = float(data["Region"])
    else:
        out["region"] = 0
    if data.get("SubRegion") is not None:
        out["sub_region"] = float(data["SubRegion"])
    else:
        out["sub_region"] = 0
    if data.get("Locality") is not None:
        out["locality"] = float(data["Locality"])
    else:
        out["locality"] = 0
    if data.get("District") is not None:
        out["district"] = float(data["District"])
    else:
        out["district"] = 0
    if data.get("SubDistrict") is not None:
        out["sub_district"] = float(data["SubDistrict"])
    else:
        out["sub_district"] = 0
    if data.get("PostalCode") is not None:
        out["postal_code"] = float(data["PostalCode"])
    else:
        out["postal_code"] = 0
    if data.get("Block") is not None:
        out["block"] = float(data["Block"])
    else:
        out["block"] = 0
    if data.get("SubBlock") is not None:
        out["sub_block"] = float(data["SubBlock"])
    else:
        out["sub_block"] = 0
    if data.get("Intersection") is not None:
        import capo_geo_places.types.match_score_list

        out["intersection"] = capo_geo_places.types.match_score_list.deserialize_json(
            data["Intersection"]
        )
    if data.get("AddressNumber") is not None:
        out["address_number"] = float(data["AddressNumber"])
    else:
        out["address_number"] = 0
    if data.get("Building") is not None:
        out["building"] = float(data["Building"])
    else:
        out["building"] = 0
    if data.get("SecondaryAddressComponents") is not None:
        import capo_geo_places.types.secondary_address_component_match_score_list

        out["secondary_address_components"] = (
            capo_geo_places.types.secondary_address_component_match_score_list.deserialize_json(
                data["SecondaryAddressComponents"]
            )
        )
    return out
