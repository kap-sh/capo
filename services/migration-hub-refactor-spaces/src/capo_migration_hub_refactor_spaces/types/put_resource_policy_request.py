"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.policy_string
    import capo_migration_hub_refactor_spaces.types.resource_arn


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_migration_hub_refactor_spaces.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to which the policy is being attached. </p>"""
    policy: "capo_migration_hub_refactor_spaces.types.policy_string.PolicyString"
    """<p>A JSON-formatted string for an Amazon Web Services resource-based policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
