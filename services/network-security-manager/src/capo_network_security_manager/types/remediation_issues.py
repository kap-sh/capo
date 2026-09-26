"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RemediationIssues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_firewall_type
    import capo_network_security_manager.types.remediation_issue_details

RemediationIssues: TypeAlias = dict[
    "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType",
    "capo_network_security_manager.types.remediation_issue_details.RemediationIssueDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RemediationIssues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_security_manager.types.policy_firewall_type
        import capo_network_security_manager.types.remediation_issue_details

        out[
            capo_network_security_manager.types.policy_firewall_type.serialize_json(key)
        ] = capo_network_security_manager.types.remediation_issue_details.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> RemediationIssues:
    out: RemediationIssues = {}
    for key, value in data.items():
        import capo_network_security_manager.types.policy_firewall_type

        if value is None:
            continue
        import capo_network_security_manager.types.remediation_issue_details

        out[
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                key
            )
        ] = capo_network_security_manager.types.remediation_issue_details.deserialize_json(
            value
        )
    return out
