"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportAccountCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.business_support_discount
    import capo_billing.types.business_support_service_spend_list
    import capo_billing.types.business_support_tier_charge_list


class BusinessSupportAccountCharge(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The linked account ID.</p>"""
    support_plan_name: "str"
    """<p>The Support plan name for this account. Valid values: <code>AWSSupportBusiness</code> (Business Support plan), <code>AWSSupportDeveloper</code> (Developer Support plan), <code>AWSSupportEssential</code> (Basic Support plan).</p>"""
    total_charge: "str"
    """<p>The total Business Support charge amount for this account in the billing month.</p>"""
    total_usage_basis: "str"
    """<p>The total Support-eligible spend used as the basis for calculating the Business Support charge for this account.</p>"""
    tier_charges: NotRequired[
        "capo_billing.types.business_support_tier_charge_list.BusinessSupportTierChargeList"
    ]
    """<p>The tier-level charges that make up the total Business Support charge for this account. Each tier represents a spend range with its own rate.</p>"""
    support_discount: NotRequired[
        "capo_billing.types.business_support_discount.BusinessSupportDiscount"
    ]
    """<p>The discount applied to the Business Support charge for this account, if any. This field is absent when no discount applies.</p>"""
    support_eligible_spend_by_service: NotRequired[
        "capo_billing.types.business_support_service_spend_list.BusinessSupportServiceSpendList"
    ]
    """<p>The Support-eligible spend broken down by contributing service for this account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportAccountCharge) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["supportPlanName"] = value["support_plan_name"]
    out["totalCharge"] = value["total_charge"]
    out["totalUsageBasis"] = value["total_usage_basis"]
    if "tier_charges" in value:
        import capo_billing.types.business_support_tier_charge_list

        out["tierCharges"] = (
            capo_billing.types.business_support_tier_charge_list.serialize_aws_json_1_0(
                value["tier_charges"]
            )
        )
    if "support_discount" in value:
        import capo_billing.types.business_support_discount

        out["supportDiscount"] = (
            capo_billing.types.business_support_discount.serialize_aws_json_1_0(
                value["support_discount"]
            )
        )
    if "support_eligible_spend_by_service" in value:
        import capo_billing.types.business_support_service_spend_list

        out["supportEligibleSpendByService"] = (
            capo_billing.types.business_support_service_spend_list.serialize_aws_json_1_0(
                value["support_eligible_spend_by_service"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BusinessSupportAccountCharge:
    out: BusinessSupportAccountCharge = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("BusinessSupportAccountCharge.account_id required")
    if data.get("supportPlanName") is not None:
        out["support_plan_name"] = data["supportPlanName"]
    else:
        raise DeserializationError(
            "BusinessSupportAccountCharge.support_plan_name required"
        )
    if data.get("totalCharge") is not None:
        out["total_charge"] = data["totalCharge"]
    else:
        raise DeserializationError("BusinessSupportAccountCharge.total_charge required")
    if data.get("totalUsageBasis") is not None:
        out["total_usage_basis"] = data["totalUsageBasis"]
    else:
        raise DeserializationError(
            "BusinessSupportAccountCharge.total_usage_basis required"
        )
    if data.get("tierCharges") is not None:
        import capo_billing.types.business_support_tier_charge_list

        out["tier_charges"] = (
            capo_billing.types.business_support_tier_charge_list.deserialize_aws_json_1_0(
                data["tierCharges"]
            )
        )
    if data.get("supportDiscount") is not None:
        import capo_billing.types.business_support_discount

        out["support_discount"] = (
            capo_billing.types.business_support_discount.deserialize_aws_json_1_0(
                data["supportDiscount"]
            )
        )
    if data.get("supportEligibleSpendByService") is not None:
        import capo_billing.types.business_support_service_spend_list

        out["support_eligible_spend_by_service"] = (
            capo_billing.types.business_support_service_spend_list.deserialize_aws_json_1_0(
                data["supportEligibleSpendByService"]
            )
        )
    return out
