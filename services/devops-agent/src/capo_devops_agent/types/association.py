"""Generated from Smithy shape ``com.amazonaws.devopsagent#Association``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.association_capabilities
    import capo_devops_agent.types.association_id
    import capo_devops_agent.types.service_configuration
    import capo_devops_agent.types.service_id
    import capo_devops_agent.types.validation_status


class Association(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the resource was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the resource was last updated.</p>"""
    status: NotRequired["capo_devops_agent.types.validation_status.ValidationStatus"]
    """<p>Validation status</p>"""
    association_id: "capo_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""
    service_id: "capo_devops_agent.types.service_id.ServiceId"
    """<p>The identifier for associated service</p>"""
    configuration: "capo_devops_agent.types.service_configuration.ServiceConfiguration"
    """<p>The configuration that directs how AgentSpace interacts with the given service.</p>"""
    capabilities: NotRequired[
        "capo_devops_agent.types.association_capabilities.AssociationCapabilities"
    ]
    """<p>Enabled capabilities for this association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Association) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import capo_devops_agent._protocol.serialize

    out["createdAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_devops_agent._protocol.serialize

    out["updatedAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    if "status" in value:
        import capo_devops_agent.types.validation_status

        out["status"] = capo_devops_agent.types.validation_status.serialize_json(
            value["status"]
        )
    out["associationId"] = value["association_id"]
    out["serviceId"] = value["service_id"]
    import capo_devops_agent.types.service_configuration

    out["configuration"] = capo_devops_agent.types.service_configuration.serialize_json(
        value["configuration"]
    )
    if "capabilities" in value:
        import capo_devops_agent.types.association_capabilities

        out["capabilities"] = (
            capo_devops_agent.types.association_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("Association.agent_space_id required")
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("Association.created_at required")
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError("Association.updated_at required")
    if data.get("status") is not None:
        import capo_devops_agent.types.validation_status

        out["status"] = capo_devops_agent.types.validation_status.deserialize_json(
            data["status"]
        )
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    else:
        raise DeserializationError("Association.association_id required")
    if data.get("serviceId") is not None:
        out["service_id"] = data["serviceId"]
    else:
        raise DeserializationError("Association.service_id required")
    if data.get("configuration") is not None:
        import capo_devops_agent.types.service_configuration

        out["configuration"] = (
            capo_devops_agent.types.service_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError("Association.configuration required")
    if data.get("capabilities") is not None:
        import capo_devops_agent.types.association_capabilities

        out["capabilities"] = (
            capo_devops_agent.types.association_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    return out


def redact_sensitive(value: Association) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_devops_agent.types.service_configuration

        out["configuration"] = (
            capo_devops_agent.types.service_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
