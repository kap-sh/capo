"""Generated from Smithy shape ``com.amazonaws.eks#AssociateAccessPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.access_scope
    import capo_eks.types.string


class AssociateAccessPolicyRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM user or role for the <code>AccessEntry</code> that you're associating the access policy to. </p>"""
    policy_arn: "capo_eks.types.string.String"
    """<p>The ARN of the <code>AccessPolicy</code> that you're associating. For a list of ARNs, use <code>ListAccessPolicies</code>.</p>"""
    access_scope: "capo_eks.types.access_scope.AccessScope"
    """<p>The scope for the <code>AccessPolicy</code>. You can scope access policies to an entire cluster or to specific Kubernetes namespaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateAccessPolicyRequest) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    import capo_eks.types.access_scope

    out["accessScope"] = capo_eks.types.access_scope.serialize_json(
        value["access_scope"]
    )
    return out


def deserialize_json(data: dict) -> AssociateAccessPolicyRequest:
    out: AssociateAccessPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("accessScope") is not None:
        import capo_eks.types.access_scope

        out["access_scope"] = capo_eks.types.access_scope.deserialize_json(
            data["accessScope"]
        )
    else:
        raise DeserializationError("AssociateAccessPolicyRequest.access_scope required")
    return out
