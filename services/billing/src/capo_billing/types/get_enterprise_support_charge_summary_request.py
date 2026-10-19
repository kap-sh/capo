"""Generated from Smithy shape ``com.amazonaws.billing#GetEnterpriseSupportChargeSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.enterprise_support_billing_month


class GetEnterpriseSupportChargeSummaryRequest(TypedDict, closed=True):
    billing_month: "capo_billing.types.enterprise_support_billing_month.EnterpriseSupportBillingMonth"
    """<p>The billing month in YYYY-MM format. This must be a month in the past.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnterpriseSupportChargeSummaryRequest) -> dict:
    out: dict = {}
    out["billingMonth"] = value["billing_month"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnterpriseSupportChargeSummaryRequest:
    out: GetEnterpriseSupportChargeSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("billingMonth") is not None:
        out["billing_month"] = data["billingMonth"]
    else:
        out["billing_month"] = ""
    return out
