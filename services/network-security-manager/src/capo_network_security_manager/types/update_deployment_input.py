"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UpdateDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_configuration
    import capo_network_security_manager.types.deployment_identifier
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.policy_reference_list
    import capo_network_security_manager.types.scope_reference_list
    import capo_network_security_manager.types.update_token


class UpdateDeploymentInput(TypedDict, closed=True):
    deployment_identifier: (
        "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier"
    )
    """<p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>"""
    update_token: "capo_network_security_manager.types.update_token.UpdateToken"
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    deployment_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the deployment.</p>"""
    deployment_configuration: NotRequired[
        "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>The configuration settings for the deployment.</p>"""
    associated_policy_list: NotRequired[
        "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList"
    ]
    """<p>The policies associated with the deployment.</p>"""
    associated_scope_list: NotRequired[
        "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList"
    ]
    """<p>The scope associated with the deployment. A deployment has exactly one scope.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentInput) -> dict:
    out: dict = {}
    out["updateToken"] = value["update_token"]
    if "deployment_description" in value:
        out["deploymentDescription"] = value["deployment_description"]
    if "deployment_configuration" in value:
        import capo_network_security_manager.types.deployment_configuration

        out["deploymentConfiguration"] = (
            capo_network_security_manager.types.deployment_configuration.serialize_json(
                value["deployment_configuration"]
            )
        )
    if "associated_policy_list" in value:
        import capo_network_security_manager.types.policy_reference_list

        out["associatedPolicyList"] = (
            capo_network_security_manager.types.policy_reference_list.serialize_json(
                value["associated_policy_list"]
            )
        )
    if "associated_scope_list" in value:
        import capo_network_security_manager.types.scope_reference_list

        out["associatedScopeList"] = (
            capo_network_security_manager.types.scope_reference_list.serialize_json(
                value["associated_scope_list"]
            )
        )
    out["isPublished"] = value["is_published"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDeploymentInput:
    out: UpdateDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    else:
        raise DeserializationError("UpdateDeploymentInput.update_token required")
    if data.get("deploymentDescription") is not None:
        out["deployment_description"] = data["deploymentDescription"]
    if data.get("deploymentConfiguration") is not None:
        import capo_network_security_manager.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_network_security_manager.types.deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    if data.get("associatedPolicyList") is not None:
        import capo_network_security_manager.types.policy_reference_list

        out["associated_policy_list"] = (
            capo_network_security_manager.types.policy_reference_list.deserialize_json(
                data["associatedPolicyList"]
            )
        )
    if data.get("associatedScopeList") is not None:
        import capo_network_security_manager.types.scope_reference_list

        out["associated_scope_list"] = (
            capo_network_security_manager.types.scope_reference_list.deserialize_json(
                data["associatedScopeList"]
            )
        )
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        raise DeserializationError("UpdateDeploymentInput.is_published required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
