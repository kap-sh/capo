"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetWorkloadAccessTokenForUserIdResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.workload_identity_token_type


class GetWorkloadAccessTokenForUserIdResponse(TypedDict, closed=True):
    workload_access_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType"
    """<p>The access token for the specified workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadAccessTokenForUserIdResponse) -> dict:
    out: dict = {}
    out["workloadAccessToken"] = value["workload_access_token"]
    return out


def deserialize_json(data: dict) -> GetWorkloadAccessTokenForUserIdResponse:
    out: GetWorkloadAccessTokenForUserIdResponse = {}  # type: ignore[typeddict-item]
    if data.get("workloadAccessToken") is not None:
        out["workload_access_token"] = data["workloadAccessToken"]
    else:
        raise DeserializationError(
            "GetWorkloadAccessTokenForUserIdResponse.workload_access_token required"
        )
    return out


def redact_sensitive(value: GetWorkloadAccessTokenForUserIdResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "workload_access_token" in value:
        out["workload_access_token"] = "*** Sensitive Data Redacted ***"
    return out
