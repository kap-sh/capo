"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAssociationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.association_capabilities
    import capo_devops_agent.types.association_id
    import capo_devops_agent.types.service_configuration


class UpdateAssociationInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    association_id: "capo_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""
    configuration: "capo_devops_agent.types.service_configuration.ServiceConfiguration"
    """<p>The configuration that directs how AgentSpace interacts with the given service. The entire configuration is replaced on update.</p>"""
    capabilities: NotRequired[
        "capo_devops_agent.types.association_capabilities.AssociationCapabilities"
    ]
    """<p>Enabled capabilities for this association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssociationInput) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> UpdateAssociationInput:
    out: UpdateAssociationInput = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_devops_agent.types.service_configuration

        out["configuration"] = (
            capo_devops_agent.types.service_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_devops_agent.types._unknown

        out["configuration"] = capo_devops_agent.types._unknown.UnknownUnionMember("")
    if data.get("capabilities") is not None:
        import capo_devops_agent.types.association_capabilities

        out["capabilities"] = (
            capo_devops_agent.types.association_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    return out


def redact_sensitive(value: UpdateAssociationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_devops_agent.types.service_configuration

        out["configuration"] = (
            capo_devops_agent.types.service_configuration.redact_sensitive(
                value["configuration"]
            )
        )
    return out
