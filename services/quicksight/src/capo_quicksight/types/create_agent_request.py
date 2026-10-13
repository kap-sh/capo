"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAgentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.agent_description
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_lifecycle
    import capo_quicksight.types.agent_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.create_agent_request_action_connectors_list
    import capo_quicksight.types.create_agent_request_spaces_list
    import capo_quicksight.types.custom_prompt_input
    import capo_quicksight.types.icon_id
    import capo_quicksight.types.starter_prompt_list
    import capo_quicksight.types.welcome_message


class CreateAgentRequest(TypedDict, closed=True):
    spaces: NotRequired[
        "capo_quicksight.types.create_agent_request_spaces_list.CreateAgentRequestSpacesList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the spaces to attach to the agent.</p>"""
    action_connectors: NotRequired[
        "capo_quicksight.types.create_agent_request_action_connectors_list.CreateAgentRequestActionConnectorsList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors to attach to the agent.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>A unique identifier for the agent.</p>"""
    name: "capo_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    description: NotRequired["capo_quicksight.types.agent_description.AgentDescription"]
    """<p>A description of the agent.</p>"""
    icon_id: NotRequired["capo_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""
    starter_prompts: NotRequired[
        "capo_quicksight.types.starter_prompt_list.StarterPromptList"
    ]
    """<p>A list of starter prompts that are displayed to users when they begin interacting with the agent.</p>"""
    welcome_message: NotRequired["capo_quicksight.types.welcome_message.WelcomeMessage"]
    """<p>The welcome message that is displayed when a user starts a conversation with the agent.</p>"""
    agent_lifecycle: NotRequired["capo_quicksight.types.agent_lifecycle.AgentLifecycle"]
    """<p>The lifecycle state of the agent. Valid values are <code>PREVIEW</code> and <code>PUBLISHED</code>.</p>"""
    custom_prompt_input: NotRequired[
        "capo_quicksight.types.custom_prompt_input.CustomPromptInput"
    ]
    """<p>The custom prompt configuration for the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentRequest) -> dict:
    out: dict = {}
    if "spaces" in value:
        import capo_quicksight.types.create_agent_request_spaces_list

        out["Spaces"] = (
            capo_quicksight.types.create_agent_request_spaces_list.serialize_json(
                value["spaces"]
            )
        )
    if "action_connectors" in value:
        import capo_quicksight.types.create_agent_request_action_connectors_list

        out["ActionConnectors"] = (
            capo_quicksight.types.create_agent_request_action_connectors_list.serialize_json(
                value["action_connectors"]
            )
        )
    out["AgentId"] = value["agent_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_id" in value:
        out["IconId"] = value["icon_id"]
    if "starter_prompts" in value:
        import capo_quicksight.types.starter_prompt_list

        out["StarterPrompts"] = (
            capo_quicksight.types.starter_prompt_list.serialize_json(
                value["starter_prompts"]
            )
        )
    if "welcome_message" in value:
        out["WelcomeMessage"] = value["welcome_message"]
    if "agent_lifecycle" in value:
        import capo_quicksight.types.agent_lifecycle

        out["AgentLifecycle"] = capo_quicksight.types.agent_lifecycle.serialize_json(
            value["agent_lifecycle"]
        )
    if "custom_prompt_input" in value:
        import capo_quicksight.types.custom_prompt_input

        out["CustomPromptInput"] = (
            capo_quicksight.types.custom_prompt_input.serialize_json(
                value["custom_prompt_input"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAgentRequest:
    out: CreateAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Spaces") is not None:
        import capo_quicksight.types.create_agent_request_spaces_list

        out["spaces"] = (
            capo_quicksight.types.create_agent_request_spaces_list.deserialize_json(
                data["Spaces"]
            )
        )
    if data.get("ActionConnectors") is not None:
        import capo_quicksight.types.create_agent_request_action_connectors_list

        out["action_connectors"] = (
            capo_quicksight.types.create_agent_request_action_connectors_list.deserialize_json(
                data["ActionConnectors"]
            )
        )
    if data.get("AgentId") is not None:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("CreateAgentRequest.agent_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAgentRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IconId") is not None:
        out["icon_id"] = data["IconId"]
    if data.get("StarterPrompts") is not None:
        import capo_quicksight.types.starter_prompt_list

        out["starter_prompts"] = (
            capo_quicksight.types.starter_prompt_list.deserialize_json(
                data["StarterPrompts"]
            )
        )
    if data.get("WelcomeMessage") is not None:
        out["welcome_message"] = data["WelcomeMessage"]
    if data.get("AgentLifecycle") is not None:
        import capo_quicksight.types.agent_lifecycle

        out["agent_lifecycle"] = capo_quicksight.types.agent_lifecycle.deserialize_json(
            data["AgentLifecycle"]
        )
    if data.get("CustomPromptInput") is not None:
        import capo_quicksight.types.custom_prompt_input

        out["custom_prompt_input"] = (
            capo_quicksight.types.custom_prompt_input.deserialize_json(
                data["CustomPromptInput"]
            )
        )
    return out


def redact_sensitive(value: CreateAgentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "starter_prompts" in value:
        out["starter_prompts"] = "*** Sensitive Data Redacted ***"
    if "welcome_message" in value:
        out["welcome_message"] = "*** Sensitive Data Redacted ***"
    if "custom_prompt_input" in value:
        out["custom_prompt_input"] = "*** Sensitive Data Redacted ***"
    return out
