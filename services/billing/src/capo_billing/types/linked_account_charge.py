"""Generated from Smithy shape ``com.amazonaws.billing#LinkedAccountCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.service_level_account_usage_list
    import capo_billing.types.time_period_list


class LinkedAccountCharge(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The linked account ID.</p>"""
    payer_account_id: "capo_billing.types.account_id.AccountId"
    """<p>The payer account ID that is authorized to view Enterprise Support data for all accounts in its Support profile.</p>"""
    account_type: NotRequired["str"]
    """<p>The type of account.</p>"""
    billable_seconds: "int"
    """<p>The number of billable seconds in the billing period based on when the account was subscribed to Enterprise Support.</p>"""
    total_seconds: "int"
    """<p>The total number of seconds in the billing period.</p>"""
    total_support_eligible_spend: "str"
    """<p>The total support-eligible spend for this account.</p>"""
    prorated_total_support_eligible_spend: "str"
    """<p>The prorated total support-eligible spend based on when the account was subscribed to Enterprise Support.</p>"""
    linked_time_periods: NotRequired[
        "capo_billing.types.time_period_list.TimePeriodList"
    ]
    """<p>The time periods during which this account was linked.</p>"""
    subscription_time_periods: NotRequired[
        "capo_billing.types.time_period_list.TimePeriodList"
    ]
    """<p>The subscription time periods for this account.</p>"""
    total_support_eligible_reserved_instance_spend: NotRequired["str"]
    """<p>The total support-eligible Reserved Instance spend for this account.</p>"""
    total_support_eligible_savings_plan_spend: NotRequired["str"]
    """<p>The total support-eligible Savings Plan spend for this account.</p>"""
    support_eligible_spend_by_service: NotRequired[
        "capo_billing.types.service_level_account_usage_list.ServiceLevelAccountUsageList"
    ]
    """<p>The support-eligible spend broken down by service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LinkedAccountCharge) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["payerAccountId"] = value["payer_account_id"]
    if "account_type" in value:
        out["accountType"] = value["account_type"]
    out["billableSeconds"] = value["billable_seconds"]
    out["totalSeconds"] = value["total_seconds"]
    out["totalSupportEligibleSpend"] = value["total_support_eligible_spend"]
    out["proratedTotalSupportEligibleSpend"] = value[
        "prorated_total_support_eligible_spend"
    ]
    if "linked_time_periods" in value:
        import capo_billing.types.time_period_list

        out["linkedTimePeriods"] = (
            capo_billing.types.time_period_list.serialize_aws_json_1_0(
                value["linked_time_periods"]
            )
        )
    if "subscription_time_periods" in value:
        import capo_billing.types.time_period_list

        out["subscriptionTimePeriods"] = (
            capo_billing.types.time_period_list.serialize_aws_json_1_0(
                value["subscription_time_periods"]
            )
        )
    if "total_support_eligible_reserved_instance_spend" in value:
        out["totalSupportEligibleReservedInstanceSpend"] = value[
            "total_support_eligible_reserved_instance_spend"
        ]
    if "total_support_eligible_savings_plan_spend" in value:
        out["totalSupportEligibleSavingsPlanSpend"] = value[
            "total_support_eligible_savings_plan_spend"
        ]
    if "support_eligible_spend_by_service" in value:
        import capo_billing.types.service_level_account_usage_list

        out["supportEligibleSpendByService"] = (
            capo_billing.types.service_level_account_usage_list.serialize_aws_json_1_0(
                value["support_eligible_spend_by_service"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LinkedAccountCharge:
    out: LinkedAccountCharge = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("payerAccountId") is not None:
        out["payer_account_id"] = data["payerAccountId"]
    else:
        out["payer_account_id"] = ""
    if data.get("accountType") is not None:
        out["account_type"] = data["accountType"]
    if data.get("billableSeconds") is not None:
        out["billable_seconds"] = data["billableSeconds"]
    else:
        out["billable_seconds"] = 0
    if data.get("totalSeconds") is not None:
        out["total_seconds"] = data["totalSeconds"]
    else:
        out["total_seconds"] = 0
    if data.get("totalSupportEligibleSpend") is not None:
        out["total_support_eligible_spend"] = data["totalSupportEligibleSpend"]
    else:
        out["total_support_eligible_spend"] = ""
    if data.get("proratedTotalSupportEligibleSpend") is not None:
        out["prorated_total_support_eligible_spend"] = data[
            "proratedTotalSupportEligibleSpend"
        ]
    else:
        out["prorated_total_support_eligible_spend"] = ""
    if data.get("linkedTimePeriods") is not None:
        import capo_billing.types.time_period_list

        out["linked_time_periods"] = (
            capo_billing.types.time_period_list.deserialize_aws_json_1_0(
                data["linkedTimePeriods"]
            )
        )
    if data.get("subscriptionTimePeriods") is not None:
        import capo_billing.types.time_period_list

        out["subscription_time_periods"] = (
            capo_billing.types.time_period_list.deserialize_aws_json_1_0(
                data["subscriptionTimePeriods"]
            )
        )
    if data.get("totalSupportEligibleReservedInstanceSpend") is not None:
        out["total_support_eligible_reserved_instance_spend"] = data[
            "totalSupportEligibleReservedInstanceSpend"
        ]
    if data.get("totalSupportEligibleSavingsPlanSpend") is not None:
        out["total_support_eligible_savings_plan_spend"] = data[
            "totalSupportEligibleSavingsPlanSpend"
        ]
    if data.get("supportEligibleSpendByService") is not None:
        import capo_billing.types.service_level_account_usage_list

        out["support_eligible_spend_by_service"] = (
            capo_billing.types.service_level_account_usage_list.deserialize_aws_json_1_0(
                data["supportEligibleSpendByService"]
            )
        )
    return out
