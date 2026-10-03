"""Generated from Smithy shape ``com.amazonaws.eks#UpdatePodIdentityAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.string


class UpdatePodIdentityAssociationRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the cluster that you want to update the association in.</p>"""
    association_id: "capo_eks.types.string.String"
    """<p>The ID of the association to be updated.</p>"""
    role_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The new IAM role to change in the association.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    disable_session_tags: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Disable the automatic sessions tags that are appended by EKS Pod Identity.</p> <p>EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to Amazon Web Services resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags">List of session tags added by EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p> <p>Amazon Web Services compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a <code>PackedPolicyTooLarge</code> error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity.</p>"""
    target_role_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.</p> <p>When you run applications on Amazon EKS, your application might need to access Amazon Web Services resources from a different role that exists in the same or different Amazon Web Services account. For example, your application running in “Account A” might need to access resources, such as buckets in “Account B” or within “Account A” itself. You can create a association to access Amazon Web Services resources in “Account B” by creating two IAM roles: a role in “Account A” and a role in “Account B” (which can be the same or different account), each with the necessary trust and permission policies. After you provide these roles in the <i>IAM role</i> and <i>Target IAM role</i> fields, EKS will perform role chaining to ensure your application gets the required permissions. This means Role A will assume Role B, allowing your Pods to securely access resources like S3 buckets in the target account.</p>"""
    policy: NotRequired["capo_eks.types.string.String"]
    """<p>An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.</p> <p> <b>Important considerations</b> </p> <ul> <li> <p> <b>Session tags:</b> When using this policy, <code>disableSessionTags</code> must be set to <code>true</code>.</p> </li> <li> <p> <b>Target role permissions:</b> If you specify both a <code>TargetRoleArn</code> and a policy, the policy restrictions apply only to the target role's permissions, not to the initial role used for assuming the target role.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePodIdentityAssociationRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "disable_session_tags" in value:
        out["disableSessionTags"] = value["disable_session_tags"]
    if "target_role_arn" in value:
        out["targetRoleArn"] = value["target_role_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> UpdatePodIdentityAssociationRequest:
    out: UpdatePodIdentityAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("disableSessionTags") is not None:
        out["disable_session_tags"] = data["disableSessionTags"]
    if data.get("targetRoleArn") is not None:
        out["target_role_arn"] = data["targetRoleArn"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out
