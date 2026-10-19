"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WorkloadIdentityType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.workload_identity_arn_type
    import capo_bedrock_agentcore_control.types.workload_identity_name_type


class WorkloadIdentityType(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity.</p>"""
    workload_identity_arn: "capo_bedrock_agentcore_control.types.workload_identity_arn_type.WorkloadIdentityArnType"
    """<p>The Amazon Resource Name (ARN) of the workload identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIdentityType) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["workloadIdentityArn"] = value["workload_identity_arn"]
    return out


def deserialize_json(data: dict) -> WorkloadIdentityType:
    out: WorkloadIdentityType = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("workloadIdentityArn") is not None:
        out["workload_identity_arn"] = data["workloadIdentityArn"]
    else:
        out["workload_identity_arn"] = ""
    return out
