"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnBehalfOfAuthenticationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method


class OnBehalfOfAuthenticationConfig(TypedDict, closed=True):
    client_authentication_method: "capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method.OnBehalfOfClientAuthenticationMethod"
    """<p>The client authentication method to use during the on-behalf-of token exchange. The <code>NO_CLIENT</code> option omits the <code>clientId</code> and <code>clientSecret</code> during the on-behalf-of token exchange with the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OnBehalfOfAuthenticationConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method

    out["clientAuthenticationMethod"] = (
        capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method.serialize_json(
            value["client_authentication_method"]
        )
    )
    return out


def deserialize_json(data: dict) -> OnBehalfOfAuthenticationConfig:
    out: OnBehalfOfAuthenticationConfig = {}  # type: ignore[typeddict-item]
    if data.get("clientAuthenticationMethod") is not None:
        import capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method

        out["client_authentication_method"] = (
            capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method.deserialize_json(
                data["clientAuthenticationMethod"]
            )
        )
    else:
        import typing

        out["client_authentication_method"] = typing.cast(
            "capo_bedrock_agentcore_control.types.on_behalf_of_client_authentication_method.OnBehalfOfClientAuthenticationMethod",
            "",
        )
    return out
