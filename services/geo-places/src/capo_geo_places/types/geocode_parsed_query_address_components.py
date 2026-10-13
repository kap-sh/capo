"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeParsedQueryAddressComponents``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.parsed_query_component_list
    import capo_geo_places.types.parsed_query_secondary_address_component_list


class GeocodeParsedQueryAddressComponents(TypedDict, closed=True):
    country: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The alpha-2 or alpha-3 character code for the country that the results will be present in.</p>"""
    region: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The region or state results should be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The city or locality of the address.</p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The district or division of a city the results should be present in.</p>"""
    sub_district: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>A subdivision of a district. </p> <p>Example: <code>Minden-Lübbecke</code>.</p>"""
    postal_code: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess. </p>"""
    block: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>Name of the block. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>Name of sub-block. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    street: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The name of the street results should be present in.</p>"""
    address_number: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The number that identifies an address within a street.</p>"""
    building: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>The name of the building at the address.</p>"""
    secondary_address_components: NotRequired[
        "capo_geo_places.types.parsed_query_secondary_address_component_list.ParsedQuerySecondaryAddressComponentList"
    ]
    """<p>Parsed secondary address components from the provided query text.</p> <note> <p>Coverage for <code>ParsedQuery.Address.SecondaryAddressComponents</code> is available in the following countries:</p> <p>AUS, AUT, BRA, CAN, ESP, FRA, GBR, HKG, IDN, IND, NZL, TUR, TWN, USA</p> </note>"""
    other_components: NotRequired[
        "capo_geo_places.types.parsed_query_component_list.ParsedQueryComponentList"
    ]
    """<p>Additional information extracted from the query that does not correspond to standard address components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeParsedQueryAddressComponents) -> dict:
    out: dict = {}
    if "country" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Country"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["country"]
            )
        )
    if "region" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Region"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["region"]
            )
        )
    if "sub_region" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["SubRegion"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["sub_region"]
            )
        )
    if "locality" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Locality"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["locality"]
            )
        )
    if "district" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["District"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["district"]
            )
        )
    if "sub_district" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["SubDistrict"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["sub_district"]
            )
        )
    if "postal_code" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["PostalCode"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["postal_code"]
            )
        )
    if "block" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Block"] = capo_geo_places.types.parsed_query_component_list.serialize_json(
            value["block"]
        )
    if "sub_block" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["SubBlock"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["sub_block"]
            )
        )
    if "street" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Street"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["street"]
            )
        )
    if "address_number" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["AddressNumber"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["address_number"]
            )
        )
    if "building" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["Building"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["building"]
            )
        )
    if "secondary_address_components" in value:
        import capo_geo_places.types.parsed_query_secondary_address_component_list

        out["SecondaryAddressComponents"] = (
            capo_geo_places.types.parsed_query_secondary_address_component_list.serialize_json(
                value["secondary_address_components"]
            )
        )
    if "other_components" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["OtherComponents"] = (
            capo_geo_places.types.parsed_query_component_list.serialize_json(
                value["other_components"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeocodeParsedQueryAddressComponents:
    out: GeocodeParsedQueryAddressComponents = {}  # type: ignore[typeddict-item]
    if data.get("Country") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["country"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Country"]
            )
        )
    if data.get("Region") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["region"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Region"]
            )
        )
    if data.get("SubRegion") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["sub_region"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["SubRegion"]
            )
        )
    if data.get("Locality") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["locality"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Locality"]
            )
        )
    if data.get("District") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["district"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["District"]
            )
        )
    if data.get("SubDistrict") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["sub_district"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["SubDistrict"]
            )
        )
    if data.get("PostalCode") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["postal_code"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["PostalCode"]
            )
        )
    if data.get("Block") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["block"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Block"]
            )
        )
    if data.get("SubBlock") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["sub_block"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["SubBlock"]
            )
        )
    if data.get("Street") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["street"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Street"]
            )
        )
    if data.get("AddressNumber") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["address_number"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["AddressNumber"]
            )
        )
    if data.get("Building") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["building"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["Building"]
            )
        )
    if data.get("SecondaryAddressComponents") is not None:
        import capo_geo_places.types.parsed_query_secondary_address_component_list

        out["secondary_address_components"] = (
            capo_geo_places.types.parsed_query_secondary_address_component_list.deserialize_json(
                data["SecondaryAddressComponents"]
            )
        )
    if data.get("OtherComponents") is not None:
        import capo_geo_places.types.parsed_query_component_list

        out["other_components"] = (
            capo_geo_places.types.parsed_query_component_list.deserialize_json(
                data["OtherComponents"]
            )
        )
    return out


def redact_sensitive(value: GeocodeParsedQueryAddressComponents) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "country" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["country"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["country"]
            )
        )
    if "region" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["region"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["region"]
            )
        )
    if "sub_region" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["sub_region"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["sub_region"]
            )
        )
    if "locality" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["locality"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["locality"]
            )
        )
    if "district" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["district"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["district"]
            )
        )
    if "sub_district" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["sub_district"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["sub_district"]
            )
        )
    if "postal_code" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["postal_code"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["postal_code"]
            )
        )
    if "block" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["block"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["block"]
            )
        )
    if "sub_block" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["sub_block"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["sub_block"]
            )
        )
    if "street" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["street"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["street"]
            )
        )
    if "address_number" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["address_number"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["address_number"]
            )
        )
    if "building" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["building"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["building"]
            )
        )
    if "secondary_address_components" in value:
        import capo_geo_places.types.parsed_query_secondary_address_component_list

        out["secondary_address_components"] = (
            capo_geo_places.types.parsed_query_secondary_address_component_list.redact_sensitive(
                value["secondary_address_components"]
            )
        )
    if "other_components" in value:
        import capo_geo_places.types.parsed_query_component_list

        out["other_components"] = (
            capo_geo_places.types.parsed_query_component_list.redact_sensitive(
                value["other_components"]
            )
        )
    return out
