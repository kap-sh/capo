"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredRemoteAgentDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.remote_agent_authorization_method
    import capo_devops_agent.types.remote_agent_endpoint
    import capo_devops_agent.types.remote_agent_name


class RegisteredRemoteAgentDetails(TypedDict, closed=True):
    name: "capo_devops_agent.types.remote_agent_name.RemoteAgentName"
    endpoint: "capo_devops_agent.types.remote_agent_endpoint.RemoteAgentEndpoint"
    description: NotRequired["capo_devops_agent.types.description.Description"]
    authorization_method: "capo_devops_agent.types.remote_agent_authorization_method.RemoteAgentAuthorizationMethod"
    """<p>The authorization method used by the remote agent.</p>"""
    api_key_header: NotRequired["str"]
    """<p>If the remote agent uses API key authentication, the header name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredRemoteAgentDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_devops_agent.types.remote_agent_authorization_method

    out["authorizationMethod"] = (
        capo_devops_agent.types.remote_agent_authorization_method.serialize_json(
            value["authorization_method"]
        )
    )
    if "api_key_header" in value:
        out["apiKeyHeader"] = value["api_key_header"]
    return out


def deserialize_json(data: dict) -> RegisteredRemoteAgentDetails:
    out: RegisteredRemoteAgentDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisteredRemoteAgentDetails.name required")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RegisteredRemoteAgentDetails.endpoint required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authorizationMethod") is not None:
        import capo_devops_agent.types.remote_agent_authorization_method

        out["authorization_method"] = (
            capo_devops_agent.types.remote_agent_authorization_method.deserialize_json(
                data["authorizationMethod"]
            )
        )
    else:
        raise DeserializationError(
            "RegisteredRemoteAgentDetails.authorization_method required"
        )
    if data.get("apiKeyHeader") is not None:
        out["api_key_header"] = data["apiKeyHeader"]
    return out


def redact_sensitive(value: RegisteredRemoteAgentDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
