"""Generated from Smithy shape ``com.amazonaws.billing#BillingPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_year
    import capo_billing.types.month


class BillingPeriod(TypedDict, closed=True):
    year: "capo_billing.types.billing_year.BillingYear"
    """<p>The four-digit year of the billing period.</p>"""
    month: "capo_billing.types.month.Month"
    """<p>The month of the billing period as an integer between 1 and 12.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPeriod) -> dict:
    out: dict = {}
    out["year"] = value["year"]
    out["month"] = value["month"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingPeriod:
    out: BillingPeriod = {}  # type: ignore[typeddict-item]
    if data.get("year") is not None:
        out["year"] = data["year"]
    else:
        out["year"] = 0
    if data.get("month") is not None:
        out["month"] = data["month"]
    else:
        out["month"] = 0
    return out
