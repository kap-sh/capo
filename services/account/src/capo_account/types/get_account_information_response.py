"""Generated from Smithy shape ``com.amazonaws.account#GetAccountInformationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.account_created_date
    import capo_account.types.account_id
    import capo_account.types.account_name
    import capo_account.types.account_state


class GetAccountInformationResponse(TypedDict, closed=True):
    account_id: NotRequired["capo_account.types.account_id.AccountId"]
    """<p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>"""
    account_name: NotRequired["capo_account.types.account_name.AccountName"]
    """<p>The name of the account.</p>"""
    account_created_date: NotRequired[
        "capo_account.types.account_created_date.AccountCreatedDate"
    ]
    """<p>The date and time the account was created.</p>"""
    account_state: NotRequired["capo_account.types.account_state.AccountState"]
    """<p>The state of the account. Each account state represents a specific phase in the account lifecycle. Use this information to manage account access, automate workflows, or trigger actions based on account state changes.</p> <p>Valid values: <code>PENDING_ACTIVATION | ACTIVE | SUSPENDED | CLOSED</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountInformationResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "account_name" in value:
        out["AccountName"] = value["account_name"]
    if "account_created_date" in value:
        import capo_account.types.account_created_date

        out["AccountCreatedDate"] = (
            capo_account.types.account_created_date.serialize_json(
                value["account_created_date"]
            )
        )
    if "account_state" in value:
        out["AccountState"] = value["account_state"]
    return out


def deserialize_json(data: dict) -> GetAccountInformationResponse:
    out: GetAccountInformationResponse = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("AccountName") is not None:
        out["account_name"] = data["AccountName"]
    if data.get("AccountCreatedDate") is not None:
        import capo_account.types.account_created_date

        out["account_created_date"] = (
            capo_account.types.account_created_date.deserialize_json(
                data["AccountCreatedDate"]
            )
        )
    if data.get("AccountState") is not None:
        out["account_state"] = data["AccountState"]
    return out
