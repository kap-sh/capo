"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListIdentitySourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.identity_source_filters
    import capo_verifiedpermissions.types.list_identity_sources_max_results
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_store_id


class ListIdentitySourcesInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that contains the identity sources that you want to list.</p> <p>To specify a policy store, use its ID or alias name. When using an alias name, prefix it with <code>policy-store-alias/</code>. For example:</p> <ul> <li> <p>ID: <code>PSEXAMPLEabcdefg111111</code> </p> </li> <li> <p>Alias name: <code>policy-store-alias/example-policy-store</code> </p> </li> </ul> <p>To view aliases, use <a href="https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicyStoreAliases.html">ListPolicyStoreAliases</a>.</p>"""
    next_token: NotRequired["capo_verifiedpermissions.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.</p>"""
    max_results: NotRequired[
        "capo_verifiedpermissions.types.list_identity_sources_max_results.ListIdentitySourcesMaxResults"
    ]
    """<p>Specifies the total number of results that you want included in each response. If additional items exist beyond the number you specify, the <code>NextToken</code> response element is returned with a value (not null). Include the specified value as the <code>NextToken</code> request parameter in the next call to the operation to get the next set of results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> <p>If you do not specify this parameter, the operation defaults to 10 identity sources per response. You can specify a maximum of 50 identity sources per response.</p>"""
    filters: NotRequired[
        "capo_verifiedpermissions.types.identity_source_filters.IdentitySourceFilters"
    ]
    """<p>Specifies characteristics of an identity source that you can use to limit the output to matching identity sources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListIdentitySourcesInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_verifiedpermissions.types.identity_source_filters

        out["filters"] = (
            capo_verifiedpermissions.types.identity_source_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListIdentitySourcesInput:
    out: ListIdentitySourcesInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("ListIdentitySourcesInput.policy_store_id required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filters") is not None:
        import capo_verifiedpermissions.types.identity_source_filters

        out["filters"] = (
            capo_verifiedpermissions.types.identity_source_filters.deserialize_aws_json_1_0(
                data["filters"]
            )
        )
    return out
