"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerBearerTokenConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.token_value


class MCPServerBearerTokenConfig(TypedDict, closed=True):
    token_name: "str"
    """<p>User friendly bearer token name specified by end user.</p>"""
    token_value: "capo_devops_agent.types.token_value.TokenValue"
    """<p>Bearer token value in alphanumeric for authenticating with the service.</p>"""
    authorization_header: "str"
    """<p>HTTP header name to send the bearer token in requests to the service. Defaults to 'Authorization' per RFC 6750.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerBearerTokenConfig) -> dict:
    out: dict = {}
    out["tokenName"] = value["token_name"]
    out["tokenValue"] = value["token_value"]
    out["authorizationHeader"] = value.get("authorization_header", "Authorization")
    return out


def deserialize_json(data: dict) -> MCPServerBearerTokenConfig:
    out: MCPServerBearerTokenConfig = {}  # type: ignore[typeddict-item]
    if data.get("tokenName") is not None:
        out["token_name"] = data["tokenName"]
    else:
        raise DeserializationError("MCPServerBearerTokenConfig.token_name required")
    if data.get("tokenValue") is not None:
        out["token_value"] = data["tokenValue"]
    else:
        raise DeserializationError("MCPServerBearerTokenConfig.token_value required")
    if data.get("authorizationHeader") is not None:
        out["authorization_header"] = data["authorizationHeader"]
    else:
        out["authorization_header"] = "Authorization"
    return out


def redact_sensitive(value: MCPServerBearerTokenConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token_value" in value:
        out["token_value"] = "*** Sensitive Data Redacted ***"
    return out
