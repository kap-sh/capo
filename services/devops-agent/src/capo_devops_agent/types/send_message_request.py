"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.asset_id_list
    import capo_devops_agent.types.chat_execution_id
    import capo_devops_agent.types.message_content
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.send_message_context


class SendMessageRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The agent space identifier</p>"""
    execution_id: "capo_devops_agent.types.chat_execution_id.ChatExecutionId"
    """<p>The execution identifier for the chat session</p>"""
    content: "capo_devops_agent.types.message_content.MessageContent"
    """<p>The user message content</p>"""
    context: NotRequired[
        "capo_devops_agent.types.send_message_context.SendMessageContext"
    ]
    """<p>Optional context for the message</p>"""
    user_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>User identifier. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>"""
    asset_ids: NotRequired["capo_devops_agent.types.asset_id_list.AssetIdList"]
    """<p>Optional list of asset identifiers to attach to the message</p>"""
    model_tier: NotRequired["str"]
    """<p>Optional model tier selection. Valid values: smart, balanced, fast. Absent or unrecognized values default to balanced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageRequest) -> dict:
    out: dict = {}
    out["executionId"] = value["execution_id"]
    out["content"] = value["content"]
    if "context" in value:
        import capo_devops_agent.types.send_message_context

        out["context"] = capo_devops_agent.types.send_message_context.serialize_json(
            value["context"]
        )
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "asset_ids" in value:
        import capo_devops_agent.types.asset_id_list

        out["assetIds"] = capo_devops_agent.types.asset_id_list.serialize_json(
            value["asset_ids"]
        )
    if "model_tier" in value:
        out["modelTier"] = value["model_tier"]
    return out


def deserialize_json(data: dict) -> SendMessageRequest:
    out: SendMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("executionId") is not None:
        out["execution_id"] = data["executionId"]
    else:
        out["execution_id"] = ""
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("context") is not None:
        import capo_devops_agent.types.send_message_context

        out["context"] = capo_devops_agent.types.send_message_context.deserialize_json(
            data["context"]
        )
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("assetIds") is not None:
        import capo_devops_agent.types.asset_id_list

        out["asset_ids"] = capo_devops_agent.types.asset_id_list.deserialize_json(
            data["assetIds"]
        )
    if data.get("modelTier") is not None:
        out["model_tier"] = data["modelTier"]
    return out
