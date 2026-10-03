"""Generated from Smithy shape ``com.amazonaws.qconnect#SessionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration_map
    import capo_qconnect.types.arn
    import capo_qconnect.types.description
    import capo_qconnect.types.name
    import capo_qconnect.types.orchestrator_configuration_list
    import capo_qconnect.types.origin
    import capo_qconnect.types.session_integration_configuration
    import capo_qconnect.types.tag_filter
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid


class SessionData(TypedDict, closed=True):
    session_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    name: "capo_qconnect.types.name.Name"
    """<p>The name of the session.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the session.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    integration_configuration: NotRequired[
        "capo_qconnect.types.session_integration_configuration.SessionIntegrationConfiguration"
    ]
    """<p>The configuration information for the session integration.</p>"""
    tag_filter: NotRequired["capo_qconnect.types.tag_filter.TagFilter"]
    """<p>An object that can be used to specify Tag conditions.</p>"""
    ai_agent_configuration: NotRequired[
        "capo_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
    ]
    """<p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.</p>"""
    origin: NotRequired["capo_qconnect.types.origin.Origin"]
    """<p>The origin of the Session to be listed. <code>SYSTEM</code> for a default Session created by Amazon Q in Connect or <code>CUSTOMER</code> for a Session created by calling <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateSession.html">CreateSession</a> API.</p>"""
    orchestrator_configuration_list: NotRequired[
        "capo_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
    ]
    """<p>The list of orchestrator configurations for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionData) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["sessionId"] = value["session_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    if "integration_configuration" in value:
        import capo_qconnect.types.session_integration_configuration

        out["integrationConfiguration"] = (
            capo_qconnect.types.session_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    if "tag_filter" in value:
        import capo_qconnect.types.tag_filter

        out["tagFilter"] = capo_qconnect.types.tag_filter.serialize_json(
            value["tag_filter"]
        )
    if "ai_agent_configuration" in value:
        import capo_qconnect.types.ai_agent_configuration_map

        out["aiAgentConfiguration"] = (
            capo_qconnect.types.ai_agent_configuration_map.serialize_json(
                value["ai_agent_configuration"]
            )
        )
    if "origin" in value:
        out["origin"] = value["origin"]
    if "orchestrator_configuration_list" in value:
        import capo_qconnect.types.orchestrator_configuration_list

        out["orchestratorConfigurationList"] = (
            capo_qconnect.types.orchestrator_configuration_list.serialize_json(
                value["orchestrator_configuration_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionData:
    out: SessionData = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("SessionData.session_arn required")
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionData.session_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SessionData.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    if data.get("integrationConfiguration") is not None:
        import capo_qconnect.types.session_integration_configuration

        out["integration_configuration"] = (
            capo_qconnect.types.session_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    if data.get("tagFilter") is not None:
        import capo_qconnect.types.tag_filter

        out["tag_filter"] = capo_qconnect.types.tag_filter.deserialize_json(
            data["tagFilter"]
        )
    if data.get("aiAgentConfiguration") is not None:
        import capo_qconnect.types.ai_agent_configuration_map

        out["ai_agent_configuration"] = (
            capo_qconnect.types.ai_agent_configuration_map.deserialize_json(
                data["aiAgentConfiguration"]
            )
        )
    if data.get("origin") is not None:
        out["origin"] = data["origin"]
    if data.get("orchestratorConfigurationList") is not None:
        import capo_qconnect.types.orchestrator_configuration_list

        out["orchestrator_configuration_list"] = (
            capo_qconnect.types.orchestrator_configuration_list.deserialize_json(
                data["orchestratorConfigurationList"]
            )
        )
    return out
