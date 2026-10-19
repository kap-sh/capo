"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.workload_identity_name_type


class GetWorkloadAccessTokenRequest(TypedDict, closed=True):
    workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The unique identifier for the registered workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenRequest) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenRequest:
    out: GetWorkloadAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        out["workload_name"] = ""
    return out
