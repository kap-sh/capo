"""Generated from Smithy shape ``com.amazonaws.account#DeleteAlternateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.alternate_contact_type


class DeleteAlternateContactRequest(TypedDict, closed=True):
    alternate_contact_type: (
        "capo_account.types.alternate_contact_type.AlternateContactType"
    )
    """<p>Specifies which of the alternate contacts to delete. </p>"""
    account_id: NotRequired["capo_account.types.account_id.AccountId"]
    """<p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAlternateContactRequest) -> dict:
    out: dict = {}
    out["AlternateContactType"] = value["alternate_contact_type"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> DeleteAlternateContactRequest:
    out: DeleteAlternateContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("AlternateContactType") is not None:
        out["alternate_contact_type"] = data["AlternateContactType"]
    else:
        raise DeserializationError(
            "DeleteAlternateContactRequest.alternate_contact_type required"
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
