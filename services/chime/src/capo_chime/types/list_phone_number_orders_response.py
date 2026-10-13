"""Generated from Smithy shape ``com.amazonaws.chime#ListPhoneNumberOrdersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.phone_number_order_list
    import capo_chime.types.string


class ListPhoneNumberOrdersResponse(TypedDict, closed=True):
    phone_number_orders: NotRequired[
        "capo_chime.types.phone_number_order_list.PhoneNumberOrderList"
    ]
    """<p>The phone number order details.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumberOrdersResponse) -> dict:
    out: dict = {}
    if "phone_number_orders" in value:
        import capo_chime.types.phone_number_order_list

        out["PhoneNumberOrders"] = (
            capo_chime.types.phone_number_order_list.serialize_json(
                value["phone_number_orders"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPhoneNumberOrdersResponse:
    out: ListPhoneNumberOrdersResponse = {}  # type: ignore[typeddict-item]
    if data.get("PhoneNumberOrders") is not None:
        import capo_chime.types.phone_number_order_list

        out["phone_number_orders"] = (
            capo_chime.types.phone_number_order_list.deserialize_json(
                data["PhoneNumberOrders"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListPhoneNumberOrdersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "phone_number_orders" in value:
        import capo_chime.types.phone_number_order_list

        out["phone_number_orders"] = (
            capo_chime.types.phone_number_order_list.redact_sensitive(
                value["phone_number_orders"]
            )
        )
    return out
