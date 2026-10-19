"""Generated from Smithy shape ``com.amazonaws.billingconductor#GetBillingGroupCostReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.billing_group_arn
    import capo_billingconductor.types.billing_period_range
    import capo_billingconductor.types.group_by_attributes_list
    import capo_billingconductor.types.max_billing_group_cost_report_results
    import capo_billingconductor.types.token


class GetBillingGroupCostReportInput(TypedDict, closed=True):
    arn: "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    """<p>The Amazon Resource Number (ARN) that uniquely identifies the billing group.</p>"""
    billing_period_range: NotRequired[
        "capo_billingconductor.types.billing_period_range.BillingPeriodRange"
    ]
    """<p>A time range for which the margin summary is effective. You can specify up to 12 months.</p>"""
    group_by: NotRequired[
        "capo_billingconductor.types.group_by_attributes_list.GroupByAttributesList"
    ]
    """<p>A list of strings that specify the attributes that are used to break down costs in the margin summary reports for the billing group. For example, you can view your costs by the Amazon Web Services service name or the billing period.</p>"""
    max_results: NotRequired[
        "capo_billingconductor.types.max_billing_group_cost_report_results.MaxBillingGroupCostReportResults"
    ]
    """<p>The maximum number of margin summary reports to retrieve.</p>"""
    next_token: NotRequired["capo_billingconductor.types.token.Token"]
    """<p>The pagination token used on subsequent calls to get reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBillingGroupCostReportInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "billing_period_range" in value:
        import capo_billingconductor.types.billing_period_range

        out["BillingPeriodRange"] = (
            capo_billingconductor.types.billing_period_range.serialize_json(
                value["billing_period_range"]
            )
        )
    if "group_by" in value:
        import capo_billingconductor.types.group_by_attributes_list

        out["GroupBy"] = (
            capo_billingconductor.types.group_by_attributes_list.serialize_json(
                value["group_by"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetBillingGroupCostReportInput:
    out: GetBillingGroupCostReportInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("BillingPeriodRange") is not None:
        import capo_billingconductor.types.billing_period_range

        out["billing_period_range"] = (
            capo_billingconductor.types.billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    if data.get("GroupBy") is not None:
        import capo_billingconductor.types.group_by_attributes_list

        out["group_by"] = (
            capo_billingconductor.types.group_by_attributes_list.deserialize_json(
                data["GroupBy"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
