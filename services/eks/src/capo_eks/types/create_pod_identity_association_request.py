"""Generated from Smithy shape ``com.amazonaws.eks#CreatePodIdentityAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eks.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eks.types.boxed_boolean
    import capo_eks.types.string
    import capo_eks.types.tag_map


class CreatePodIdentityAssociationRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the cluster to create the EKS Pod Identity association in.</p>"""
    namespace: "capo_eks.types.string.String"
    """<p>The name of the Kubernetes namespace inside the cluster to create the EKS Pod Identity association in. The service account and the Pods that use the service account must be in this namespace.</p>"""
    service_account: "capo_eks.types.string.String"
    """<p>The name of the Kubernetes service account inside the cluster to associate the IAM credentials with.</p>"""
    role_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the service account. The EKS Pod Identity agent manages credentials to assume this role for applications in the containers in the Pods that use this service account.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource – 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length – 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length – 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    disable_session_tags: NotRequired["capo_eks.types.boxed_boolean.BoxedBoolean"]
    """<p>Disable the automatic sessions tags that are appended by EKS Pod Identity.</p> <p>EKS Pod Identity adds a pre-defined set of session tags when it assumes the role. You can use these tags to author a single role that can work across resources by allowing access to Amazon Web Services resources based on matching tags. By default, EKS Pod Identity attaches six tags, including tags for cluster name, namespace, and service account name. For the list of tags added by EKS Pod Identity, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-id-abac.html#pod-id-abac-tags">List of session tags added by EKS Pod Identity</a> in the <i>Amazon EKS User Guide</i>.</p> <p>Amazon Web Services compresses inline session policies, managed policy ARNs, and session tags into a packed binary format that has a separate limit. If you receive a <code>PackedPolicyTooLarge</code> error indicating the packed binary format has exceeded the size limit, you can attempt to reduce the size by disabling the session tags added by EKS Pod Identity.</p>"""
    target_role_arn: NotRequired["capo_eks.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the target IAM role to associate with the service account. This role is assumed by using the EKS Pod Identity association role, then the credentials for this role are injected into the Pod.</p> <p>When you run applications on Amazon EKS, your application might need to access Amazon Web Services resources from a different role that exists in the same or different Amazon Web Services account. For example, your application running in “Account A” might need to access resources, such as Amazon S3 buckets in “Account B” or within “Account A” itself. You can create a association to access Amazon Web Services resources in “Account B” by creating two IAM roles: a role in “Account A” and a role in “Account B” (which can be the same or different account), each with the necessary trust and permission policies. After you provide these roles in the <i>IAM role</i> and <i>Target IAM role</i> fields, EKS will perform role chaining to ensure your application gets the required permissions. This means Role A will assume Role B, allowing your Pods to securely access resources like S3 buckets in the target account.</p>"""
    policy: NotRequired["capo_eks.types.string.String"]
    """<p>An optional IAM policy in JSON format (as an escaped string) that applies additional restrictions to this pod identity association beyond the IAM policies attached to the IAM role. This policy is applied as the intersection of the role's policies and this policy, allowing you to reduce the permissions that applications in the pods can use. Use this policy to enforce least privilege access while still leveraging a shared IAM role across multiple applications.</p> <p> <b>Important considerations</b> </p> <ul> <li> <p> <b>Session tags:</b> When using this policy, <code>disableSessionTags</code> must be set to <code>true</code>.</p> </li> <li> <p> <b>Target role permissions:</b> If you specify both a <code>TargetRoleArn</code> and a policy, the policy restrictions apply only to the target role's permissions, not to the initial role used for assuming the target role.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePodIdentityAssociationRequest) -> dict:
    out: dict = {}
    out["namespace"] = value["namespace"]
    out["serviceAccount"] = value["service_account"]
    out["roleArn"] = value["role_arn"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    if "disable_session_tags" in value:
        out["disableSessionTags"] = value["disable_session_tags"]
    if "target_role_arn" in value:
        out["targetRoleArn"] = value["target_role_arn"]
    if "policy" in value:
        out["policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> CreatePodIdentityAssociationRequest:
    out: CreatePodIdentityAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError(
            "CreatePodIdentityAssociationRequest.namespace required"
        )
    if data.get("serviceAccount") is not None:
        out["service_account"] = data["serviceAccount"]
    else:
        raise DeserializationError(
            "CreatePodIdentityAssociationRequest.service_account required"
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "CreatePodIdentityAssociationRequest.role_arn required"
        )
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("disableSessionTags") is not None:
        out["disable_session_tags"] = data["disableSessionTags"]
    if data.get("targetRoleArn") is not None:
        out["target_role_arn"] = data["targetRoleArn"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    return out
