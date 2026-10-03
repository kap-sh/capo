"""Generated from Smithy shape ``com.amazonaws.account#StartPrimaryEmailUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.primary_email_address


class StartPrimaryEmailUpdateRequest(TypedDict, closed=True):
    account_id: "capo_account.types.account_id.AccountId"
    """<p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <p>This operation can only be called from the management account or the delegated administrator account of an organization for a member account.</p> <note> <p>The management account can't specify its own <code>AccountId</code>.</p> </note>"""
    primary_email: "capo_account.types.primary_email_address.PrimaryEmailAddress"
    """<p>The new primary email address (also known as the root user email address) to use in the specified account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartPrimaryEmailUpdateRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["PrimaryEmail"] = value["primary_email"]
    return out


def deserialize_json(data: dict) -> StartPrimaryEmailUpdateRequest:
    out: StartPrimaryEmailUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("StartPrimaryEmailUpdateRequest.account_id required")
    if data.get("PrimaryEmail") is not None:
        out["primary_email"] = data["PrimaryEmail"]
    else:
        raise DeserializationError(
            "StartPrimaryEmailUpdateRequest.primary_email required"
        )
    return out
