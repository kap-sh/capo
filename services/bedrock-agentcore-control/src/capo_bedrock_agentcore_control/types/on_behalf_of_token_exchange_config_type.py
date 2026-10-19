"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnBehalfOfTokenExchangeConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type
    import capo_bedrock_agentcore_control.types.token_exchange_grant_type_config_type


class OnBehalfOfTokenExchangeConfigType(TypedDict, closed=True):
    grant_type: "capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.OnBehalfOfTokenExchangeGrantTypeType"
    """<p>The grant type for the on-behalf-of token exchange.</p>"""
    token_exchange_grant_type_config: NotRequired[
        "capo_bedrock_agentcore_control.types.token_exchange_grant_type_config_type.TokenExchangeGrantTypeConfigType"
    ]
    """<p>Configuration specific to the TOKEN_EXCHANGE grant type (RFC 8693).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnBehalfOfTokenExchangeConfigType) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type

    out["grantType"] = (
        capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.serialize_json(
            value["grant_type"]
        )
    )
    if "token_exchange_grant_type_config" in value:
        import capo_bedrock_agentcore_control.types.token_exchange_grant_type_config_type

        out["tokenExchangeGrantTypeConfig"] = (
            capo_bedrock_agentcore_control.types.token_exchange_grant_type_config_type.serialize_json(
                value["token_exchange_grant_type_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> OnBehalfOfTokenExchangeConfigType:
    out: OnBehalfOfTokenExchangeConfigType = {}  # type: ignore[typeddict-item]
    if data.get("grantType") is not None:
        import capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type

        out["grant_type"] = (
            capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.deserialize_json(
                data["grantType"]
            )
        )
    else:
        import typing

        out["grant_type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.on_behalf_of_token_exchange_grant_type_type.OnBehalfOfTokenExchangeGrantTypeType",
            "",
        )
    if data.get("tokenExchangeGrantTypeConfig") is not None:
        import capo_bedrock_agentcore_control.types.token_exchange_grant_type_config_type

        out["token_exchange_grant_type_config"] = (
            capo_bedrock_agentcore_control.types.token_exchange_grant_type_config_type.deserialize_json(
                data["tokenExchangeGrantTypeConfig"]
            )
        )
    return out
