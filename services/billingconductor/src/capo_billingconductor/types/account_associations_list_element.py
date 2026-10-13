"""Generated from Smithy shape ``com.amazonaws.billingconductor#AccountAssociationsListElement``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billingconductor.types.account_email
    import capo_billingconductor.types.account_id
    import capo_billingconductor.types.account_name
    import capo_billingconductor.types.billing_group_arn


class AccountAssociationsListElement(TypedDict, closed=True):
    account_id: NotRequired["capo_billingconductor.types.account_id.AccountId"]
    """<p>The associating array of account IDs.</p>"""
    billing_group_arn: NotRequired[
        "capo_billingconductor.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The Billing Group Arn that the linked account is associated to.</p>"""
    account_name: NotRequired["capo_billingconductor.types.account_name.AccountName"]
    """<p>The Amazon Web Services account name.</p>"""
    account_email: NotRequired["capo_billingconductor.types.account_email.AccountEmail"]
    """<p>The Amazon Web Services account email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAssociationsListElement) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "billing_group_arn" in value:
        out["BillingGroupArn"] = value["billing_group_arn"]
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "account_email" in value:
        out["AccountEmail"] = value["account_email"]
    return out


def deserialize_json(data: dict) -> AccountAssociationsListElement:
    out: AccountAssociationsListElement = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("BillingGroupArn") is not None:
        out["billing_group_arn"] = data["BillingGroupArn"]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("AccountEmail") is not None:
        out["account_email"] = data["AccountEmail"]
    return out


def redact_sensitive(value: AccountAssociationsListElement) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "account_name" in value:
        out["account_name"] = "*** Sensitive Data Redacted ***"
    if "account_email" in value:
        out["account_email"] = "*** Sensitive Data Redacted ***"
    return out
