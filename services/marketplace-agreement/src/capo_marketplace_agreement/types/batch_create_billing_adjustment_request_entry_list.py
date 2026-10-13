"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestEntryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

BatchCreateBillingAdjustmentRequestEntryList: TypeAlias = list[
    "capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.BatchCreateBillingAdjustmentRequestEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestEntryList) -> list:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillingAdjustmentRequestEntryList:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

    out: BatchCreateBillingAdjustmentRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: BatchCreateBillingAdjustmentRequestEntryList) -> list[Any]:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

    return [
        capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.redact_sensitive(
            item
        )
        for item in value
    ]
