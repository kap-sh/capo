"""Generated from Smithy shape ``com.amazonaws.location#Place``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.place_category_list
    import capo_location.types.place_geometry
    import capo_location.types.place_supplemental_category_list
    import capo_location.types.sensitive_boolean
    import capo_location.types.sensitive_string
    import capo_location.types.time_zone


class Place(TypedDict, closed=True):
    label: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>The full name and address of the point of interest such as a city, region, or country. For example, <code>123 Any Street, Any Town, USA</code>.</p>"""
    geometry: "capo_location.types.place_geometry.PlaceGeometry"
    address_number: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>The numerical portion of an address, such as a building number. </p>"""
    street: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>The name for a street or a road to identify a location. For example, <code>Main Street</code>.</p>"""
    neighborhood: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>The name of a community district. For example, <code>Downtown</code>.</p>"""
    municipality: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>A name for a local area, such as a city or town name. For example, <code>Toronto</code>.</p>"""
    sub_region: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>A county, or an area that's part of a larger region. For example, <code>Metro Vancouver</code>.</p>"""
    region: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>A name for an area or geographical division, such as a province or state name. For example, <code>British Columbia</code>.</p>"""
    country: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>A country/region specified using <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country/region code. For example, <code>CAN</code>.</p>"""
    postal_code: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>A group of numbers and letters in a country-specific format, which accompanies the address for the purpose of identifying a location. </p>"""
    interpolated: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p> <code>True</code> if the result is interpolated from other known places.</p> <p> <code>False</code> if the Place is a known place.</p> <p>Not returned when the partner does not provide the information.</p> <p>For example, returns <code>False</code> for an address location that is found in the partner data, but returns <code>True</code> if an address does not exist in the partner data and its location is calculated by interpolating between other known addresses. </p>"""
    time_zone: NotRequired["capo_location.types.time_zone.TimeZone"]
    """<p>The time zone in which the <code>Place</code> is located. Returned only when using HERE or Grab as the selected partner.</p>"""
    unit_type: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>For addresses with a <code>UnitNumber</code>, the type of unit. For example, <code>Apartment</code>.</p> <note> <p>Returned only for a place index that uses Esri as a data provider.</p> </note>"""
    unit_number: NotRequired["capo_location.types.sensitive_string.SensitiveString"]
    """<p>For addresses with multiple units, the unit identifier. Can include numbers and letters, for example <code>3B</code> or <code>Unit 123</code>.</p> <note> <p>Returned only for a place index that uses Esri or Grab as a data provider. Is not returned for <code>SearchPlaceIndexForPosition</code>.</p> </note>"""
    categories: NotRequired["capo_location.types.place_category_list.PlaceCategoryList"]
    """<p>The Amazon Location categories that describe this Place.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>"""
    supplemental_categories: NotRequired[
        "capo_location.types.place_supplemental_category_list.PlaceSupplementalCategoryList"
    ]
    """<p>Categories from the data provider that describe the Place that are not mapped to any Amazon Location categories.</p>"""
    sub_municipality: NotRequired[
        "capo_location.types.sensitive_string.SensitiveString"
    ]
    """<p>An area that's part of a larger municipality. For example, <code>Blissville </code> is a submunicipality in the Queen County in New York.</p> <note> <p>This property supported by Esri and OpenData. The Esri property is <code>district</code>, and the OpenData property is <code>borough</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: Place) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    import capo_location.types.place_geometry

    out["Geometry"] = capo_location.types.place_geometry.serialize_json(
        value["geometry"]
    )
    if "address_number" in value:
        out["AddressNumber"] = value["address_number"]
    if "street" in value:
        out["Street"] = value["street"]
    if "neighborhood" in value:
        out["Neighborhood"] = value["neighborhood"]
    if "municipality" in value:
        out["Municipality"] = value["municipality"]
    if "sub_region" in value:
        out["SubRegion"] = value["sub_region"]
    if "region" in value:
        out["Region"] = value["region"]
    if "country" in value:
        out["Country"] = value["country"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "interpolated" in value:
        out["Interpolated"] = value["interpolated"]
    if "time_zone" in value:
        import capo_location.types.time_zone

        out["TimeZone"] = capo_location.types.time_zone.serialize_json(
            value["time_zone"]
        )
    if "unit_type" in value:
        out["UnitType"] = value["unit_type"]
    if "unit_number" in value:
        out["UnitNumber"] = value["unit_number"]
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
    if "sub_municipality" in value:
        out["SubMunicipality"] = value["sub_municipality"]
    return out


def deserialize_json(data: dict) -> Place:
    out: Place = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Geometry") is not None:
        import capo_location.types.place_geometry

        out["geometry"] = capo_location.types.place_geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("Place.geometry required")
    if data.get("AddressNumber") is not None:
        out["address_number"] = data["AddressNumber"]
    if data.get("Street") is not None:
        out["street"] = data["Street"]
    if data.get("Neighborhood") is not None:
        out["neighborhood"] = data["Neighborhood"]
    if data.get("Municipality") is not None:
        out["municipality"] = data["Municipality"]
    if data.get("SubRegion") is not None:
        out["sub_region"] = data["SubRegion"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("Interpolated") is not None:
        out["interpolated"] = data["Interpolated"]
    if data.get("TimeZone") is not None:
        import capo_location.types.time_zone

        out["time_zone"] = capo_location.types.time_zone.deserialize_json(
            data["TimeZone"]
        )
    if data.get("UnitType") is not None:
        out["unit_type"] = data["UnitType"]
    if data.get("UnitNumber") is not None:
        out["unit_number"] = data["UnitNumber"]
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
    if data.get("SubMunicipality") is not None:
        out["sub_municipality"] = data["SubMunicipality"]
    return out
