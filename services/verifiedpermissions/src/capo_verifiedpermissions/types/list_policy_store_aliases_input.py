"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPolicyStoreAliasesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.max_results
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_store_alias_filter


class ListPolicyStoreAliasesInput(TypedDict, closed=True):
    next_token: NotRequired["capo_verifiedpermissions.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired["capo_verifiedpermissions.types.max_results.MaxResults"]
    """<p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 5 policy store aliases per response. You can specify a maximum of 50 policy store aliases per response.</p>"""
    filter: NotRequired[
        "capo_verifiedpermissions.types.policy_store_alias_filter.PolicyStoreAliasFilter"
    ]
    """<p>Specifies a filter to narrow the results. You can filter by <code>policyStoreId</code> to list only the policy store aliases associated with a specific policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPolicyStoreAliasesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_verifiedpermissions.types.policy_store_alias_filter

        out["filter"] = (
            capo_verifiedpermissions.types.policy_store_alias_filter.serialize_aws_json_1_0(
                value["filter"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPolicyStoreAliasesInput:
    out: ListPolicyStoreAliasesInput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_verifiedpermissions.types.policy_store_alias_filter

        out["filter"] = (
            capo_verifiedpermissions.types.policy_store_alias_filter.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    return out
