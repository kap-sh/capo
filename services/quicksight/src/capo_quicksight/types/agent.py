"""Generated from Smithy shape ``com.amazonaws.quicksight#Agent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.agent_action_connectors_list
    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_description
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_lifecycle
    import capo_quicksight.types.agent_name
    import capo_quicksight.types.agent_spaces_list
    import capo_quicksight.types.agent_status
    import capo_quicksight.types.custom_prompt_interface
    import capo_quicksight.types.icon_id
    import capo_quicksight.types.starter_prompt_list
    import capo_quicksight.types.welcome_message


class Agent(TypedDict, closed=True):
    spaces: NotRequired["capo_quicksight.types.agent_spaces_list.AgentSpacesList"]
    """<p>The Amazon Resource Names (ARNs) of the spaces attached to the agent.</p>"""
    action_connectors: NotRequired[
        "capo_quicksight.types.agent_action_connectors_list.AgentActionConnectorsList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors attached to the agent.</p>"""
    description: NotRequired["capo_quicksight.types.agent_description.AgentDescription"]
    """<p>A description of the agent.</p>"""
    icon_id: NotRequired["capo_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""
    name: "capo_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    starter_prompts: NotRequired[
        "capo_quicksight.types.starter_prompt_list.StarterPromptList"
    ]
    """<p>A list of starter prompts that are displayed to users when they begin interacting with the agent.</p>"""
    welcome_message: NotRequired["capo_quicksight.types.welcome_message.WelcomeMessage"]
    """<p>The welcome message that is displayed when a user starts a conversation with the agent.</p>"""
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    agent_lifecycle: "capo_quicksight.types.agent_lifecycle.AgentLifecycle"
    """<p>The lifecycle state of the agent. Valid values are <code>PREVIEW</code> and <code>PUBLISHED</code>.</p>"""
    agent_status: "capo_quicksight.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the agent was created.</p>"""
    creator: "str"
    """<p>The identity of the user who created the agent.</p>"""
    custom_prompt_interface: NotRequired[
        "capo_quicksight.types.custom_prompt_interface.CustomPromptInterface"
    ]
    """<p>The custom prompt interface configuration for the agent.</p>"""
    error_message: NotRequired["str"]
    """<p>An error message associated with the agent, if applicable.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time that the agent was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Agent) -> dict:
    out: dict = {}
    if "spaces" in value:
        import capo_quicksight.types.agent_spaces_list

        out["Spaces"] = capo_quicksight.types.agent_spaces_list.serialize_json(
            value["spaces"]
        )
    if "action_connectors" in value:
        import capo_quicksight.types.agent_action_connectors_list

        out["ActionConnectors"] = (
            capo_quicksight.types.agent_action_connectors_list.serialize_json(
                value["action_connectors"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_id" in value:
        out["IconId"] = value["icon_id"]
    out["Name"] = value["name"]
    if "starter_prompts" in value:
        import capo_quicksight.types.starter_prompt_list

        out["StarterPrompts"] = (
            capo_quicksight.types.starter_prompt_list.serialize_json(
                value["starter_prompts"]
            )
        )
    if "welcome_message" in value:
        out["WelcomeMessage"] = value["welcome_message"]
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import capo_quicksight.types.agent_lifecycle

    out["AgentLifecycle"] = capo_quicksight.types.agent_lifecycle.serialize_json(
        value["agent_lifecycle"]
    )
    import capo_quicksight.types.agent_status

    out["AgentStatus"] = capo_quicksight.types.agent_status.serialize_json(
        value["agent_status"]
    )
    import capo_quicksight.types._prelude.timestamp

    out["CreatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    out["Creator"] = value["creator"]
    if "custom_prompt_interface" in value:
        import capo_quicksight.types.custom_prompt_interface

        out["CustomPromptInterface"] = (
            capo_quicksight.types.custom_prompt_interface.serialize_json(
                value["custom_prompt_interface"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    import capo_quicksight.types._prelude.timestamp

    out["UpdatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> Agent:
    out: Agent = {}  # type: ignore[typeddict-item]
    if data.get("Spaces") is not None:
        import capo_quicksight.types.agent_spaces_list

        out["spaces"] = capo_quicksight.types.agent_spaces_list.deserialize_json(
            data["Spaces"]
        )
    if data.get("ActionConnectors") is not None:
        import capo_quicksight.types.agent_action_connectors_list

        out["action_connectors"] = (
            capo_quicksight.types.agent_action_connectors_list.deserialize_json(
                data["ActionConnectors"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IconId") is not None:
        out["icon_id"] = data["IconId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("StarterPrompts") is not None:
        import capo_quicksight.types.starter_prompt_list

        out["starter_prompts"] = (
            capo_quicksight.types.starter_prompt_list.deserialize_json(
                data["StarterPrompts"]
            )
        )
    if data.get("WelcomeMessage") is not None:
        out["welcome_message"] = data["WelcomeMessage"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AgentId") is not None:
        out["agent_id"] = data["AgentId"]
    else:
        out["agent_id"] = ""
    if data.get("AgentLifecycle") is not None:
        import capo_quicksight.types.agent_lifecycle

        out["agent_lifecycle"] = capo_quicksight.types.agent_lifecycle.deserialize_json(
            data["AgentLifecycle"]
        )
    else:
        import typing

        out["agent_lifecycle"] = typing.cast(
            "capo_quicksight.types.agent_lifecycle.AgentLifecycle", ""
        )
    if data.get("AgentStatus") is not None:
        import capo_quicksight.types.agent_status

        out["agent_status"] = capo_quicksight.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    else:
        import typing

        out["agent_status"] = typing.cast(
            "capo_quicksight.types.agent_status.AgentStatus", ""
        )
    if data.get("CreatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["created_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Creator") is not None:
        out["creator"] = data["Creator"]
    else:
        out["creator"] = ""
    if data.get("CustomPromptInterface") is not None:
        import capo_quicksight.types.custom_prompt_interface

        out["custom_prompt_interface"] = (
            capo_quicksight.types.custom_prompt_interface.deserialize_json(
                data["CustomPromptInterface"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["updated_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: Agent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "starter_prompts" in value:
        out["starter_prompts"] = "*** Sensitive Data Redacted ***"
    if "welcome_message" in value:
        out["welcome_message"] = "*** Sensitive Data Redacted ***"
    if "custom_prompt_interface" in value:
        import capo_quicksight.types.custom_prompt_interface

        out["custom_prompt_interface"] = (
            capo_quicksight.types.custom_prompt_interface.redact_sensitive(
                value["custom_prompt_interface"]
            )
        )
    return out
