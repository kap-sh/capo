"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#InvoiceBillingPeriod``."""

from typing_extensions import TypedDict


class InvoiceBillingPeriod(TypedDict, closed=True):
    month: "int"
    """<p>The billing period month. Valid range: 1-12.</p>"""
    year: "int"
    """<p>The billing period year.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceBillingPeriod) -> dict:
    out: dict = {}
    out["month"] = value["month"]
    out["year"] = value["year"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceBillingPeriod:
    out: InvoiceBillingPeriod = {}  # type: ignore[typeddict-item]
    if data.get("month") is not None:
        out["month"] = data["month"]
    else:
        out["month"] = 0
    if data.get("year") is not None:
        out["year"] = data["year"]
    else:
        out["year"] = 0
    return out
