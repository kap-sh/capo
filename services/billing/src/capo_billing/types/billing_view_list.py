"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_view_list_element

BillingViewList: TypeAlias = list[
    "capo_billing.types.billing_view_list_element.BillingViewListElement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewList) -> list:
    import capo_billing.types.billing_view_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.billing_view_list_element.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingViewList:
    import capo_billing.types.billing_view_list_element

    out: BillingViewList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.billing_view_list_element.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: BillingViewList) -> list[Any]:
    import capo_billing.types.billing_view_list_element

    return [
        capo_billing.types.billing_view_list_element.redact_sensitive(item)
        for item in value
    ]
