"""Generated from Smithy shape ``com.amazonaws.billing#ListBusinessSupportAccountChargesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.business_support_account_charge_list
    import capo_billing.types.business_support_billing_month
    import capo_billing.types.page_token


class ListBusinessSupportAccountChargesResponse(TypedDict, closed=True):
    billing_month: (
        "capo_billing.types.business_support_billing_month.BusinessSupportBillingMonth"
    )
    """<p>The billing month for the returned charges, in YYYY-MM format.</p>"""
    is_estimated: "bool"
    """<p>Specifies whether the Support charge amount is estimated. When false, the charge amount is finalized.</p>"""
    total_support_charge: "str"
    """<p>The total Business Support charge amount for all accounts in the billing month.</p>"""
    total_support_eligible_spend: "str"
    """<p>The total Support-eligible spend from all accounts in the billing month. This includes eligible spend from usage of Amazon Web Services.</p>"""
    account_count: "int"
    """<p>The total number of linked accounts with Business Support charges in the billing month.</p>"""
    account_charges: "capo_billing.types.business_support_account_charge_list.BusinessSupportAccountChargeList"
    """<p>The list of Business Support charges per linked account.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token for the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBusinessSupportAccountChargesResponse) -> dict:
    out: dict = {}
    out["billingMonth"] = value["billing_month"]
    out["isEstimated"] = value["is_estimated"]
    out["totalSupportCharge"] = value["total_support_charge"]
    out["totalSupportEligibleSpend"] = value["total_support_eligible_spend"]
    out["accountCount"] = value["account_count"]
    import capo_billing.types.business_support_account_charge_list

    out["accountCharges"] = (
        capo_billing.types.business_support_account_charge_list.serialize_aws_json_1_0(
            value["account_charges"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBusinessSupportAccountChargesResponse:
    out: ListBusinessSupportAccountChargesResponse = {}  # type: ignore[typeddict-item]
    if data.get("billingMonth") is not None:
        out["billing_month"] = data["billingMonth"]
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesResponse.billing_month required"
        )
    if data.get("isEstimated") is not None:
        out["is_estimated"] = data["isEstimated"]
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesResponse.is_estimated required"
        )
    if data.get("totalSupportCharge") is not None:
        out["total_support_charge"] = data["totalSupportCharge"]
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesResponse.total_support_charge required"
        )
    if data.get("totalSupportEligibleSpend") is not None:
        out["total_support_eligible_spend"] = data["totalSupportEligibleSpend"]
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesResponse.total_support_eligible_spend required"
        )
    if data.get("accountCount") is not None:
        out["account_count"] = data["accountCount"]
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesResponse.account_count required"
        )
    if data.get("accountCharges") is not None:
        import capo_billing.types.business_support_account_charge_list

        out["account_charges"] = (
            capo_billing.types.business_support_account_charge_list.deserialize_aws_json_1_0(
                data["accountCharges"]
            )
        )
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesResponse.account_charges required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
