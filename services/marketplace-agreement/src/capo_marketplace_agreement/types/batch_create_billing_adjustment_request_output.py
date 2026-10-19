"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_error_list
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_item_list


class BatchCreateBillingAdjustmentRequestOutput(TypedDict, closed=True):
    items: "capo_marketplace_agreement.types.batch_create_billing_adjustment_item_list.BatchCreateBillingAdjustmentItemList"
    """<p>A list of successfully created billing adjustment items, each containing the <code>billingAdjustmentRequestId</code> and <code>clientToken</code>.</p>"""
    errors: "capo_marketplace_agreement.types.batch_create_billing_adjustment_error_list.BatchCreateBillingAdjustmentErrorList"
    """<p>A list of errors for entries that failed validation, each containing the <code>clientToken</code>, error <code>code</code>, and <code>message</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestOutput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_item_list

    out["items"] = (
        capo_marketplace_agreement.types.batch_create_billing_adjustment_item_list.serialize_aws_json_1_0(
            value["items"]
        )
    )
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_error_list

    out["errors"] = (
        capo_marketplace_agreement.types.batch_create_billing_adjustment_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentRequestOutput:
    out: BatchCreateBillingAdjustmentRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_marketplace_agreement.types.batch_create_billing_adjustment_item_list

        out["items"] = (
            capo_marketplace_agreement.types.batch_create_billing_adjustment_item_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("errors") is not None:
        import capo_marketplace_agreement.types.batch_create_billing_adjustment_error_list

        out["errors"] = (
            capo_marketplace_agreement.types.batch_create_billing_adjustment_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out
