"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentPolicyArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_arn

DeploymentPolicyArnList: TypeAlias = list[
    "capo_network_security_manager.types.policy_arn.PolicyArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentPolicyArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> DeploymentPolicyArnList:
    return [item for item in data if item is not None]
