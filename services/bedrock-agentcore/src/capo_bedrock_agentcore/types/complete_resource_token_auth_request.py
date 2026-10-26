"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CompleteResourceTokenAuthRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.request_uri
    import capo_bedrock_agentcore.types.user_identifier


class CompleteResourceTokenAuthRequest(TypedDict, closed=True):
    user_identifier: "capo_bedrock_agentcore.types.user_identifier.UserIdentifier"
    """<p>The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.</p>"""
    session_uri: "capo_bedrock_agentcore.types.request_uri.RequestUri"
    """<p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteResourceTokenAuthRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.user_identifier

    out["userIdentifier"] = capo_bedrock_agentcore.types.user_identifier.serialize_json(
        value["user_identifier"]
    )
    out["sessionUri"] = value["session_uri"]
    return out


def deserialize_json(data: dict) -> CompleteResourceTokenAuthRequest:
    out: CompleteResourceTokenAuthRequest = {}  # type: ignore[typeddict-item]
    if data.get("userIdentifier") is not None:
        import capo_bedrock_agentcore.types.user_identifier

        out["user_identifier"] = (
            capo_bedrock_agentcore.types.user_identifier.deserialize_json(
                data["userIdentifier"]
            )
        )
    else:
        out["user_identifier"] = {"$unknown": {"name": ""}}
    if data.get("sessionUri") is not None:
        out["session_uri"] = data["sessionUri"]
    else:
        out["session_uri"] = ""
    return out


def redact_sensitive(value: CompleteResourceTokenAuthRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_identifier" in value:
        import capo_bedrock_agentcore.types.user_identifier

        out["user_identifier"] = (
            capo_bedrock_agentcore.types.user_identifier.redact_sensitive(
                value["user_identifier"]
            )
        )
    return out
