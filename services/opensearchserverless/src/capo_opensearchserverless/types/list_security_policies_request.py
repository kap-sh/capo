"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListSecurityPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.resource_filter
    import capo_opensearchserverless.types.security_policy_type


class ListSecurityPoliciesRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.security_policy_type.SecurityPolicyType"
    """<p>The type of policy.</p>"""
    resource: NotRequired[
        "capo_opensearchserverless.types.resource_filter.ResourceFilter"
    ]
    """<p>Resource filters (can be collection or indexes) that policies can apply to. </p>"""
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListSecurityPolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListSecurityPolicies</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results. The default is 20.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSecurityPoliciesRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "resource" in value:
        import capo_opensearchserverless.types.resource_filter

        out["resource"] = (
            capo_opensearchserverless.types.resource_filter.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSecurityPoliciesRequest:
    out: ListSecurityPoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("resource") is not None:
        import capo_opensearchserverless.types.resource_filter

        out["resource"] = (
            capo_opensearchserverless.types.resource_filter.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
