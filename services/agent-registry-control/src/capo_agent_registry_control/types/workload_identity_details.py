"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#WorkloadIdentityDetails``."""

from typing_extensions import TypedDict


class WorkloadIdentityDetails(TypedDict, closed=True):
    workload_identity_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the workload identity associated with the source resource.</p>"""


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
