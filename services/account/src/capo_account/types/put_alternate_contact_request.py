"""Generated from Smithy shape ``com.amazonaws.account#PutAlternateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.alternate_contact_type
    import capo_account.types.email_address
    import capo_account.types.name
    import capo_account.types.phone_number
    import capo_account.types.title


class PutAlternateContactRequest(TypedDict, closed=True):
    name: "capo_account.types.name.Name"
    """<p>Specifies a name for the alternate contact.</p>"""
    title: "capo_account.types.title.Title"
    """<p>Specifies a title for the alternate contact.</p>"""
    email_address: "capo_account.types.email_address.EmailAddress"
    """<p>Specifies an email address for the alternate contact. </p>"""
    phone_number: "capo_account.types.phone_number.PhoneNumber"
    """<p>Specifies a phone number for the alternate contact.</p>"""
    alternate_contact_type: (
        "capo_account.types.alternate_contact_type.AlternateContactType"
    )
    """<p>Specifies which alternate contact you want to create or update.</p>"""
    account_id: NotRequired["capo_account.types.account_id.AccountId"]
    """<p>Specifies the 12 digit account ID number of the Amazon Web Services account that you want to access or modify with this operation.</p> <p>If you do not specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation.</p> <p>To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account, and the specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated administrator</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>; it must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, then don't specify this parameter, and call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAlternateContactRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Title"] = value["title"]
    out["EmailAddress"] = value["email_address"]
    out["PhoneNumber"] = value["phone_number"]
    out["AlternateContactType"] = value["alternate_contact_type"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> PutAlternateContactRequest:
    out: PutAlternateContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutAlternateContactRequest.name required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("PutAlternateContactRequest.title required")
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    else:
        raise DeserializationError("PutAlternateContactRequest.email_address required")
    if data.get("PhoneNumber") is not None:
        out["phone_number"] = data["PhoneNumber"]
    else:
        raise DeserializationError("PutAlternateContactRequest.phone_number required")
    if data.get("AlternateContactType") is not None:
        out["alternate_contact_type"] = data["AlternateContactType"]
    else:
        raise DeserializationError(
            "PutAlternateContactRequest.alternate_contact_type required"
        )
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
