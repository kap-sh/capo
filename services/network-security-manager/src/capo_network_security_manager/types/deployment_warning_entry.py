"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#DeploymentWarningEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_arn


class DeploymentWarningEntry(TypedDict, closed=True):
    code: "str"
    """<p>A code that identifies the type of warning.</p>"""
    policy_arn: "capo_network_security_manager.types.policy_arn.PolicyArn"
    """<p>The ARN of the policy that the warning relates to.</p>"""
    message: "str"
    """<p>A human-readable description of the warning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentWarningEntry) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["policyArn"] = value["policy_arn"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeploymentWarningEntry:
    out: DeploymentWarningEntry = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("DeploymentWarningEntry.code required")
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("DeploymentWarningEntry.policy_arn required")
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        raise DeserializationError("DeploymentWarningEntry.message required")
    return out
