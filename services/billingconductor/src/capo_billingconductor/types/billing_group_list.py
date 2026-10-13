"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_list_element

BillingGroupList: TypeAlias = list[
    "capo_billingconductor.types.billing_group_list_element.BillingGroupListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupList) -> list:
    import capo_billingconductor.types.billing_group_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.billing_group_list_element.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BillingGroupList:
    import capo_billingconductor.types.billing_group_list_element

    out: BillingGroupList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billingconductor.types.billing_group_list_element.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: BillingGroupList) -> list[Any]:
    import capo_billingconductor.types.billing_group_list_element

    return [
        capo_billingconductor.types.billing_group_list_element.redact_sensitive(item)
        for item in value
    ]
