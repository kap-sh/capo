"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_configuration
    import capo_network_security_manager.types.deployment_name
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.policy_reference_list
    import capo_network_security_manager.types.scope_reference_list
    import capo_network_security_manager.types.tag_map


class CreateDeploymentInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""
    deployment_name: (
        "capo_network_security_manager.types.deployment_name.DeploymentName"
    )
    """<p>The name of the deployment.</p>"""
    deployment_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the deployment.</p>"""
    deployment_configuration: "capo_network_security_manager.types.deployment_configuration.DeploymentConfiguration"
    """<p>The configuration settings for the deployment.</p>"""
    associated_policy_list: (
        "capo_network_security_manager.types.policy_reference_list.PolicyReferenceList"
    )
    """<p>The policies associated with the deployment.</p>"""
    associated_scope_list: (
        "capo_network_security_manager.types.scope_reference_list.ScopeReferenceList"
    )
    """<p>The scope associated with the deployment. A deployment has exactly one scope.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>"""
    tags: NotRequired["capo_network_security_manager.types.tag_map.TagMap"]
    """<p>The tags to add to the resource when it is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["deploymentName"] = value["deployment_name"]
    if "deployment_description" in value:
        out["deploymentDescription"] = value["deployment_description"]
    import capo_network_security_manager.types.deployment_configuration

    out["deploymentConfiguration"] = (
        capo_network_security_manager.types.deployment_configuration.serialize_json(
            value["deployment_configuration"]
        )
    )
    import capo_network_security_manager.types.policy_reference_list

    out["associatedPolicyList"] = (
        capo_network_security_manager.types.policy_reference_list.serialize_json(
            value["associated_policy_list"]
        )
    )
    import capo_network_security_manager.types.scope_reference_list

    out["associatedScopeList"] = (
        capo_network_security_manager.types.scope_reference_list.serialize_json(
            value["associated_scope_list"]
        )
    )
    out["isPublished"] = value.get("is_published", True)
    if "tags" in value:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDeploymentInput:
    out: CreateDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("deploymentName") is not None:
        out["deployment_name"] = data["deploymentName"]
    else:
        raise DeserializationError("CreateDeploymentInput.deployment_name required")
    if data.get("deploymentDescription") is not None:
        out["deployment_description"] = data["deploymentDescription"]
    if data.get("deploymentConfiguration") is not None:
        import capo_network_security_manager.types.deployment_configuration

        out["deployment_configuration"] = (
            capo_network_security_manager.types.deployment_configuration.deserialize_json(
                data["deploymentConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDeploymentInput.deployment_configuration required"
        )
    if data.get("associatedPolicyList") is not None:
        import capo_network_security_manager.types.policy_reference_list

        out["associated_policy_list"] = (
            capo_network_security_manager.types.policy_reference_list.deserialize_json(
                data["associatedPolicyList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDeploymentInput.associated_policy_list required"
        )
    if data.get("associatedScopeList") is not None:
        import capo_network_security_manager.types.scope_reference_list

        out["associated_scope_list"] = (
            capo_network_security_manager.types.scope_reference_list.deserialize_json(
                data["associatedScopeList"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDeploymentInput.associated_scope_list required"
        )
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        out["is_published"] = True
    if data.get("tags") is not None:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
