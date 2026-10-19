"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateAgentSpaceInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_name
    import capo_devops_agent.types.agent_space_preferences
    import capo_devops_agent.types.description
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.locale
    import capo_devops_agent.types.tags


class CreateAgentSpaceInput(TypedDict, closed=True):
    name: "capo_devops_agent.types.agent_space_name.AgentSpaceName"
    """<p>The name of the AgentSpace.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>The description of the AgentSpace.</p>"""
    locale: NotRequired["capo_devops_agent.types.locale.Locale"]
    """<p>The locale for the AgentSpace, which determines the language used in agent responses.</p>"""
    kms_key_arn: NotRequired["capo_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    client_token: NotRequired["str"]
    """<p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>"""
    tags: NotRequired["capo_devops_agent.types.tags.Tags"]
    """<p>Tags to add to the AgentSpace at creation time.</p>"""
    preferences: NotRequired[
        "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
    ]
    """<p>The preferences to configure on the agent space. Preferences not provided take their default values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentSpaceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.serialize_json(value["tags"])
    if "preferences" in value:
        import capo_devops_agent.types.agent_space_preferences

        out["preferences"] = (
            capo_devops_agent.types.agent_space_preferences.serialize_json(
                value["preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAgentSpaceInput:
    out: CreateAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.deserialize_json(data["tags"])
    if data.get("preferences") is not None:
        import capo_devops_agent.types.agent_space_preferences

        out["preferences"] = (
            capo_devops_agent.types.agent_space_preferences.deserialize_json(
                data["preferences"]
            )
        )
    return out


def redact_sensitive(value: CreateAgentSpaceInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
