"""Generated from Smithy shape ``com.amazonaws.account#ListRegionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_account.types.account_id
    import capo_account.types.region_opt_status_list


class ListRegionsRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_account.types.account_id.AccountId"]
    """<p>Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you don't specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account">organization's management account</a> or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html">all features enabled</a>, and the organization must have <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html">trusted access</a> enabled for the Account Management service, and optionally a <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin">delegated admin</a> account assigned.</p> <note> <p>The management account can't specify its own <code>AccountId</code>. It must call the operation in standalone context by not including the <code>AccountId</code> parameter.</p> </note> <p>To call this operation on an account that is not a member of an organization, don't specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.</p>"""
    max_results: NotRequired["int"]
    """<p>The total number of items to return in the command’s output. If the total number of items available is more than the value specified, a <code>NextToken</code> is provided in the command’s output. To resume pagination, provide the <code>NextToken</code> value in the <code>starting-token</code> argument of a subsequent command. Do not use the <code>NextToken</code> response element directly outside of the Amazon Web Services CLI. For usage examples, see <a href="http://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Pagination</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>. </p>"""
    next_token: NotRequired["str"]
    """<p>A token used to specify where to start paginating. This is the <code>NextToken</code> from a previously truncated response. For usage examples, see <a href="http://docs.aws.amazon.com/cli/latest/userguide/pagination.html">Pagination</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>.</p>"""
    region_opt_status_contains: NotRequired[
        "capo_account.types.region_opt_status_list.RegionOptStatusList"
    ]
    """<p>A list of Region statuses (Enabling, Enabled, Disabling, Disabled, Enabled_by_default) to use to filter the list of Regions for a given account. For example, passing in a value of ENABLING will only return a list of Regions with a Region status of ENABLING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegionsRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "region_opt_status_contains" in value:
        import capo_account.types.region_opt_status_list

        out["RegionOptStatusContains"] = (
            capo_account.types.region_opt_status_list.serialize_json(
                value["region_opt_status_contains"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRegionsRequest:
    out: ListRegionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RegionOptStatusContains") is not None:
        import capo_account.types.region_opt_status_list

        out["region_opt_status_contains"] = (
            capo_account.types.region_opt_status_list.deserialize_json(
                data["RegionOptStatusContains"]
            )
        )
    return out
