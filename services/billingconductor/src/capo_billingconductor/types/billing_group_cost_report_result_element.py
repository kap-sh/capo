"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupCostReportResultElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.attributes_list
    import capo_billingconductor.types.aws_cost
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.currency
    import capo_billingconductor.types.margin
    import capo_billingconductor.types.margin_percentage
    import capo_billingconductor.types.proforma_cost


class BillingGroupCostReportResultElement(TypedDict, closed=True):
    arn: NotRequired["capo_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Number (ARN) that uniquely identifies the billing group.</p>"""
    aws_cost: NotRequired["capo_billingconductor.types.aws_cost.AWSCost"]
    """<p>The actual Amazon Web Services charges for the billing group.</p>"""
    proforma_cost: NotRequired["capo_billingconductor.types.proforma_cost.ProformaCost"]
    """<p>The hypothetical Amazon Web Services charges based on the associated pricing plan of a billing group.</p>"""
    margin: NotRequired["capo_billingconductor.types.margin.Margin"]
    """<p>The billing group margin.</p>"""
    margin_percentage: NotRequired[
        "capo_billingconductor.types.margin_percentage.MarginPercentage"
    ]
    """<p>The percentage of the billing group margin.</p>"""
    currency: NotRequired["capo_billingconductor.types.currency.Currency"]
    """<p>The displayed currency.</p>"""
    attributes: NotRequired[
        "capo_billingconductor.types.attributes_list.AttributesList"
    ]
    """<p>The list of key-value pairs that represent the attributes by which the <code>BillingGroupCostReportResults</code> are grouped. For example, if you want the Amazon S3 service-level breakdown of a billing group for November 2023, the attributes list will contain a key-value pair of <code>"PRODUCT_NAME"</code> and <code>"S3"</code> and a key-value pair of <code>"BILLING_PERIOD"</code> and <code>"Nov 2023"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupCostReportResultElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "aws_cost" in value:
        out["AWSCost"] = value["aws_cost"]
    if "proforma_cost" in value:
        out["ProformaCost"] = value["proforma_cost"]
    if "margin" in value:
        out["Margin"] = value["margin"]
    if "margin_percentage" in value:
        out["MarginPercentage"] = value["margin_percentage"]
    if "currency" in value:
        out["Currency"] = value["currency"]
    if "attributes" in value:
        import capo_billingconductor.types.attributes_list

        out["Attributes"] = capo_billingconductor.types.attributes_list.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> BillingGroupCostReportResultElement:
    out: BillingGroupCostReportResultElement = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AWSCost") is not None:
        out["aws_cost"] = data["AWSCost"]
    if data.get("ProformaCost") is not None:
        out["proforma_cost"] = data["ProformaCost"]
    if data.get("Margin") is not None:
        out["margin"] = data["Margin"]
    if data.get("MarginPercentage") is not None:
        out["margin_percentage"] = data["MarginPercentage"]
    if data.get("Currency") is not None:
        out["currency"] = data["Currency"]
    if data.get("Attributes") is not None:
        import capo_billingconductor.types.attributes_list

        out["attributes"] = (
            capo_billingconductor.types.attributes_list.deserialize_json(
                data["Attributes"]
            )
        )
    return out
