"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumber``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.alpha2_country_code
    import capo_chime_sdk_voice.types.calling_name
    import capo_chime_sdk_voice.types.calling_name_status
    import capo_chime_sdk_voice.types.e164_phone_number
    import capo_chime_sdk_voice.types.guid_string
    import capo_chime_sdk_voice.types.iso8601_timestamp
    import capo_chime_sdk_voice.types.non_empty_string
    import capo_chime_sdk_voice.types.phone_number_association_list
    import capo_chime_sdk_voice.types.phone_number_capabilities
    import capo_chime_sdk_voice.types.phone_number_name
    import capo_chime_sdk_voice.types.phone_number_product_type
    import capo_chime_sdk_voice.types.phone_number_status
    import capo_chime_sdk_voice.types.phone_number_type
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class PhoneNumber(TypedDict, closed=True):
    phone_number_id: NotRequired[
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The phone number's ID.</p>"""
    e164_phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The phone number, in E.164 format.</p>"""
    phone_number_arn: NotRequired[
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    country: NotRequired[
        "capo_chime_sdk_voice.types.alpha2_country_code.Alpha2CountryCode"
    ]
    """<p>The phone number's country. Format: ISO 3166-1 alpha-2.</p>"""
    type: NotRequired["capo_chime_sdk_voice.types.phone_number_type.PhoneNumberType"]
    """<p>The phone number's type.</p>"""
    product_type: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The phone number's product type.</p>"""
    status: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_status.PhoneNumberStatus"
    ]
    """<p>The phone number's status.</p>"""
    capabilities: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_capabilities.PhoneNumberCapabilities"
    ]
    """<p>The phone number's capabilities.</p>"""
    associations: NotRequired[
        "capo_chime_sdk_voice.types.phone_number_association_list.PhoneNumberAssociationList"
    ]
    """<p>The phone number's associations.</p>"""
    calling_name: NotRequired["capo_chime_sdk_voice.types.calling_name.CallingName"]
    """<p>The outbound calling name associated with the phone number.</p>"""
    calling_name_status: NotRequired[
        "capo_chime_sdk_voice.types.calling_name_status.CallingNameStatus"
    ]
    """<p>The outbound calling name status.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The phone number creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated phone number timestamp, in ISO 8601 format.</p>"""
    deletion_timestamp: NotRequired[
        "capo_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The deleted phone number timestamp, in ISO 8601 format.</p>"""
    order_id: NotRequired["capo_chime_sdk_voice.types.guid_string.GuidString"]
    """<p>The phone number's order ID.</p>"""
    name: NotRequired["capo_chime_sdk_voice.types.phone_number_name.PhoneNumberName"]
    """<p>The name of the phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumber) -> dict:
    out: dict = {}
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    if "e164_phone_number" in value:
        out["E164PhoneNumber"] = value["e164_phone_number"]
    if "phone_number_arn" in value:
        out["PhoneNumberArn"] = value["phone_number_arn"]
    if "country" in value:
        out["Country"] = value["country"]
    if "type" in value:
        import capo_chime_sdk_voice.types.phone_number_type

        out["Type"] = capo_chime_sdk_voice.types.phone_number_type.serialize_json(
            value["type"]
        )
    if "product_type" in value:
        import capo_chime_sdk_voice.types.phone_number_product_type

        out["ProductType"] = (
            capo_chime_sdk_voice.types.phone_number_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "status" in value:
        import capo_chime_sdk_voice.types.phone_number_status

        out["Status"] = capo_chime_sdk_voice.types.phone_number_status.serialize_json(
            value["status"]
        )
    if "capabilities" in value:
        import capo_chime_sdk_voice.types.phone_number_capabilities

        out["Capabilities"] = (
            capo_chime_sdk_voice.types.phone_number_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    if "associations" in value:
        import capo_chime_sdk_voice.types.phone_number_association_list

        out["Associations"] = (
            capo_chime_sdk_voice.types.phone_number_association_list.serialize_json(
                value["associations"]
            )
        )
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
    if "calling_name_status" in value:
        import capo_chime_sdk_voice.types.calling_name_status

        out["CallingNameStatus"] = (
            capo_chime_sdk_voice.types.calling_name_status.serialize_json(
                value["calling_name_status"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "deletion_timestamp" in value:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["DeletionTimestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["deletion_timestamp"]
            )
        )
    if "order_id" in value:
        out["OrderId"] = value["order_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> PhoneNumber:
    out: PhoneNumber = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    if data.get("E164PhoneNumber") is not None:
        out["e164_phone_number"] = data["E164PhoneNumber"]
    if data.get("PhoneNumberArn") is not None:
        out["phone_number_arn"] = data["PhoneNumberArn"]
    if data.get("Country") is not None:
        out["country"] = data["Country"]
    if data.get("Type") is not None:
        import capo_chime_sdk_voice.types.phone_number_type

        out["type"] = capo_chime_sdk_voice.types.phone_number_type.deserialize_json(
            data["Type"]
        )
    if data.get("ProductType") is not None:
        import capo_chime_sdk_voice.types.phone_number_product_type

        out["product_type"] = (
            capo_chime_sdk_voice.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if data.get("Status") is not None:
        import capo_chime_sdk_voice.types.phone_number_status

        out["status"] = capo_chime_sdk_voice.types.phone_number_status.deserialize_json(
            data["Status"]
        )
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_voice.types.phone_number_capabilities

        out["capabilities"] = (
            capo_chime_sdk_voice.types.phone_number_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    if data.get("Associations") is not None:
        import capo_chime_sdk_voice.types.phone_number_association_list

        out["associations"] = (
            capo_chime_sdk_voice.types.phone_number_association_list.deserialize_json(
                data["Associations"]
            )
        )
    if data.get("CallingName") is not None:
        out["calling_name"] = data["CallingName"]
    if data.get("CallingNameStatus") is not None:
        import capo_chime_sdk_voice.types.calling_name_status

        out["calling_name_status"] = (
            capo_chime_sdk_voice.types.calling_name_status.deserialize_json(
                data["CallingNameStatus"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if data.get("DeletionTimestamp") is not None:
        import capo_chime_sdk_voice.types.iso8601_timestamp

        out["deletion_timestamp"] = (
            capo_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["DeletionTimestamp"]
            )
        )
    if data.get("OrderId") is not None:
        out["order_id"] = data["OrderId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: PhoneNumber) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number_id" in value:
        out["phone_number_id"] = "*** Sensitive Data Redacted ***"
    if "e164_phone_number" in value:
        out["e164_phone_number"] = "*** Sensitive Data Redacted ***"
    if "calling_name" in value:
        out["calling_name"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
