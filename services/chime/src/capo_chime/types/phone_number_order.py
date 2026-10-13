"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberOrder``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.guid_string
    import capo_chime.types.iso8601_timestamp
    import capo_chime.types.ordered_phone_number_list
    import capo_chime.types.phone_number_order_status
    import capo_chime.types.phone_number_product_type


class PhoneNumberOrder(TypedDict, closed=True):
    phone_number_order_id: NotRequired["capo_chime.types.guid_string.GuidString"]
    """<p>The phone number order ID.</p>"""
    product_type: NotRequired[
        "capo_chime.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The phone number order product type.</p>"""
    status: NotRequired[
        "capo_chime.types.phone_number_order_status.PhoneNumberOrderStatus"
    ]
    """<p>The status of the phone number order.</p>"""
    ordered_phone_numbers: NotRequired[
        "capo_chime.types.ordered_phone_number_list.OrderedPhoneNumberList"
    ]
    """<p>The ordered phone number details, such as the phone number in E.164 format and the phone number status.</p>"""
    created_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The phone number order creation time stamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated phone number order time stamp, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberOrder) -> dict:
    out: dict = {}
    if "phone_number_order_id" in value:
        out["PhoneNumberOrderId"] = value["phone_number_order_id"]
    if "product_type" in value:
        import capo_chime.types.phone_number_product_type

        out["ProductType"] = capo_chime.types.phone_number_product_type.serialize_json(
            value["product_type"]
        )
    if "status" in value:
        import capo_chime.types.phone_number_order_status

        out["Status"] = capo_chime.types.phone_number_order_status.serialize_json(
            value["status"]
        )
    if "ordered_phone_numbers" in value:
        import capo_chime.types.ordered_phone_number_list

        out["OrderedPhoneNumbers"] = (
            capo_chime.types.ordered_phone_number_list.serialize_json(
                value["ordered_phone_numbers"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["CreatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["UpdatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberOrder:
    out: PhoneNumberOrder = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberOrderId") is not None:
        out["phone_number_order_id"] = data["PhoneNumberOrderId"]
    if data.get("ProductType") is not None:
        import capo_chime.types.phone_number_product_type

        out["product_type"] = (
            capo_chime.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if data.get("Status") is not None:
        import capo_chime.types.phone_number_order_status

        out["status"] = capo_chime.types.phone_number_order_status.deserialize_json(
            data["Status"]
        )
    if data.get("OrderedPhoneNumbers") is not None:
        import capo_chime.types.ordered_phone_number_list

        out["ordered_phone_numbers"] = (
            capo_chime.types.ordered_phone_number_list.deserialize_json(
                data["OrderedPhoneNumbers"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["created_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["updated_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["UpdatedTimestamp"]
        )
    return out


def redact_sensitive(value: PhoneNumberOrder) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ordered_phone_numbers" in value:
        import capo_chime.types.ordered_phone_number_list

        out["ordered_phone_numbers"] = (
            capo_chime.types.ordered_phone_number_list.redact_sensitive(
                value["ordered_phone_numbers"]
            )
        )
    return out
