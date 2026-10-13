"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessGatewayOutboundAuth``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.o_auth_credential_provider


class _HarnessGatewayOutboundAuth_awsIam(TypedDict, closed=True):
    awsIam: "None"


class _HarnessGatewayOutboundAuth_none(TypedDict, closed=True):
    none: "None"


class _HarnessGatewayOutboundAuth_oauth(TypedDict, closed=True):
    oauth: "capo_bedrock_agentcore_control.types.o_auth_credential_provider.OAuthCredentialProvider"


HarnessGatewayOutboundAuth: TypeAlias = (
    _HarnessGatewayOutboundAuth_awsIam
    | _HarnessGatewayOutboundAuth_none
    | _HarnessGatewayOutboundAuth_oauth
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessGatewayOutboundAuth) -> dict:
    if "awsIam" in value:
        return {"awsIam": {}}
    elif "none" in value:
        return {"none": {}}
    elif "oauth" in value:
        import capo_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauth": capo_bedrock_agentcore_control.types.o_auth_credential_provider.serialize_json(
                value["oauth"]
            )
        }
    else:
        raise SerializationError("HarnessGatewayOutboundAuth: no variant present")


def deserialize_json(data: dict) -> HarnessGatewayOutboundAuth:
    if data.get("awsIam") is not None:
        return {"awsIam": None}
    elif data.get("none") is not None:
        return {"none": None}
    elif data.get("oauth") is not None:
        import capo_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauth": capo_bedrock_agentcore_control.types.o_auth_credential_provider.deserialize_json(
                data["oauth"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessGatewayOutboundAuth: no recognized variant key"
        )


def redact_sensitive(value: HarnessGatewayOutboundAuth) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oauth" in value:
        import capo_bedrock_agentcore_control.types.o_auth_credential_provider

        out["oauth"] = (
            capo_bedrock_agentcore_control.types.o_auth_credential_provider.redact_sensitive(
                value["oauth"]
            )
        )
    return out
