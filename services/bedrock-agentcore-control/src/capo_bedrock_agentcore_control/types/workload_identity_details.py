"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WorkloadIdentityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.workload_identity_arn


class WorkloadIdentityDetails(TypedDict, closed=True):
    workload_identity_arn: (
        "capo_bedrock_agentcore_control.types.workload_identity_arn.WorkloadIdentityArn"
    )
    """<p>The ARN associated with the workload identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadIdentityDetails) -> dict:
    out: dict = {}
    out["workloadIdentityArn"] = value["workload_identity_arn"]
    return out


def deserialize_json(data: dict) -> WorkloadIdentityDetails:
    out: WorkloadIdentityDetails = {}  # type: ignore[typeddict-item]
    if data.get("workloadIdentityArn") is not None:
        out["workload_identity_arn"] = data["workloadIdentityArn"]
    else:
        out["workload_identity_arn"] = ""
    return out
