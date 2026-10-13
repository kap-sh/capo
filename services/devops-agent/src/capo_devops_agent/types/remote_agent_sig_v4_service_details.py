"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentSigV4ServiceDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.remote_agent_endpoint
    import capo_devops_agent.types.remote_agent_name
    import capo_devops_agent.types.remote_agent_sig_v4_authorization_config


class RemoteAgentSigV4ServiceDetails(TypedDict, closed=True):
    name: "capo_devops_agent.types.remote_agent_name.RemoteAgentName"
    endpoint: "capo_devops_agent.types.remote_agent_endpoint.RemoteAgentEndpoint"
    description: NotRequired["capo_devops_agent.types.description.Description"]
    authorization_config: "capo_devops_agent.types.remote_agent_sig_v4_authorization_config.RemoteAgentSigV4AuthorizationConfig"
    """<p>Remote agent SigV4 authorization configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentSigV4ServiceDetails) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_devops_agent.types.remote_agent_sig_v4_authorization_config

    out["authorizationConfig"] = (
        capo_devops_agent.types.remote_agent_sig_v4_authorization_config.serialize_json(
            value["authorization_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> RemoteAgentSigV4ServiceDetails:
    out: RemoteAgentSigV4ServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RemoteAgentSigV4ServiceDetails.name required")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RemoteAgentSigV4ServiceDetails.endpoint required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authorizationConfig") is not None:
        import capo_devops_agent.types.remote_agent_sig_v4_authorization_config

        out["authorization_config"] = (
            capo_devops_agent.types.remote_agent_sig_v4_authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "RemoteAgentSigV4ServiceDetails.authorization_config required"
        )
    return out


def redact_sensitive(value: RemoteAgentSigV4ServiceDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
