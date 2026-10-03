"""Generated from Smithy shape ``com.amazonaws.eks#CreateAccessEntryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.string
    import capo_eks.types.string_list
    import capo_eks.types.tag_map


class CreateAccessEntryRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    principal_arn: "capo_eks.types.string.String"
    """<p>The ARN of the IAM principal for the <code>AccessEntry</code>. You can specify one ARN for each access entry. You can't specify the same ARN in more than one access entry. This value can't be changed after access entry creation.</p> <p>The valid principals differ depending on the type of the access entry in the <code>type</code> field. For <code>STANDARD</code> access entries, you can use every IAM principal type. For nodes (<code>EC2</code> (for EKS Auto Mode), <code>EC2_LINUX</code>, <code>EC2_WINDOWS</code>, <code>FARGATE_LINUX</code>, and <code>HYBRID_LINUX</code>), the only valid ARN is IAM roles. You can't use the STS session principal type with access entries because this is a temporary principal for each session and not a permanent identity that can be assigned permissions.</p> <p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp">IAM best practices</a> recommend using IAM roles with temporary credentials, rather than IAM users with long-term credentials. </p>"""
    kubernetes_groups: NotRequired["capo_eks.types.string_list.StringList"]
    """<p>The value for <code>name</code> that you've specified for <code>kind: Group</code> as a <code>subject</code> in a Kubernetes <code>RoleBinding</code> or <code>ClusterRoleBinding</code> object. Amazon EKS doesn't confirm that the value for <code>name</code> exists in any bindings on your cluster. You can specify one or more names.</p> <p>Kubernetes authorizes the <code>principalArn</code> of the access entry to access any cluster objects that you've specified in a Kubernetes <code>Role</code> or <code>ClusterRole</code> object that is also specified in a binding's <code>roleRef</code>. For more information about creating Kubernetes <code>RoleBinding</code>, <code>ClusterRoleBinding</code>, <code>Role</code>, or <code>ClusterRole</code> objects, see <a href="https://kubernetes.io/docs/reference/access-authn-authz/rbac/">Using RBAC Authorization in the Kubernetes documentation</a>.</p> <p>If you want Amazon EKS to authorize the <code>principalArn</code> (instead of, or in addition to Kubernetes authorizing the <code>principalArn</code>), you can associate one or more access policies to the access entry using <code>AssociateAccessPolicy</code>. If you associate any access policies, the <code>principalARN</code> has all permissions assigned in the associated access policies and all permissions in any Kubernetes <code>Role</code> or <code>ClusterRole</code> objects that the group names are bound to.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    username: NotRequired["capo_eks.types.string.String"]
    """<p>The username to authenticate to Kubernetes with. We recommend not specifying a username and letting Amazon EKS specify it for you. For more information about the value Amazon EKS specifies for you, or constraints before specifying your own username, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html#creating-access-entries">Creating access entries</a> in the <i>Amazon EKS User Guide</i>.</p>"""
    type: NotRequired["capo_eks.types.string.String"]
    """<p>The type of the new access entry. Valid values are <code>STANDARD</code>, <code>FARGATE_LINUX</code>, <code>EC2_LINUX</code>, <code>EC2_WINDOWS</code>, <code>EC2</code> (for EKS Auto Mode), <code>HYBRID_LINUX</code>, and <code>HYPERPOD_LINUX</code>. </p> <p>If the <code>principalArn</code> is for an IAM role that's used for self-managed Amazon EC2 nodes, specify <code>EC2_LINUX</code> or <code>EC2_WINDOWS</code>. Amazon EKS grants the necessary permissions to the node for you. If the <code>principalArn</code> is for any other purpose, specify <code>STANDARD</code>. If you don't specify a value, Amazon EKS sets the value to <code>STANDARD</code>. If you have the access mode of the cluster set to <code>API_AND_CONFIG_MAP</code>, it's unnecessary to create access entries for IAM roles used with Fargate profiles or managed Amazon EC2 nodes, because Amazon EKS creates entries in the <code>aws-auth</code> <code>ConfigMap</code> for the roles. You can't change this value once you've created the access entry.</p> <p>If you set the value to <code>EC2_LINUX</code> or <code>EC2_WINDOWS</code>, you can't specify values for <code>kubernetesGroups</code>, or associate an <code>AccessPolicy</code> to the access entry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessEntryRequest) -> dict:
    out: dict = {}
    out["principalArn"] = value["principal_arn"]
    if "kubernetes_groups" in value:
        import capo_eks.types.string_list

        out["kubernetesGroups"] = capo_eks.types.string_list.serialize_json(
            value["kubernetes_groups"]
        )
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "username" in value:
        out["username"] = value["username"]
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> CreateAccessEntryRequest:
    out: CreateAccessEntryRequest = {}  # type: ignore[typeddict-item]
    if data.get("principalArn") is not None:
        out["principal_arn"] = data["principalArn"]
    else:
        raise DeserializationError("CreateAccessEntryRequest.principal_arn required")
    if data.get("kubernetesGroups") is not None:
        import capo_eks.types.string_list

        out["kubernetes_groups"] = capo_eks.types.string_list.deserialize_json(
            data["kubernetesGroups"]
        )
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out
