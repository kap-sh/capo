"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TokenExchangeGrantTypeConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.actor_token_content_type
    import capo_bedrock_agentcore_control.types.scopes_list_type


class TokenExchangeGrantTypeConfigType(TypedDict, closed=True):
    actor_token_content: "capo_bedrock_agentcore_control.types.actor_token_content_type.ActorTokenContentType"
    """<p>The content type for the actor token in the token exchange.</p>"""
    actor_token_scopes: NotRequired[
        "capo_bedrock_agentcore_control.types.scopes_list_type.ScopesListType"
    ]
    """<p>The scopes for the actor token. Only valid when actorTokenContent is M2M.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenExchangeGrantTypeConfigType) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.actor_token_content_type

    out["actorTokenContent"] = (
        capo_bedrock_agentcore_control.types.actor_token_content_type.serialize_json(
            value["actor_token_content"]
        )
    )
    if "actor_token_scopes" in value:
        import capo_bedrock_agentcore_control.types.scopes_list_type

        out["actorTokenScopes"] = (
            capo_bedrock_agentcore_control.types.scopes_list_type.serialize_json(
                value["actor_token_scopes"]
            )
        )
    return out


def deserialize_json(data: dict) -> TokenExchangeGrantTypeConfigType:
    out: TokenExchangeGrantTypeConfigType = {}  # type: ignore[typeddict-item]
    if data.get("actorTokenContent") is not None:
        import capo_bedrock_agentcore_control.types.actor_token_content_type

        out["actor_token_content"] = (
            capo_bedrock_agentcore_control.types.actor_token_content_type.deserialize_json(
                data["actorTokenContent"]
            )
        )
    else:
        import typing

        out["actor_token_content"] = typing.cast(
            "capo_bedrock_agentcore_control.types.actor_token_content_type.ActorTokenContentType",
            "",
        )
    if data.get("actorTokenScopes") is not None:
        import capo_bedrock_agentcore_control.types.scopes_list_type

        out["actor_token_scopes"] = (
            capo_bedrock_agentcore_control.types.scopes_list_type.deserialize_json(
                data["actorTokenScopes"]
            )
        )
    return out
