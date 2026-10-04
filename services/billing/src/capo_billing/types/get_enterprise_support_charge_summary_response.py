"""Generated from Smithy shape ``com.amazonaws.billing#GetEnterpriseSupportChargeSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.account_id
    import capo_billing.types.enterprise_support_billing_month
    import capo_billing.types.pricing_plan


class GetEnterpriseSupportChargeSummaryResponse(TypedDict, closed=True):
    payer_account_id: "capo_billing.types.account_id.AccountId"
    """<p>The payer account ID that is authorized to view Enterprise Support data for all accounts in its Support profile.</p>"""
    billing_month: "capo_billing.types.enterprise_support_billing_month.EnterpriseSupportBillingMonth"
    """<p>The billing month in YYYY-MM format. This must be a month in the past.</p>"""
    billing_period_start_date: "datetime.datetime"
    """<p>The start date of the billing period.</p>"""
    billing_period_end_date: "datetime.datetime"
    """<p>The end date of the billing period.</p>"""
    is_estimated: "bool"
    """<p>Specifies whether the Support charge amount is estimated. When false, the charge amount is finalized.</p>"""
    bill_date: "datetime.datetime"
    """<p>The date the bill was generated.</p>"""
    support_charge: "str"
    """<p>The Support charge amount for the account.</p>"""
    total_support_charge: "str"
    """<p>The total Support charge amount for all accounts in the Support profile.</p>"""
    support_discount: "str"
    """<p>The support discount amount.</p>"""
    total_support_eligible_spend: "str"
    """<p>The total Support-eligible Spend from all accounts in the Support profile. This includes eligible spend from usage of Amazon Web Services, Reserved Instances, and Savings Plans.</p>"""
    total_support_eligible_usage_spend: "str"
    """<p>The total Support-eligible spend from usage of Amazon Web Services from all accounts in the Support profile.</p>"""
    total_support_eligible_reserved_instance_spend: "str"
    """<p>The total Support-eligible Reserved Instance spend from all accounts in the Support profile.</p>"""
    total_support_eligible_savings_plan_spend: "str"
    """<p>The total Support-eligible Savings Plan spend from all accounts in the Support profile.</p>"""
    support_charge_percentage: "str"
    """<p>The percentage applied to the total Support-eligible spend to calculate the total Support charge across all accounts in the Support profile.</p>"""
    support_effective_pricing_plan: "capo_billing.types.pricing_plan.PricingPlan"
    """<p>The effective pricing plan used for the support charge calculation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnterpriseSupportChargeSummaryResponse) -> dict:
    out: dict = {}
    out["payerAccountId"] = value["payer_account_id"]
    out["billingMonth"] = value["billing_month"]
    import capo_billing.types._prelude.timestamp

    out["billingPeriodStartDate"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["billing_period_start_date"]
        )
    )
    import capo_billing.types._prelude.timestamp

    out["billingPeriodEndDate"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["billing_period_end_date"]
        )
    )
    out["isEstimated"] = value["is_estimated"]
    import capo_billing.types._prelude.timestamp

    out["billDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["bill_date"]
    )
    out["supportCharge"] = value["support_charge"]
    out["totalSupportCharge"] = value["total_support_charge"]
    out["supportDiscount"] = value["support_discount"]
    out["totalSupportEligibleSpend"] = value["total_support_eligible_spend"]
    out["totalSupportEligibleUsageSpend"] = value["total_support_eligible_usage_spend"]
    out["totalSupportEligibleReservedInstanceSpend"] = value[
        "total_support_eligible_reserved_instance_spend"
    ]
    out["totalSupportEligibleSavingsPlanSpend"] = value[
        "total_support_eligible_savings_plan_spend"
    ]
    out["supportChargePercentage"] = value["support_charge_percentage"]
    import capo_billing.types.pricing_plan

    out["supportEffectivePricingPlan"] = (
        capo_billing.types.pricing_plan.serialize_aws_json_1_0(
            value["support_effective_pricing_plan"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnterpriseSupportChargeSummaryResponse:
    out: GetEnterpriseSupportChargeSummaryResponse = {}  # type: ignore[typeddict-item]
    if data.get("payerAccountId") is not None:
        out["payer_account_id"] = data["payerAccountId"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.payer_account_id required"
        )
    if data.get("billingMonth") is not None:
        out["billing_month"] = data["billingMonth"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.billing_month required"
        )
    if data.get("billingPeriodStartDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["billing_period_start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["billingPeriodStartDate"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.billing_period_start_date required"
        )
    if data.get("billingPeriodEndDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["billing_period_end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["billingPeriodEndDate"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.billing_period_end_date required"
        )
    if data.get("isEstimated") is not None:
        out["is_estimated"] = data["isEstimated"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.is_estimated required"
        )
    if data.get("billDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["bill_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["billDate"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.bill_date required"
        )
    if data.get("supportCharge") is not None:
        out["support_charge"] = data["supportCharge"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.support_charge required"
        )
    if data.get("totalSupportCharge") is not None:
        out["total_support_charge"] = data["totalSupportCharge"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.total_support_charge required"
        )
    if data.get("supportDiscount") is not None:
        out["support_discount"] = data["supportDiscount"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.support_discount required"
        )
    if data.get("totalSupportEligibleSpend") is not None:
        out["total_support_eligible_spend"] = data["totalSupportEligibleSpend"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.total_support_eligible_spend required"
        )
    if data.get("totalSupportEligibleUsageSpend") is not None:
        out["total_support_eligible_usage_spend"] = data[
            "totalSupportEligibleUsageSpend"
        ]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.total_support_eligible_usage_spend required"
        )
    if data.get("totalSupportEligibleReservedInstanceSpend") is not None:
        out["total_support_eligible_reserved_instance_spend"] = data[
            "totalSupportEligibleReservedInstanceSpend"
        ]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.total_support_eligible_reserved_instance_spend required"
        )
    if data.get("totalSupportEligibleSavingsPlanSpend") is not None:
        out["total_support_eligible_savings_plan_spend"] = data[
            "totalSupportEligibleSavingsPlanSpend"
        ]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.total_support_eligible_savings_plan_spend required"
        )
    if data.get("supportChargePercentage") is not None:
        out["support_charge_percentage"] = data["supportChargePercentage"]
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.support_charge_percentage required"
        )
    if data.get("supportEffectivePricingPlan") is not None:
        import capo_billing.types.pricing_plan

        out["support_effective_pricing_plan"] = (
            capo_billing.types.pricing_plan.deserialize_aws_json_1_0(
                data["supportEffectivePricingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "GetEnterpriseSupportChargeSummaryResponse.support_effective_pricing_plan required"
        )
    return out
