"""Generated from Smithy shape ``com.amazonaws.invoicing#BillingPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.month
    import capo_invoicing.types.year


class BillingPeriod(TypedDict, closed=True):
    month: "capo_invoicing.types.month.Month"
    """<p> The billing period month. </p>"""
    year: "capo_invoicing.types.year.Year"
    """<p> The billing period year. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPeriod) -> dict:
    out: dict = {}
    out["Month"] = value["month"]
    out["Year"] = value["year"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingPeriod:
    out: BillingPeriod = {}  # type: ignore[typeddict-item]
    if data.get("Month") is not None:
        out["month"] = data["Month"]
    else:
        out["month"] = 0
    if data.get("Year") is not None:
        out["year"] = data["Year"]
    else:
        out["year"] = 0
    return out
