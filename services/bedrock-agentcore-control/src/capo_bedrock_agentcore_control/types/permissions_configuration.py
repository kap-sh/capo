"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PermissionsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.role_arn


class PermissionsConfiguration(TypedDict, closed=True):
    capacity_provider_operator_role_arn: (
        "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM role that AgentCore assumes to manage the capacity provider, including launching, tagging, and terminating instances and their network interfaces. We recommend scoping this role to the minimum permissions that your workloads require.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionsConfiguration) -> dict:
    out: dict = {}
    out["capacityProviderOperatorRoleArn"] = value[
        "capacity_provider_operator_role_arn"
    ]
    return out


def deserialize_json(data: dict) -> PermissionsConfiguration:
    out: PermissionsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderOperatorRoleArn") is not None:
        out["capacity_provider_operator_role_arn"] = data[
            "capacityProviderOperatorRoleArn"
        ]
    else:
        out["capacity_provider_operator_role_arn"] = ""
    return out
