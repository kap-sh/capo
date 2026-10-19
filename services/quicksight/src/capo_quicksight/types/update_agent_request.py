"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.agent_description
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_name
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.custom_prompt_input
    import capo_quicksight.types.icon_id
    import capo_quicksight.types.starter_prompt_list
    import capo_quicksight.types.update_agent_request_action_connectors_to_add_list
    import capo_quicksight.types.update_agent_request_action_connectors_to_remove_list
    import capo_quicksight.types.update_agent_request_spaces_to_add_list
    import capo_quicksight.types.update_agent_request_spaces_to_remove_list
    import capo_quicksight.types.welcome_message


class UpdateAgentRequest(TypedDict, closed=True):
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent to update.</p>"""
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agent.</p>"""
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
    custom_prompt_input: NotRequired[
        "capo_quicksight.types.custom_prompt_input.CustomPromptInput"
    ]
    """<p>The custom prompt configuration for the agent.</p>"""
    spaces_to_add: NotRequired[
        "capo_quicksight.types.update_agent_request_spaces_to_add_list.UpdateAgentRequestSpacesToAddList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the spaces to attach to the agent.</p>"""
    spaces_to_remove: NotRequired[
        "capo_quicksight.types.update_agent_request_spaces_to_remove_list.UpdateAgentRequestSpacesToRemoveList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the spaces to detach from the agent.</p>"""
    action_connectors_to_add: NotRequired[
        "capo_quicksight.types.update_agent_request_action_connectors_to_add_list.UpdateAgentRequestActionConnectorsToAddList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors to attach to the agent.</p>"""
    action_connectors_to_remove: NotRequired[
        "capo_quicksight.types.update_agent_request_action_connectors_to_remove_list.UpdateAgentRequestActionConnectorsToRemoveList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors to detach from the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequest) -> dict:
    out: dict = {}
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
    if "custom_prompt_input" in value:
        import capo_quicksight.types.custom_prompt_input

        out["CustomPromptInput"] = (
            capo_quicksight.types.custom_prompt_input.serialize_json(
                value["custom_prompt_input"]
            )
        )
    if "spaces_to_add" in value:
        import capo_quicksight.types.update_agent_request_spaces_to_add_list

        out["SpacesToAdd"] = (
            capo_quicksight.types.update_agent_request_spaces_to_add_list.serialize_json(
                value["spaces_to_add"]
            )
        )
    if "spaces_to_remove" in value:
        import capo_quicksight.types.update_agent_request_spaces_to_remove_list

        out["SpacesToRemove"] = (
            capo_quicksight.types.update_agent_request_spaces_to_remove_list.serialize_json(
                value["spaces_to_remove"]
            )
        )
    if "action_connectors_to_add" in value:
        import capo_quicksight.types.update_agent_request_action_connectors_to_add_list

        out["ActionConnectorsToAdd"] = (
            capo_quicksight.types.update_agent_request_action_connectors_to_add_list.serialize_json(
                value["action_connectors_to_add"]
            )
        )
    if "action_connectors_to_remove" in value:
        import capo_quicksight.types.update_agent_request_action_connectors_to_remove_list

        out["ActionConnectorsToRemove"] = (
            capo_quicksight.types.update_agent_request_action_connectors_to_remove_list.serialize_json(
                value["action_connectors_to_remove"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentRequest:
    out: UpdateAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
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
    if data.get("CustomPromptInput") is not None:
        import capo_quicksight.types.custom_prompt_input

        out["custom_prompt_input"] = (
            capo_quicksight.types.custom_prompt_input.deserialize_json(
                data["CustomPromptInput"]
            )
        )
    if data.get("SpacesToAdd") is not None:
        import capo_quicksight.types.update_agent_request_spaces_to_add_list

        out["spaces_to_add"] = (
            capo_quicksight.types.update_agent_request_spaces_to_add_list.deserialize_json(
                data["SpacesToAdd"]
            )
        )
    if data.get("SpacesToRemove") is not None:
        import capo_quicksight.types.update_agent_request_spaces_to_remove_list

        out["spaces_to_remove"] = (
            capo_quicksight.types.update_agent_request_spaces_to_remove_list.deserialize_json(
                data["SpacesToRemove"]
            )
        )
    if data.get("ActionConnectorsToAdd") is not None:
        import capo_quicksight.types.update_agent_request_action_connectors_to_add_list

        out["action_connectors_to_add"] = (
            capo_quicksight.types.update_agent_request_action_connectors_to_add_list.deserialize_json(
                data["ActionConnectorsToAdd"]
            )
        )
    if data.get("ActionConnectorsToRemove") is not None:
        import capo_quicksight.types.update_agent_request_action_connectors_to_remove_list

        out["action_connectors_to_remove"] = (
            capo_quicksight.types.update_agent_request_action_connectors_to_remove_list.deserialize_json(
                data["ActionConnectorsToRemove"]
            )
        )
    return out


def redact_sensitive(value: UpdateAgentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "starter_prompts" in value:
        out["starter_prompts"] = "*** Sensitive Data Redacted ***"
    if "welcome_message" in value:
        out["welcome_message"] = "*** Sensitive Data Redacted ***"
    if "custom_prompt_input" in value:
        out["custom_prompt_input"] = "*** Sensitive Data Redacted ***"
    return out
