"""Generated from Smithy shape ``com.amazonaws.snowball#Address``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.address_id
    import capo_snowball.types.address_type
    import capo_snowball.types.boolean
    import capo_snowball.types.string


class Address(TypedDict, closed=True):
    address_id: NotRequired["capo_snowball.types.address_id.AddressId"]
    """<p>The unique ID for an address.</p>"""
    name: NotRequired["capo_snowball.types.string.String"]
    """<p>The name of a person to receive a Snow device at an address.</p>"""
    company: NotRequired["capo_snowball.types.string.String"]
    """<p>The name of the company to receive a Snow device at an address.</p>"""
    street1: NotRequired["capo_snowball.types.string.String"]
    """<p>The first line in a street address that a Snow device is to be delivered to.</p>"""
    street2: NotRequired["capo_snowball.types.string.String"]
    """<p>The second line in a street address that a Snow device is to be delivered to.</p>"""
    street3: NotRequired["capo_snowball.types.string.String"]
    """<p>The third line in a street address that a Snow device is to be delivered to.</p>"""
    city: NotRequired["capo_snowball.types.string.String"]
    """<p>The city in an address that a Snow device is to be delivered to.</p>"""
    state_or_province: NotRequired["capo_snowball.types.string.String"]
    """<p>The state or province in an address that a Snow device is to be delivered to.</p>"""
    prefecture_or_district: NotRequired["capo_snowball.types.string.String"]
    """<p>This field is no longer used and the value is ignored.</p>"""
    landmark: NotRequired["capo_snowball.types.string.String"]
    """<p>This field is no longer used and the value is ignored.</p>"""
    country: NotRequired["capo_snowball.types.string.String"]
    """<p>The country in an address that a Snow device is to be delivered to.</p>"""
    postal_code: NotRequired["capo_snowball.types.string.String"]
    """<p>The postal code in an address that a Snow device is to be delivered to.</p>"""
    phone_number: NotRequired["capo_snowball.types.string.String"]
    """<p>The phone number associated with an address that a Snow device is to be delivered to.</p>"""
    is_restricted: "capo_snowball.types.boolean.Boolean"
    """<p>If the address you are creating is a primary address, then set this option to true. This field is not supported in most regions.</p>"""
    type: NotRequired["capo_snowball.types.address_type.AddressType"]
    """<p>Differentiates between delivery address and pickup address in the customer account. Provided at job creation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Address) -> dict:
    out: dict = {}
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "company" in value:
        out["Company"] = value["company"]
    if "street1" in value:
        out["Street1"] = value["street1"]
    if "street2" in value:
        out["Street2"] = value["street2"]
    if "street3" in value:
        out["Street3"] = value["street3"]
    if "city" in value:
        out["City"] = value["city"]
    if "state_or_province" in value:
        out["StateOrProvince"] = value["state_or_province"]
    if "prefecture_or_district" in value:
        out["PrefectureOrDistrict"] = value["prefecture_or_district"]
    if "landmark" in value:
        out["Landmark"] = value["landmark"]
    if "country" in value:
        out["Country"] = value["country"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    out["IsRestricted"] = value.get("is_restricted", False)
    if "type" in value:
        import capo_snowball.types.address_type

        out["Type"] = capo_snowball.types.address_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Company") is not None:
        out["company"] = data["Company"]
    if data.get("Street1") is not None:
        out["street1"] = data["Street1"]
    if data.get("Street2") is not None:
        out["street2"] = data["Street2"]
    if data.get("Street3") is not None:
        out["street3"] = data["Street3"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("StateOrProvince") is not None:
        out["state_or_province"] = data["StateOrProvince"]
    if data.get("PrefectureOrDistrict") is not None:
        out["prefecture_or_district"] = data["PrefectureOrDistrict"]
    if data.get("Landmark") is not None:
        out["landmark"] = data["Landmark"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("IsRestricted") is not None:
        out["is_restricted"] = data["IsRestricted"]
    else:
        out["is_restricted"] = False
    if data.get("Type") is not None:
        import capo_snowball.types.address_type

        out["type"] = capo_snowball.types.address_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Address) -> dict:
    out: dict = {}
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "company" in value:
        out["Company"] = value["company"]
    if "street1" in value:
        out["Street1"] = value["street1"]
    if "street2" in value:
        out["Street2"] = value["street2"]
    if "street3" in value:
        out["Street3"] = value["street3"]
    if "city" in value:
        out["City"] = value["city"]
    if "state_or_province" in value:
        out["StateOrProvince"] = value["state_or_province"]
    if "prefecture_or_district" in value:
        out["PrefectureOrDistrict"] = value["prefecture_or_district"]
    if "landmark" in value:
        out["Landmark"] = value["landmark"]
    if "country" in value:
        out["Country"] = value["country"]
    if "postal_code" in value:
        out["PostalCode"] = value["postal_code"]
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    out["IsRestricted"] = value.get("is_restricted", False)
    if "type" in value:
        import capo_snowball.types.address_type

        out["Type"] = capo_snowball.types.address_type.serialize_cbor(value["type"])
    return out


def deserialize_cbor(data: dict) -> Address:
    out: Address = {}  # type: ignore[typeddict-item]
    if data.get("AddressId") is not None:
        out["address_id"] = data["AddressId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Company") is not None:
        out["company"] = data["Company"]
    if data.get("Street1") is not None:
        out["street1"] = data["Street1"]
    if data.get("Street2") is not None:
        out["street2"] = data["Street2"]
    if data.get("Street3") is not None:
        out["street3"] = data["Street3"]
    if data.get("City") is not None:
        out["city"] = data["City"]
    if data.get("StateOrProvince") is not None:
        out["state_or_province"] = data["StateOrProvince"]
    if data.get("PrefectureOrDistrict") is not None:
        out["prefecture_or_district"] = data["PrefectureOrDistrict"]
    if data.get("Landmark") is not None:
        out["landmark"] = data["Landmark"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("PostalCode") is not None:
        out["postal_code"] = data["PostalCode"]
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    if data.get("IsRestricted") is not None:
        out["is_restricted"] = data["IsRestricted"]
    else:
        out["is_restricted"] = False
    if data.get("Type") is not None:
        import capo_snowball.types.address_type

        out["type"] = capo_snowball.types.address_type.deserialize_cbor(data["Type"])
    return out
