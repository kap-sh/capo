"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list


class BatchCreateBillingAdjustmentRequestInput(TypedDict, closed=True):
    billing_adjustment_request_entries: "capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.BatchCreateBillingAdjustmentRequestEntryList"
    """<p>A list of billing adjustment request entries. Each entry specifies the invoice and adjustment details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestInput) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list

    out["billingAdjustmentRequestEntries"] = (
        capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.serialize_aws_json_1_0(
            value["billing_adjustment_request_entries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentRequestInput:
    out: BatchCreateBillingAdjustmentRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("billingAdjustmentRequestEntries") is not None:
        import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list

        out["billing_adjustment_request_entries"] = (
            capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.deserialize_aws_json_1_0(
                data["billingAdjustmentRequestEntries"]
            )
        )
    else:
        out["billing_adjustment_request_entries"] = []
    return out


def redact_sensitive(value: BatchCreateBillingAdjustmentRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "billing_adjustment_request_entries" in value:
        import capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list

        out["billing_adjustment_request_entries"] = (
            capo_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.redact_sensitive(
                value["billing_adjustment_request_entries"]
            )
        )
    return out
