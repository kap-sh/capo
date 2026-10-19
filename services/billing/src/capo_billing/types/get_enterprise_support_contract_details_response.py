"""Generated from Smithy shape ``com.amazonaws.billing#GetEnterpriseSupportContractDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.additional_charge_list
    import capo_billing.types.charge_account_list
    import capo_billing.types.contract_account_list
    import capo_billing.types.pricing_plan_list


class GetEnterpriseSupportContractDetailsResponse(TypedDict, closed=True):
    is_contract_active: NotRequired["bool"]
    """<p>When true, the Enterprise Support contract is active. When false, the Enterprise Support Contract is inactive.</p>"""
    support_allocation_method: "str"
    """<p>The method used to distribute the total Support charge amount across each account in the Support profile. Valid values: Proportional, Fixed_Percentage. Proportional means support charges are distributed to each account in proportion to its eligible Spend. Fixed_Percentage means support charges are distributed across accounts according to pre-configured percentages from the contract.</p>"""
    support_reserved_instance_amortization_start_date: NotRequired["datetime.datetime"]
    """<p>When supportReservedInstanceTreatmentMethod = AmortizedCustom, only amortized fees for Reserved Instances purchased on or after this date are included in the calculation. This field is Null for all other treatment methods.</p>"""
    support_reserved_instance_treatment_method: NotRequired["str"]
    """<p>The method used to include Reserved Instance (RI) fees in the Enterprise Support charge calculation. Valid values: None (RI fees excluded from Support-eligible spend), Upfront (full upfront RI fees included in month of purchase), Amortized (RI fees spread over commitment term for RIs purchased on or after Support subscription start date), AmortizedCustom (same as Amortized but only for RIs purchased on or after a specified custom start date), AmortizedAll (RI fees amortized for all active RIs including those purchased before Support subscription started).</p>"""
    support_savings_plans_amortization_start_date: NotRequired["datetime.datetime"]
    """<p>This is applicable when supportSavingsPlansTreatmentMethod = Amortized and is Null for all other methods. It shows the start date from which Savings Plan fees are included in Support Eligible Spend.</p>"""
    support_savings_plans_treatment_method: NotRequired["str"]
    """<p>The method used to include Savings Plans fees in Enterprise Support charge calculations. Valid values: None (Savings Plan fees excluded from Support-eligible spend), Upfront (full upfront Savings Plan fees included in month of purchase), Amortized (Savings Plan fees spread over commitment term for Savings Plans purchased on or after Support subscription start date), AmortizedCustom (same as Amortized but only for Savings Plans purchased on or after a specified custom start date), AmortizedAll (Savings Plan fees amortized for all active Savings Plans including those purchased before Support subscription started).</p>"""
    support_prorate_start_date: NotRequired["datetime.datetime"]
    """<p>The start date for accounts subscribed or unsubscribed to Support billing during the billing month.</p>"""
    contract_payer_account_ids: (
        "capo_billing.types.contract_account_list.ContractAccountList"
    )
    """<p>The list of accounts covered by the Enterprise Support contract.</p>"""
    charged_payer_account_ids: (
        "capo_billing.types.charge_account_list.ChargeAccountList"
    )
    """<p>The list of payer accounts and their charge allocation percentages.</p>"""
    additional_support_charge: NotRequired[
        "capo_billing.types.additional_charge_list.AdditionalChargeList"
    ]
    """<p>Any Additional support charges applied to the contract.</p>"""
    additional_support_eligible_usage_spend: NotRequired[
        "capo_billing.types.additional_charge_list.AdditionalChargeList"
    ]
    """<p>Any Additional support-eligible usage spend charges.</p>"""
    pricing_plans: "capo_billing.types.pricing_plan_list.PricingPlanList"
    """<p>The pricing plans associated with this Enterprise Support contract.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEnterpriseSupportContractDetailsResponse) -> dict:
    out: dict = {}
    if "is_contract_active" in value:
        out["isContractActive"] = value["is_contract_active"]
    out["supportAllocationMethod"] = value["support_allocation_method"]
    if "support_reserved_instance_amortization_start_date" in value:
        import capo_billing.types._prelude.timestamp

        out["supportReservedInstanceAmortizationStartDate"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["support_reserved_instance_amortization_start_date"]
            )
        )
    if "support_reserved_instance_treatment_method" in value:
        out["supportReservedInstanceTreatmentMethod"] = value[
            "support_reserved_instance_treatment_method"
        ]
    if "support_savings_plans_amortization_start_date" in value:
        import capo_billing.types._prelude.timestamp

        out["supportSavingsPlansAmortizationStartDate"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["support_savings_plans_amortization_start_date"]
            )
        )
    if "support_savings_plans_treatment_method" in value:
        out["supportSavingsPlansTreatmentMethod"] = value[
            "support_savings_plans_treatment_method"
        ]
    if "support_prorate_start_date" in value:
        import capo_billing.types._prelude.timestamp

        out["supportProrateStartDate"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["support_prorate_start_date"]
            )
        )
    import capo_billing.types.contract_account_list

    out["contractPayerAccountIds"] = (
        capo_billing.types.contract_account_list.serialize_aws_json_1_0(
            value["contract_payer_account_ids"]
        )
    )
    import capo_billing.types.charge_account_list

    out["chargedPayerAccountIds"] = (
        capo_billing.types.charge_account_list.serialize_aws_json_1_0(
            value["charged_payer_account_ids"]
        )
    )
    if "additional_support_charge" in value:
        import capo_billing.types.additional_charge_list

        out["additionalSupportCharge"] = (
            capo_billing.types.additional_charge_list.serialize_aws_json_1_0(
                value["additional_support_charge"]
            )
        )
    if "additional_support_eligible_usage_spend" in value:
        import capo_billing.types.additional_charge_list

        out["additionalSupportEligibleUsageSpend"] = (
            capo_billing.types.additional_charge_list.serialize_aws_json_1_0(
                value["additional_support_eligible_usage_spend"]
            )
        )
    import capo_billing.types.pricing_plan_list

    out["pricingPlans"] = capo_billing.types.pricing_plan_list.serialize_aws_json_1_0(
        value["pricing_plans"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEnterpriseSupportContractDetailsResponse:
    out: GetEnterpriseSupportContractDetailsResponse = {}  # type: ignore[typeddict-item]
    if data.get("isContractActive") is not None:
        out["is_contract_active"] = data["isContractActive"]
    if data.get("supportAllocationMethod") is not None:
        out["support_allocation_method"] = data["supportAllocationMethod"]
    else:
        out["support_allocation_method"] = ""
    if data.get("supportReservedInstanceAmortizationStartDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["support_reserved_instance_amortization_start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["supportReservedInstanceAmortizationStartDate"]
            )
        )
    if data.get("supportReservedInstanceTreatmentMethod") is not None:
        out["support_reserved_instance_treatment_method"] = data[
            "supportReservedInstanceTreatmentMethod"
        ]
    if data.get("supportSavingsPlansAmortizationStartDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["support_savings_plans_amortization_start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["supportSavingsPlansAmortizationStartDate"]
            )
        )
    if data.get("supportSavingsPlansTreatmentMethod") is not None:
        out["support_savings_plans_treatment_method"] = data[
            "supportSavingsPlansTreatmentMethod"
        ]
    if data.get("supportProrateStartDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["support_prorate_start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["supportProrateStartDate"]
            )
        )
    if data.get("contractPayerAccountIds") is not None:
        import capo_billing.types.contract_account_list

        out["contract_payer_account_ids"] = (
            capo_billing.types.contract_account_list.deserialize_aws_json_1_0(
                data["contractPayerAccountIds"]
            )
        )
    else:
        out["contract_payer_account_ids"] = []
    if data.get("chargedPayerAccountIds") is not None:
        import capo_billing.types.charge_account_list

        out["charged_payer_account_ids"] = (
            capo_billing.types.charge_account_list.deserialize_aws_json_1_0(
                data["chargedPayerAccountIds"]
            )
        )
    else:
        out["charged_payer_account_ids"] = []
    if data.get("additionalSupportCharge") is not None:
        import capo_billing.types.additional_charge_list

        out["additional_support_charge"] = (
            capo_billing.types.additional_charge_list.deserialize_aws_json_1_0(
                data["additionalSupportCharge"]
            )
        )
    if data.get("additionalSupportEligibleUsageSpend") is not None:
        import capo_billing.types.additional_charge_list

        out["additional_support_eligible_usage_spend"] = (
            capo_billing.types.additional_charge_list.deserialize_aws_json_1_0(
                data["additionalSupportEligibleUsageSpend"]
            )
        )
    if data.get("pricingPlans") is not None:
        import capo_billing.types.pricing_plan_list

        out["pricing_plans"] = (
            capo_billing.types.pricing_plan_list.deserialize_aws_json_1_0(
                data["pricingPlans"]
            )
        )
    else:
        out["pricing_plans"] = []
    return out
