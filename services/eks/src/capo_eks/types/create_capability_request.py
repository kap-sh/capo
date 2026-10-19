"""Generated from Smithy shape ``com.amazonaws.eks#CreateCapabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.capability_configuration_request
    import capo_eks.types.capability_delete_propagation_policy
    import capo_eks.types.capability_type
    import capo_eks.types.string
    import capo_eks.types.tag_map


class CreateCapabilityRequest(TypedDict, closed=True):
    capability_name: "capo_eks.types.string.String"
    """<p>A unique name for the capability. The name must be unique within your cluster and can contain alphanumeric characters, hyphens, and underscores.</p>"""
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster where you want to create the capability.</p>"""
    client_request_token: NotRequired["capo_eks.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is valid for 24 hours after creation. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.</p>"""
    type: "capo_eks.types.capability_type.CapabilityType"
    """<p>The type of capability to create. Valid values are:</p> <ul> <li> <p> <code>ACK</code> – Amazon Web Services Controllers for Kubernetes (ACK), which lets you manage resources directly from Kubernetes.</p> </li> <li> <p> <code>ARGOCD</code> – Argo CD for GitOps-based continuous delivery.</p> </li> <li> <p> <code>KRO</code> – Kube Resource Orchestrator (KRO) for composing and managing custom Kubernetes resources.</p> </li> </ul>"""
    role_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the IAM role that the capability uses to interact with Amazon Web Services services. This role must have a trust policy that allows the EKS service principal to assume it, and it must have the necessary permissions for the capability type you're creating.</p> <p>For ACK capabilities, the role needs permissions to manage the resources you want to control through Kubernetes. For Argo CD capabilities, the role needs permissions to access Git repositories and Secrets Manager. For KRO capabilities, the role needs permissions based on the resources you'll be orchestrating.</p>"""
    configuration: NotRequired[
        "capo_eks.types.capability_configuration_request.CapabilityConfigurationRequest"
    ]
    """<p>The configuration settings for the capability. The structure of this object varies depending on the capability type. For Argo CD capabilities, you can configure IAM Identity CenterIAM; Identity Center integration, RBAC role mappings, and network access settings.</p>"""
    tags: NotRequired["capo_eks.types.tag_map.TagMap"]
    delete_propagation_policy: "capo_eks.types.capability_delete_propagation_policy.CapabilityDeletePropagationPolicy"
    """<p>Specifies how Kubernetes resources managed by the capability should be handled when the capability is deleted. Currently, the only supported value is <code>RETAIN</code> which retains all Kubernetes resources managed by the capability when the capability is deleted.</p> <p>Because resources are retained, all Kubernetes resources created by the capability should be deleted from the cluster before deleting the capability itself. After the capability is deleted, these resources become difficult to manage because the controller is no longer available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCapabilityRequest) -> dict:
    out: dict = {}
    out["capabilityName"] = value["capability_name"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    import capo_eks.types.capability_type

    out["type"] = capo_eks.types.capability_type.serialize_json(value["type"])
    out["roleArn"] = value["role_arn"]
    if "configuration" in value:
        import capo_eks.types.capability_configuration_request

        out["configuration"] = (
            capo_eks.types.capability_configuration_request.serialize_json(
                value["configuration"]
            )
        )
    if "tags" in value:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.serialize_json(value["tags"])
    import capo_eks.types.capability_delete_propagation_policy

    out["deletePropagationPolicy"] = (
        capo_eks.types.capability_delete_propagation_policy.serialize_json(
            value["delete_propagation_policy"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateCapabilityRequest:
    out: CreateCapabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("capabilityName") is not None:
        out["capability_name"] = data["capabilityName"]
    else:
        out["capability_name"] = ""
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    if data.get("type") is not None:
        import capo_eks.types.capability_type

        out["type"] = capo_eks.types.capability_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_eks.types.capability_type.CapabilityType", "")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("configuration") is not None:
        import capo_eks.types.capability_configuration_request

        out["configuration"] = (
            capo_eks.types.capability_configuration_request.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("tags") is not None:
        import capo_eks.types.tag_map

        out["tags"] = capo_eks.types.tag_map.deserialize_json(data["tags"])
    if data.get("deletePropagationPolicy") is not None:
        import capo_eks.types.capability_delete_propagation_policy

        out["delete_propagation_policy"] = (
            capo_eks.types.capability_delete_propagation_policy.deserialize_json(
                data["deletePropagationPolicy"]
            )
        )
    else:
        import typing

        out["delete_propagation_policy"] = typing.cast(
            "capo_eks.types.capability_delete_propagation_policy.CapabilityDeletePropagationPolicy",
            "",
        )
    return out
