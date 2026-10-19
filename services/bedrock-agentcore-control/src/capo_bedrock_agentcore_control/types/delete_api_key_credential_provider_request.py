"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteApiKeyCredentialProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_name


class DeleteApiKeyCredentialProviderRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the API key credential provider to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApiKeyCredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteApiKeyCredentialProviderRequest:
    out: DeleteApiKeyCredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
