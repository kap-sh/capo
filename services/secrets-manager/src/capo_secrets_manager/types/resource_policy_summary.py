"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ResourcePolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.resource_policy_name_type


class ResourcePolicySummary(TypedDict, closed=True):
    policy_name: NotRequired[
        "capo_secrets_manager.types.resource_policy_name_type.ResourcePolicyNameType"
    ]
    """<p>The name of the resource policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourcePolicySummary) -> dict:
    out: dict = {}
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourcePolicySummary:
    out: ResourcePolicySummary = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    return out
