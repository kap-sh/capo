"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemsFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_id_list
    import capo_billingconductor.types.billing_group_arn_list
    import capo_billingconductor.types.custom_line_item_arns
    import capo_billingconductor.types.custom_line_item_name_list


class ListCustomLineItemsFilter(TypedDict, closed=True):
    names: NotRequired[
        "capo_billingconductor.types.custom_line_item_name_list.CustomLineItemNameList"
    ]
    """<p>A list of custom line items to retrieve information.</p>"""
    billing_groups: NotRequired[
        "capo_billingconductor.types.billing_group_arn_list.BillingGroupArnList"
    ]
    """<p>The billing group Amazon Resource Names (ARNs) to retrieve information.</p>"""
    arns: NotRequired[
        "capo_billingconductor.types.custom_line_item_arns.CustomLineItemArns"
    ]
    """<p>A list of custom line item ARNs to retrieve information.</p>"""
    account_ids: NotRequired[
        "capo_billingconductor.types.account_id_list.AccountIdList"
    ]
    """<p>The Amazon Web Services accounts in which this custom line item will be applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemsFilter) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_billingconductor.types.custom_line_item_name_list

        out["Names"] = (
            capo_billingconductor.types.custom_line_item_name_list.serialize_json(
                value["names"]
            )
        )
    if "billing_groups" in value:
        import capo_billingconductor.types.billing_group_arn_list

        out["BillingGroups"] = (
            capo_billingconductor.types.billing_group_arn_list.serialize_json(
                value["billing_groups"]
            )
        )
    if "arns" in value:
        import capo_billingconductor.types.custom_line_item_arns

        out["Arns"] = capo_billingconductor.types.custom_line_item_arns.serialize_json(
            value["arns"]
        )
    if "account_ids" in value:
        import capo_billingconductor.types.account_id_list

        out["AccountIds"] = capo_billingconductor.types.account_id_list.serialize_json(
            value["account_ids"]
        )
    return out


def deserialize_json(data: dict) -> ListCustomLineItemsFilter:
    out: ListCustomLineItemsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_billingconductor.types.custom_line_item_name_list

        out["names"] = (
            capo_billingconductor.types.custom_line_item_name_list.deserialize_json(
                data["Names"]
            )
        )
    if data.get("BillingGroups") is not None:
        import capo_billingconductor.types.billing_group_arn_list

        out["billing_groups"] = (
            capo_billingconductor.types.billing_group_arn_list.deserialize_json(
                data["BillingGroups"]
            )
        )
    if data.get("Arns") is not None:
        import capo_billingconductor.types.custom_line_item_arns

        out["arns"] = (
            capo_billingconductor.types.custom_line_item_arns.deserialize_json(
                data["Arns"]
            )
        )
    if data.get("AccountIds") is not None:
        import capo_billingconductor.types.account_id_list

        out["account_ids"] = (
            capo_billingconductor.types.account_id_list.deserialize_json(
                data["AccountIds"]
            )
        )
    return out


def redact_sensitive(value: ListCustomLineItemsFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "names" in value:
        import capo_billingconductor.types.custom_line_item_name_list

        out["names"] = (
            capo_billingconductor.types.custom_line_item_name_list.redact_sensitive(
                value["names"]
            )
        )
    return out
