"""Generated from Smithy shape ``com.amazonaws.chime#CreatePhoneNumberOrderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.e164_phone_number_list
    import capo_chime.types.phone_number_product_type


class CreatePhoneNumberOrderRequest(TypedDict, closed=True):
    product_type: "capo_chime.types.phone_number_product_type.PhoneNumberProductType"
    """<p>The phone number product type.</p>"""
    e164_phone_numbers: "capo_chime.types.e164_phone_number_list.E164PhoneNumberList"
    """<p>List of phone numbers, in E.164 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePhoneNumberOrderRequest) -> dict:
    out: dict = {}
    import capo_chime.types.phone_number_product_type

    out["ProductType"] = capo_chime.types.phone_number_product_type.serialize_json(
        value["product_type"]
    )
    import capo_chime.types.e164_phone_number_list

    out["E164PhoneNumbers"] = capo_chime.types.e164_phone_number_list.serialize_json(
        value["e164_phone_numbers"]
    )
    return out


def deserialize_json(data: dict) -> CreatePhoneNumberOrderRequest:
    out: CreatePhoneNumberOrderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProductType") is not None:
        import capo_chime.types.phone_number_product_type

        out["product_type"] = (
            capo_chime.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePhoneNumberOrderRequest.product_type required"
        )
    if data.get("E164PhoneNumbers") is not None:
        import capo_chime.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime.types.e164_phone_number_list.deserialize_json(
                data["E164PhoneNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePhoneNumberOrderRequest.e164_phone_numbers required"
        )
    return out


def redact_sensitive(value: CreatePhoneNumberOrderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "e164_phone_numbers" in value:
        import capo_chime.types.e164_phone_number_list

        out["e164_phone_numbers"] = (
            capo_chime.types.e164_phone_number_list.redact_sensitive(
                value["e164_phone_numbers"]
            )
        )
    return out
