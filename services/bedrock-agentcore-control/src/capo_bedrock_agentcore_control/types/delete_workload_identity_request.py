"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteWorkloadIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.workload_identity_name_type


class DeleteWorkloadIdentityRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload identity to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkloadIdentityRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteWorkloadIdentityRequest:
    out: DeleteWorkloadIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
