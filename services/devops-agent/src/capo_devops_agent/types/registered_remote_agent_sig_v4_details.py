"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredRemoteAgentSigV4Details``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.description
    import capo_devops_agent.types.remote_agent_endpoint
    import capo_devops_agent.types.remote_agent_name
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.sig_v4_region


class RegisteredRemoteAgentSigV4Details(TypedDict, closed=True):
    name: "capo_devops_agent.types.remote_agent_name.RemoteAgentName"
    endpoint: "capo_devops_agent.types.remote_agent_endpoint.RemoteAgentEndpoint"
    description: NotRequired["capo_devops_agent.types.description.Description"]
    region: "capo_devops_agent.types.sig_v4_region.SigV4Region"
    service: "str"
    """<p>The AWS service name for SigV4 signing.</p>"""
    role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredRemoteAgentSigV4Details) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["endpoint"] = value["endpoint"]
    if "description" in value:
        out["description"] = value["description"]
    out["region"] = value["region"]
    out["service"] = value["service"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> RegisteredRemoteAgentSigV4Details:
    out: RegisteredRemoteAgentSigV4Details = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegisteredRemoteAgentSigV4Details.name required")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError(
            "RegisteredRemoteAgentSigV4Details.endpoint required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        raise DeserializationError("RegisteredRemoteAgentSigV4Details.region required")
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        raise DeserializationError("RegisteredRemoteAgentSigV4Details.service required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out


def redact_sensitive(value: RegisteredRemoteAgentSigV4Details) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
