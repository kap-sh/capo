"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingPeriodRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_period


class BillingPeriodRange(TypedDict, closed=True):
    inclusive_start_billing_period: (
        "capo_billingconductor.types.billing_period.BillingPeriod"
    )
    """<p>The inclusive start billing period that defines a billing period range for the margin summary.</p>"""
    exclusive_end_billing_period: (
        "capo_billingconductor.types.billing_period.BillingPeriod"
    )
    """<p>The exclusive end billing period that defines a billing period range for the margin summary. For example, if you choose a billing period that starts in October 2023 and ends in December 2023, the margin summary will only include data from October 2023 and November 2023.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingPeriodRange) -> dict:
    out: dict = {}
    out["InclusiveStartBillingPeriod"] = value["inclusive_start_billing_period"]
    out["ExclusiveEndBillingPeriod"] = value["exclusive_end_billing_period"]
    return out


def deserialize_json(data: dict) -> BillingPeriodRange:
    out: BillingPeriodRange = {}  # type: ignore[typeddict-item]
    if data.get("InclusiveStartBillingPeriod") is not None:
        out["inclusive_start_billing_period"] = data["InclusiveStartBillingPeriod"]
    else:
        out["inclusive_start_billing_period"] = ""
    if data.get("ExclusiveEndBillingPeriod") is not None:
        out["exclusive_end_billing_period"] = data["ExclusiveEndBillingPeriod"]
    else:
        out["exclusive_end_billing_period"] = ""
    return out
