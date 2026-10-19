"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenForJWTRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_token_type
    import capo_bedrock_agentcore.types.workload_identity_name_type


class GetWorkloadAccessTokenForJWTRequest(TypedDict, closed=True):
    workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType"
    """<p>The unique identifier for the registered workload.</p>"""
    user_token: "capo_bedrock_agentcore.types.user_token_type.UserTokenType"
    """<p>The OAuth 2.0 token issued by the user's identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenForJWTRequest) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["userToken"] = value["user_token"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenForJWTRequest:
    out: GetWorkloadAccessTokenForJWTRequest = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        out["workload_name"] = ""
    if data.get("userToken") is not None:
        out["user_token"] = data["userToken"]
    else:
        out["user_token"] = ""
    return out


def redact_sensitive(value: GetWorkloadAccessTokenForJWTRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_token" in value:
        out["user_token"] = "*** Sensitive Data Redacted ***"
    return out
