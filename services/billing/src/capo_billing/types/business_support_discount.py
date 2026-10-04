"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportDiscount``."""

from typing_extensions import NotRequired, TypedDict


class BusinessSupportDiscount(TypedDict, closed=True):
    discount_amount: NotRequired["str"]
    """<p>The discount amount applied to the Business Support charge. This value is negative, representing a reduction in the charge.</p>"""
    discount_percentage: NotRequired["str"]
    """<p>The discount percentage applied to the Business Support charge, expressed as a decimal (for example, <code>0.12</code> for a 12% discount).</p>"""
    discount_type: NotRequired["str"]
    """<p>The type of discount applied. Valid values: <code>Distributor_Discount</code> (a discount applied through a distributor arrangement), <code>SPP_Discount</code> (a discount applied through the Solution Provider Program).</p>"""
    discount_source: NotRequired["str"]
    """<p>The source or program through which the discount was applied.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportDiscount) -> dict:
    out: dict = {}
    if "discount_amount" in value:
        out["discountAmount"] = value["discount_amount"]
    if "discount_percentage" in value:
        out["discountPercentage"] = value["discount_percentage"]
    if "discount_type" in value:
        out["discountType"] = value["discount_type"]
    if "discount_source" in value:
        out["discountSource"] = value["discount_source"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessSupportDiscount:
    out: BusinessSupportDiscount = {}  # type: ignore[typeddict-item]
    if data.get("discountAmount") is not None:
        out["discount_amount"] = data["discountAmount"]
    if data.get("discountPercentage") is not None:
        out["discount_percentage"] = data["discountPercentage"]
    if data.get("discountType") is not None:
        out["discount_type"] = data["discountType"]
    if data.get("discountSource") is not None:
        out["discount_source"] = data["discountSource"]
    return out
