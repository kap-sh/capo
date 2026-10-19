"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_core_memory_id
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_persistence_mode
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config_list
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_session_binding


class AgenticRetrieveMemoryConfiguration(TypedDict, closed=True):
    memory_id: "capo_bedrock_agent_runtime.types.agent_core_memory_id.AgentCoreMemoryId"
    """<p>The identifier of the AgentCore Memory resource to use. The resource must exist in your account and be in the ACTIVE state.</p>"""
    session_binding: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_session_binding.AgenticRetrieveMemorySessionBinding"
    ]
    """<p>The short-term memory session whose history is restored for this retrieval. To persist the agent-generated answer to the session, omit persistenceMode or set it to DEFAULT. To leave the session unchanged, set persistenceMode to NONE. Supply session history through the existing messages parameter or through short-term memory, but not both.</p>"""
    retrieval_configs: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config_list.AgenticRetrieveMemoryRetrievalConfigList"
    ]
    """<p>Specifies the long-term memory configuration the agent can retrieve from. The agent decides whether to retrieve and composes its own query. This field currently accepts at most one entry.</p>"""
    persistence_mode: NotRequired[
        "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_persistence_mode.AgenticRetrieveMemoryPersistenceMode"
    ]
    """<p>Specifies whether the agent-generated answer is written back to the given short-term memory session, and applies only when sessionBinding is set. Valid values:</p> <ul> <li> <p> <code>DEFAULT</code> (default) – Specifies that the question and the agent-generated answer are persisted to the session as a single event. This value requires generateResponse to be true.</p> </li> <li> <p> <code>NONE</code> – Specifies that the session is left unchanged.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryConfiguration) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    if "session_binding" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_session_binding

        out["sessionBinding"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_session_binding.serialize_json(
                value["session_binding"]
            )
        )
    if "retrieval_configs" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config_list

        out["retrievalConfigs"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config_list.serialize_json(
                value["retrieval_configs"]
            )
        )
    if "persistence_mode" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_persistence_mode

        out["persistenceMode"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_persistence_mode.serialize_json(
                value["persistence_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMemoryConfiguration:
    out: AgenticRetrieveMemoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    if data.get("sessionBinding") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_session_binding

        out["session_binding"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_session_binding.deserialize_json(
                data["sessionBinding"]
            )
        )
    if data.get("retrievalConfigs") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config_list

        out["retrieval_configs"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_retrieval_config_list.deserialize_json(
                data["retrievalConfigs"]
            )
        )
    if data.get("persistenceMode") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_persistence_mode

        out["persistence_mode"] = (
            capo_bedrock_agent_runtime.types.agentic_retrieve_memory_persistence_mode.deserialize_json(
                data["persistenceMode"]
            )
        )
    return out
