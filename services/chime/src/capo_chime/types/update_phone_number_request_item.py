"""Generated from Smithy shape ``com.amazonaws.chime#UpdatePhoneNumberRequestItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.calling_name
    import capo_chime.types.non_empty_string
    import capo_chime.types.phone_number_product_type


class UpdatePhoneNumberRequestItem(TypedDict, closed=True):
    phone_number_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The phone number ID to update.</p>"""
    product_type: NotRequired[
        "capo_chime.types.phone_number_product_type.PhoneNumberProductType"
    ]
    """<p>The product type to update.</p>"""
    calling_name: NotRequired["capo_chime.types.calling_name.CallingName"]
    """<p>The outbound calling name to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberRequestItem) -> dict:
    out: dict = {}
    out["PhoneNumberId"] = value["phone_number_id"]
    if "product_type" in value:
        import capo_chime.types.phone_number_product_type

        out["ProductType"] = capo_chime.types.phone_number_product_type.serialize_json(
            value["product_type"]
        )
    if "calling_name" in value:
        out["CallingName"] = value["calling_name"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberRequestItem:
    out: UpdatePhoneNumberRequestItem = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberId") is not None:
        out["phone_number_id"] = data["PhoneNumberId"]
    else:
        out["phone_number_id"] = ""
    if data.get("ProductType") is not None:
        import capo_chime.types.phone_number_product_type

        out["product_type"] = (
            capo_chime.types.phone_number_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if data.get("CallingName") is not None:
        out["calling_name"] = data["CallingName"]
    return out


def redact_sensitive(value: UpdatePhoneNumberRequestItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "calling_name" in value:
        out["calling_name"] = "*** Sensitive Data Redacted ***"
    return out
