"""Generated from Smithy shape ``com.amazonaws.geoplaces#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.country
    import capo_geo_places.types.intersection_street_list
    import capo_geo_places.types.region
    import capo_geo_places.types.secondary_address_component_list
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.street_components_list
    import capo_geo_places.types.sub_region


class Address(TypedDict, closed=True):
    label: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>Assembled address value built out of the address components, according to the regional postal rules. This is the correctly formatted address.</p>"""
    country: NotRequired["capo_geo_places.types.country.Country"]
    """<p>The country component of the address.</p>"""
    region: NotRequired["capo_geo_places.types.region.Region"]
    """<p>The region or state results should be present in. </p> <p>Example: <code>North Rhine-Westphalia</code>.</p>"""
    sub_region: NotRequired["capo_geo_places.types.sub_region.SubRegion"]
    """<p>The sub-region or county for which results should be present in. </p>"""
    locality: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The city or locality of the address.</p> <p>Example: <code>Vancouver</code>.</p>"""
    district: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The district or division of a locality associated with this address.</p>"""
    sub_district: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>A subdivision of a district. </p> <p>Example: <code>Minden-Lübbecke</code>.</p>"""
    postal_code: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code, for which the result should possess. </p>"""
    block: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p> Name of the block. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Example: <code>Sunny Mansion 203 block: 2 Chome</code> </p>"""
    sub_block: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p> Name of sub-block. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Example: <code>Sunny Mansion 203 sub-block: 4</code> </p>"""
    intersection: NotRequired[
        "capo_geo_places.types.intersection_street_list.IntersectionStreetList"
    ]
    """<p> Name of the streets in the intersection. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Example: <code>["Friedrichstraße","Unter den Linden"]</code> </p>"""
    street: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The name of the street results should be present in.</p>"""
    street_components: NotRequired[
        "capo_geo_places.types.street_components_list.StreetComponentsList"
    ]
    """<p> Components of the street. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <p>Example: Yonge from "Yonge street".</p>"""
    address_number: NotRequired[
        "capo_geo_places.types.sensitive_string.SensitiveString"
    ]
    """<p>The number that identifies an address within a street.</p>"""
    building: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p> The name of the building at the address. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    secondary_address_components: NotRequired[
        "capo_geo_places.types.secondary_address_component_list.SecondaryAddressComponentList"
    ]
    """<p> Components that correspond to secondary identifiers on an Address. Secondary address components include information such as Suite or Unit Number, Building, or Floor. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>Coverage for <code>Address.SecondaryAddressComponents</code> is available in the following countries:</p> <p>AUS, CAN, NZL, USA, PRI</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Address) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "country" in value:
        import capo_geo_places.types.country

        out["Country"] = capo_geo_places.types.country.serialize_json(value["country"])
    if "region" in value:
        import capo_geo_places.types.region

        out["Region"] = capo_geo_places.types.region.serialize_json(value["region"])
    if "sub_region" in value:
        import capo_geo_places.types.sub_region

        out["SubRegion"] = capo_geo_places.types.sub_region.serialize_json(
            value["sub_region"]
        )
    if "locality" in value:
        out["Locality"] = value["locality"]
    if "district" in value:
        out["District"] = value["district"]
    if "sub_district" in value:
        out["SubDistrict"] = value["sub_district"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "block" in value:
        out["Block"] = value["block"]
    if "sub_block" in value:
        out["SubBlock"] = value["sub_block"]
    if "intersection" in value:
        import capo_geo_places.types.intersection_street_list

        out["Intersection"] = (
            capo_geo_places.types.intersection_street_list.serialize_json(
                value["intersection"]
            )
        )
    if "street" in value:
        out["Street"] = value["street"]
    if "street_components" in value:
        import capo_geo_places.types.street_components_list

        out["StreetComponents"] = (
            capo_geo_places.types.street_components_list.serialize_json(
                value["street_components"]
            )
        )
    if "address_number" in value:
        out["AddressNumber"] = value["address_number"]
    if "building" in value:
        out["Building"] = value["building"]
    if "secondary_address_components" in value:
        import capo_geo_places.types.secondary_address_component_list

        out["SecondaryAddressComponents"] = (
            capo_geo_places.types.secondary_address_component_list.serialize_json(
                value["secondary_address_components"]
            )
        )
    return out


def deserialize_json(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Country") is not None:
        import capo_geo_places.types.country

        out["country"] = capo_geo_places.types.country.deserialize_json(data["Country"])
    if data.get("Region") is not None:
        import capo_geo_places.types.region

        out["region"] = capo_geo_places.types.region.deserialize_json(data["Region"])
    if data.get("SubRegion") is not None:
        import capo_geo_places.types.sub_region

        out["sub_region"] = capo_geo_places.types.sub_region.deserialize_json(
            data["SubRegion"]
        )
    if data.get("Locality") is not None:
        out["locality"] = data["Locality"]
    if data.get("District") is not None:
        out["district"] = data["District"]
    if data.get("SubDistrict") is not None:
        out["sub_district"] = data["SubDistrict"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("Block") is not None:
        out["block"] = data["Block"]
    if data.get("SubBlock") is not None:
        out["sub_block"] = data["SubBlock"]
    if data.get("Intersection") is not None:
        import capo_geo_places.types.intersection_street_list

        out["intersection"] = (
            capo_geo_places.types.intersection_street_list.deserialize_json(
                data["Intersection"]
            )
        )
    if data.get("Street") is not None:
        out["street"] = data["Street"]
    if data.get("StreetComponents") is not None:
        import capo_geo_places.types.street_components_list

        out["street_components"] = (
            capo_geo_places.types.street_components_list.deserialize_json(
                data["StreetComponents"]
            )
        )
    if data.get("AddressNumber") is not None:
        out["address_number"] = data["AddressNumber"]
    if data.get("Building") is not None:
        out["building"] = data["Building"]
    if data.get("SecondaryAddressComponents") is not None:
        import capo_geo_places.types.secondary_address_component_list

        out["secondary_address_components"] = (
            capo_geo_places.types.secondary_address_component_list.deserialize_json(
                data["SecondaryAddressComponents"]
            )
        )
    return out
