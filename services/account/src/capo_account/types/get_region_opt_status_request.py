"""Generated from Smithy shape ``com.amazonaws.account#GetRegionOptStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.region_name


class GetRegionOptStatusRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_account.types.account_id.AccountId"]
    """<p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>"""
    region_name: "capo_account.types.region_name.RegionName"
    """<p>Specifies the Region-code for a given Region name (for example, <code>af-south-1</code>). This function will return the status of whatever Region you pass into this parameter. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRegionOptStatusRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    out["RegionName"] = value["region_name"]
    return out


def deserialize_json(data: dict) -> GetRegionOptStatusRequest:
    out: GetRegionOptStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        raise DeserializationError("GetRegionOptStatusRequest.region_name required")
    return out
