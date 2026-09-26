"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentCoverageEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_policy_arn_list
    import capo_network_security_manager.types.deployment_resource_type_list
    import capo_network_security_manager.types.policy_firewall_type


class DeploymentCoverageEntry(TypedDict, closed=True):
    firewall_type: (
        "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType"
    )
    """<p>The firewall type that the policies in this entry share.</p>"""
    policy_arns: "capo_network_security_manager.types.deployment_policy_arn_list.DeploymentPolicyArnList"
    """<p>The Amazon Resource Names (ARNs) of the deployment's policies that have this firewall type.</p>"""
    in_scope_resource_types: "capo_network_security_manager.types.deployment_resource_type_list.DeploymentResourceTypeList"
    """<p>The resource types in the deployment's scope that this firewall type protects. This list is empty if the scope does not select any resource types that the firewall type protects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentCoverageEntry) -> dict:
    out: dict = {}
    import capo_network_security_manager.types.policy_firewall_type

    out["firewallType"] = (
        capo_network_security_manager.types.policy_firewall_type.serialize_json(
            value["firewall_type"]
        )
    )
    import capo_network_security_manager.types.deployment_policy_arn_list

    out["policyArns"] = (
        capo_network_security_manager.types.deployment_policy_arn_list.serialize_json(
            value["policy_arns"]
        )
    )
    import capo_network_security_manager.types.deployment_resource_type_list

    out["inScopeResourceTypes"] = (
        capo_network_security_manager.types.deployment_resource_type_list.serialize_json(
            value["in_scope_resource_types"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeploymentCoverageEntry:
    out: DeploymentCoverageEntry = {}  # type: ignore[typeddict-item]
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.policy_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("DeploymentCoverageEntry.firewall_type required")
    if data.get("policyArns") is not None:
        import capo_network_security_manager.types.deployment_policy_arn_list

        out["policy_arns"] = (
            capo_network_security_manager.types.deployment_policy_arn_list.deserialize_json(
                data["policyArns"]
            )
        )
    else:
        raise DeserializationError("DeploymentCoverageEntry.policy_arns required")
    if data.get("inScopeResourceTypes") is not None:
        import capo_network_security_manager.types.deployment_resource_type_list

        out["in_scope_resource_types"] = (
            capo_network_security_manager.types.deployment_resource_type_list.deserialize_json(
                data["inScopeResourceTypes"]
            )
        )
    else:
        raise DeserializationError(
            "DeploymentCoverageEntry.in_scope_resource_types required"
        )
    return out
