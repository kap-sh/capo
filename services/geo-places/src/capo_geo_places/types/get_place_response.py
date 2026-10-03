"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.access_point_list
    import capo_geo_places.types.access_restriction_list
    import capo_geo_places.types.address
    import capo_geo_places.types.bounding_box
    import capo_geo_places.types.business_chain_list
    import capo_geo_places.types.category_list
    import capo_geo_places.types.contacts
    import capo_geo_places.types.country_code3
    import capo_geo_places.types.cross_reference_list
    import capo_geo_places.types.food_type_list
    import capo_geo_places.types.opening_hours_list
    import capo_geo_places.types.phoneme_details
    import capo_geo_places.types.place_attribute_list
    import capo_geo_places.types.place_type
    import capo_geo_places.types.position
    import capo_geo_places.types.postal_code_details_list
    import capo_geo_places.types.related_place
    import capo_geo_places.types.related_place_list
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.time_zone


class GetPlaceResponse(TypedDict, closed=True):
    place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>"""
    place_type: "capo_geo_places.types.place_type.PlaceType"
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    title: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p> <p>For more information on pricing, please visit <a href="https://aws.amazon.com/location/pricing/">Amazon Location Service Pricing</a>.</p>"""
    address: NotRequired["capo_geo_places.types.address.Address"]
    """<p>The place's address.</p>"""
    address_number_corrected: NotRequired[
        "capo_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p> Boolean indicating if the address provided has been corrected. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    postal_code_details: NotRequired[
        "capo_geo_places.types.postal_code_details_list.PostalCodeDetailsList"
    ]
    """<p> Contains details about the postal code of the place/result. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    map_view: NotRequired["capo_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set of four coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    categories: NotRequired["capo_geo_places.types.category_list.CategoryList"]
    """<p>Categories of results that results must belong to.</p>"""
    food_types: NotRequired["capo_geo_places.types.food_type_list.FoodTypeList"]
    """<p> List of food types offered by this result. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    business_chains: NotRequired[
        "capo_geo_places.types.business_chain_list.BusinessChainList"
    ]
    """<p>The Business Chains associated with the place.</p>"""
    contacts: NotRequired["capo_geo_places.types.contacts.Contacts"]
    """<p> List of potential contact methods for the result/place. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    opening_hours: NotRequired[
        "capo_geo_places.types.opening_hours_list.OpeningHoursList"
    ]
    """<p> List of opening hours objects. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    access_points: NotRequired[
        "capo_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p> Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    access_restrictions: NotRequired[
        "capo_geo_places.types.access_restriction_list.AccessRestrictionList"
    ]
    """<p> Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    time_zone: NotRequired["capo_geo_places.types.time_zone.TimeZone"]
    """<p>The time zone in which the place is located.</p>"""
    political_view: NotRequired["capo_geo_places.types.country_code3.CountryCode3"]
    """<p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    phonemes: NotRequired["capo_geo_places.types.phoneme_details.PhonemeDetails"]
    """<p> How the various components of the result's address are pronounced in various languages. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    main_address: NotRequired["capo_geo_places.types.related_place.RelatedPlace"]
    """<p> The main address corresponding to a place of type Secondary Address. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    secondary_addresses: NotRequired[
        "capo_geo_places.types.related_place_list.RelatedPlaceList"
    ]
    """<p> All secondary addresses that are associated with a main address. A secondary address is one that includes secondary designators, such as a Suite or Unit Number, Building, or Floor information. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>Coverage for this functionality is available in the following countries: AUS, CAN, NZL, USA, PRI.</p> </note>"""
    place_attributes: NotRequired[
        "capo_geo_places.types.place_attribute_list.PlaceAttributeList"
    ]
    """<p>A list of place attributes for the result, such as whether the business offers drive-through service.</p>"""
    estimated_point_address: NotRequired[
        "capo_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>If <code>true</code>, indicates that the coordinates of the position and access points of the point address are estimated.</p>"""
    cross_references: NotRequired[
        "capo_geo_places.types.cross_reference_list.CrossReferenceList"
    ]
    """<p>The list of supplier references available for this place. Requires the <code>CrossReferences</code> additional feature to be enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceResponse) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    import capo_geo_places.types.place_type

    out["PlaceType"] = capo_geo_places.types.place_type.serialize_json(
        value["place_type"]
    )
    out["Title"] = value["title"]
    if "address" in value:
        import capo_geo_places.types.address

        out["Address"] = capo_geo_places.types.address.serialize_json(value["address"])
    if "address_number_corrected" in value:
        out["AddressNumberCorrected"] = value["address_number_corrected"]
    if "postal_code_details" in value:
        import capo_geo_places.types.postal_code_details_list

        out["PostalCodeDetails"] = (
            capo_geo_places.types.postal_code_details_list.serialize_json(
                value["postal_code_details"]
            )
        )
    if "position" in value:
        import capo_geo_places.types.position

        out["Position"] = capo_geo_places.types.position.serialize_json(
            value["position"]
        )
    if "map_view" in value:
        import capo_geo_places.types.bounding_box

        out["MapView"] = capo_geo_places.types.bounding_box.serialize_json(
            value["map_view"]
        )
    if "categories" in value:
        import capo_geo_places.types.category_list

        out["Categories"] = capo_geo_places.types.category_list.serialize_json(
            value["categories"]
        )
    if "food_types" in value:
        import capo_geo_places.types.food_type_list

        out["FoodTypes"] = capo_geo_places.types.food_type_list.serialize_json(
            value["food_types"]
        )
    if "business_chains" in value:
        import capo_geo_places.types.business_chain_list

        out["BusinessChains"] = (
            capo_geo_places.types.business_chain_list.serialize_json(
                value["business_chains"]
            )
        )
    if "contacts" in value:
        import capo_geo_places.types.contacts

        out["Contacts"] = capo_geo_places.types.contacts.serialize_json(
            value["contacts"]
        )
    if "opening_hours" in value:
        import capo_geo_places.types.opening_hours_list

        out["OpeningHours"] = capo_geo_places.types.opening_hours_list.serialize_json(
            value["opening_hours"]
        )
    if "access_points" in value:
        import capo_geo_places.types.access_point_list

        out["AccessPoints"] = capo_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    if "access_restrictions" in value:
        import capo_geo_places.types.access_restriction_list

        out["AccessRestrictions"] = (
            capo_geo_places.types.access_restriction_list.serialize_json(
                value["access_restrictions"]
            )
        )
    if "time_zone" in value:
        import capo_geo_places.types.time_zone

        out["TimeZone"] = capo_geo_places.types.time_zone.serialize_json(
            value["time_zone"]
        )
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "phonemes" in value:
        import capo_geo_places.types.phoneme_details

        out["Phonemes"] = capo_geo_places.types.phoneme_details.serialize_json(
            value["phonemes"]
        )
    if "main_address" in value:
        import capo_geo_places.types.related_place

        out["MainAddress"] = capo_geo_places.types.related_place.serialize_json(
            value["main_address"]
        )
    if "secondary_addresses" in value:
        import capo_geo_places.types.related_place_list

        out["SecondaryAddresses"] = (
            capo_geo_places.types.related_place_list.serialize_json(
                value["secondary_addresses"]
            )
        )
    if "place_attributes" in value:
        import capo_geo_places.types.place_attribute_list

        out["PlaceAttributes"] = (
            capo_geo_places.types.place_attribute_list.serialize_json(
                value["place_attributes"]
            )
        )
    if "estimated_point_address" in value:
        out["EstimatedPointAddress"] = value["estimated_point_address"]
    if "cross_references" in value:
        import capo_geo_places.types.cross_reference_list

        out["CrossReferences"] = (
            capo_geo_places.types.cross_reference_list.serialize_json(
                value["cross_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPlaceResponse:
    out: GetPlaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("GetPlaceResponse.place_id required")
    if data.get("PlaceType") is not None:
        import capo_geo_places.types.place_type

        out["place_type"] = capo_geo_places.types.place_type.deserialize_json(
            data["PlaceType"]
        )
    else:
        raise DeserializationError("GetPlaceResponse.place_type required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("GetPlaceResponse.title required")
    if data.get("Address") is not None:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.deserialize_json(data["Address"])
    if data.get("AddressNumberCorrected") is not None:
        out["address_number_corrected"] = data["AddressNumberCorrected"]
    if data.get("PostalCodeDetails") is not None:
        import capo_geo_places.types.postal_code_details_list

        out["postal_code_details"] = (
            capo_geo_places.types.postal_code_details_list.deserialize_json(
                data["PostalCodeDetails"]
            )
        )
    if data.get("Position") is not None:
        import capo_geo_places.types.position

        out["position"] = capo_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if data.get("MapView") is not None:
        import capo_geo_places.types.bounding_box

        out["map_view"] = capo_geo_places.types.bounding_box.deserialize_json(
            data["MapView"]
        )
    if data.get("Categories") is not None:
        import capo_geo_places.types.category_list

        out["categories"] = capo_geo_places.types.category_list.deserialize_json(
            data["Categories"]
        )
    if data.get("FoodTypes") is not None:
        import capo_geo_places.types.food_type_list

        out["food_types"] = capo_geo_places.types.food_type_list.deserialize_json(
            data["FoodTypes"]
        )
    if data.get("BusinessChains") is not None:
        import capo_geo_places.types.business_chain_list

        out["business_chains"] = (
            capo_geo_places.types.business_chain_list.deserialize_json(
                data["BusinessChains"]
            )
        )
    if data.get("Contacts") is not None:
        import capo_geo_places.types.contacts

        out["contacts"] = capo_geo_places.types.contacts.deserialize_json(
            data["Contacts"]
        )
    if data.get("OpeningHours") is not None:
        import capo_geo_places.types.opening_hours_list

        out["opening_hours"] = (
            capo_geo_places.types.opening_hours_list.deserialize_json(
                data["OpeningHours"]
            )
        )
    if data.get("AccessPoints") is not None:
        import capo_geo_places.types.access_point_list

        out["access_points"] = capo_geo_places.types.access_point_list.deserialize_json(
            data["AccessPoints"]
        )
    if data.get("AccessRestrictions") is not None:
        import capo_geo_places.types.access_restriction_list

        out["access_restrictions"] = (
            capo_geo_places.types.access_restriction_list.deserialize_json(
                data["AccessRestrictions"]
            )
        )
    if data.get("TimeZone") is not None:
        import capo_geo_places.types.time_zone

        out["time_zone"] = capo_geo_places.types.time_zone.deserialize_json(
            data["TimeZone"]
        )
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("Phonemes") is not None:
        import capo_geo_places.types.phoneme_details

        out["phonemes"] = capo_geo_places.types.phoneme_details.deserialize_json(
            data["Phonemes"]
        )
    if data.get("MainAddress") is not None:
        import capo_geo_places.types.related_place

        out["main_address"] = capo_geo_places.types.related_place.deserialize_json(
            data["MainAddress"]
        )
    if data.get("SecondaryAddresses") is not None:
        import capo_geo_places.types.related_place_list

        out["secondary_addresses"] = (
            capo_geo_places.types.related_place_list.deserialize_json(
                data["SecondaryAddresses"]
            )
        )
    if data.get("PlaceAttributes") is not None:
        import capo_geo_places.types.place_attribute_list

        out["place_attributes"] = (
            capo_geo_places.types.place_attribute_list.deserialize_json(
                data["PlaceAttributes"]
            )
        )
    if data.get("EstimatedPointAddress") is not None:
        out["estimated_point_address"] = data["EstimatedPointAddress"]
    if data.get("CrossReferences") is not None:
        import capo_geo_places.types.cross_reference_list

        out["cross_references"] = (
            capo_geo_places.types.cross_reference_list.deserialize_json(
                data["CrossReferences"]
            )
        )
    return out
