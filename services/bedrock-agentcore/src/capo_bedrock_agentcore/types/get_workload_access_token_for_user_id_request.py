"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenForUserIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_id_type
    import capo_bedrock_agentcore.types.workload_identity_name_type


class GetWorkloadAccessTokenForUserIdRequest(TypedDict, closed=True):
    workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The name of the workload from which you want to retrieve the access token.</p>"""
    user_id: "capo_bedrock_agentcore.types.user_id_type.UserIdType"
    """<p>The ID of the user for whom you are retrieving the access token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenForUserIdRequest) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenForUserIdRequest:
    out: GetWorkloadAccessTokenForUserIdRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        out["workload_name"] = ""
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    return out
