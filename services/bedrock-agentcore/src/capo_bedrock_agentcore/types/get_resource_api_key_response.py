"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourceApiKeyResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.api_key_type


class GetResourceApiKeyResponse(TypedDict, closed=True):
    api_key: "capo_bedrock_agentcore.types.api_key_type.ApiKeyType"
    """<p>The API key associated with the resource requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceApiKeyResponse) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> GetResourceApiKeyResponse:
    out: GetResourceApiKeyResponse = {}  # type: ignore[typeddict-item]
    if data.get("apiKey") is not None:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError("GetResourceApiKeyResponse.api_key required")
    return out


def redact_sensitive(value: GetResourceApiKeyResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "api_key" in value:
        out["api_key"] = "*** Sensitive Data Redacted ***"
    return out
