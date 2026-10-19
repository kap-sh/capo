"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListLifecyclePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.lifecycle_policy_type
    import capo_opensearchserverless.types.lifecycle_resource_filter


class ListLifecyclePoliciesRequest(TypedDict, closed=True):
    type: "capo_opensearchserverless.types.lifecycle_policy_type.LifecyclePolicyType"
    """<p>The type of lifecycle policy.</p>"""
    resources: NotRequired[
        "capo_opensearchserverless.types.lifecycle_resource_filter.LifecycleResourceFilter"
    ]
    """<p>Resource filters that policies can apply to. Currently, the only supported resource type is <code>index</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListLifecyclePolicies</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListLifecyclePolicies</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use use <code>nextToken</code> to get the next page of results. The default is 10.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListLifecyclePoliciesRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "resources" in value:
        import capo_opensearchserverless.types.lifecycle_resource_filter

        out["resources"] = (
            capo_opensearchserverless.types.lifecycle_resource_filter.serialize_aws_json_1_0(
                value["resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListLifecyclePoliciesRequest:
    out: ListLifecyclePoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("resources") is not None:
        import capo_opensearchserverless.types.lifecycle_resource_filter

        out["resources"] = (
            capo_opensearchserverless.types.lifecycle_resource_filter.deserialize_aws_json_1_0(
                data["resources"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
