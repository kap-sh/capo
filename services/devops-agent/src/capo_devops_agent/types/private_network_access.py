"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateNetworkAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.role_arn


class PrivateNetworkAccess(TypedDict, closed=True):
    private_connection_name: (
        "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    )
    """<p>Name of the private connection that supplies the VPC configuration for this release management environment.</p>"""
    runtime_role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>Role ARN that AWS DevOps Agent assumes at runtime to connect to your VPC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateNetworkAccess) -> dict:
    out: dict = {}
    out["privateConnectionName"] = value["private_connection_name"]
    out["runtimeRoleArn"] = value["runtime_role_arn"]
    return out


def deserialize_json(data: dict) -> PrivateNetworkAccess:
    out: PrivateNetworkAccess = {}  # type: ignore[typeddict-item]
    if data.get("privateConnectionName") is not None:
        out["private_connection_name"] = data["privateConnectionName"]
    else:
        raise DeserializationError(
            "PrivateNetworkAccess.private_connection_name required"
        )
    if data.get("runtimeRoleArn") is not None:
        out["runtime_role_arn"] = data["runtimeRoleArn"]
    else:
        raise DeserializationError("PrivateNetworkAccess.runtime_role_arn required")
    return out
