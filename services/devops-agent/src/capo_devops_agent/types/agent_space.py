"""Generated from Smithy shape ``com.amazonaws.devopsagent#AgentSpace``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.agent_space_name
    import capo_devops_agent.types.agent_space_preferences
    import capo_devops_agent.types.description
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.locale


class AgentSpace(TypedDict, closed=True):
    name: "capo_devops_agent.types.agent_space_name.AgentSpaceName"
    """<p>The name of the AgentSpace.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>The description of the AgentSpace.</p>"""
    locale: NotRequired["capo_devops_agent.types.locale.Locale"]
    """<p>The locale for the AgentSpace, which determines the language used in agent responses.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the resource was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the resource was last updated.</p>"""
    kms_key_arn: NotRequired["capo_devops_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>"""
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    preferences: NotRequired[
        "capo_devops_agent.types.agent_space_preferences.AgentSpacePreferences"
    ]
    """<p>The preferences configured on the agent space. Preferences that are not set take their default values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpace) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "locale" in value:
        out["locale"] = value["locale"]
    import capo_devops_agent._protocol.serialize

    out["createdAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_devops_agent._protocol.serialize

    out["updatedAt"] = capo_devops_agent._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "preferences" in value:
        import capo_devops_agent.types.agent_space_preferences

        out["preferences"] = (
            capo_devops_agent.types.agent_space_preferences.serialize_json(
                value["preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> AgentSpace:
    out: AgentSpace = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        out["agent_space_id"] = ""
    if data.get("preferences") is not None:
        import capo_devops_agent.types.agent_space_preferences

        out["preferences"] = (
            capo_devops_agent.types.agent_space_preferences.deserialize_json(
                data["preferences"]
            )
        )
    return out


def redact_sensitive(value: AgentSpace) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
