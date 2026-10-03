"""Generated from Smithy shape ``com.amazonaws.eks#UpdateAccessEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list


class UpdateAccessEntryRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "capo_eks.types.string.String"
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>.</p>"""
    kubernetes_groups: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The value for <code>name</code> that you've specified for <code>kind: Group</code> as a <code>subject</code> in a Kubernetes <code>RoleBinding</code> or <code>ClusterRoleBinding</code> object. Amazon EKS doesn't confirm that the value for <code>name</code> exists in any bindings on your cluster. You can specify one or more names.</p> <p>Kubernetes authorizes the <code>principalArn</code> of the access entry to access any cluster objects that you've specified in a Kubernetes <code>Role</code> or <code>ClusterRole</code> object that is also specified in a binding's <code>roleRef</code>. For more information about creating Kubernetes <code>RoleBinding</code>, <code>ClusterRoleBinding</code>, <code>Role</code>, or <code>ClusterRole</code> objects, see <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">Using RBAC Authorization in the Kubernetes documentation</a>.</p> <p>If you want Amazon EKS to authorize the <code>principalArn</code> (instead of, or in addition to Kubernetes authorizing the <code>principalArn</code>), you can associate one or more access policies to the access entry using <code>AssociateAccessPolicy</code>. If you associate any access policies, the <code>principalARN</code> has all permissions assigned in the associated access policies and all permissions in any Kubernetes <code>Role</code> or <code>ClusterRole</code> objects that the group names are bound to.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    username: NotRequired["capo_eks.types.string.String"]
    """<p>The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries">Creating access entries</a> in the <i>Amazon EKS User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccessEntryRequest) -> dict:
    out: dict = {}
    if "kubernetes_groups" in value:
        import capo_eks.types.string_list

        out["kubernetesGroups"] = capo_eks.types.string_list.serialize_json(
            value["kubernetes_groups"]
        )
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> UpdateAccessEntryRequest:
    out: UpdateAccessEntryRequest = {}  # type: ignore[typeddict-item]
    if data.get("kubernetesGroups") is not None:
        import capo_eks.types.string_list

        out["kubernetes_groups"] = capo_eks.types.string_list.deserialize_json(
            data["kubernetesGroups"]
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    return out
