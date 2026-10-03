"""Generated from Smithy shape ``com.amazonaws.chatbot#ConfiguredTeam``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chatbot.types.resource_state
    import capo_chatbot.types.string
    import capo_chatbot.types.uuid


class ConfiguredTeam(TypedDict, closed=True):
    tenant_id: "capo_chatbot.types.uuid.UUID"
    """<p>The ID of the Microsoft Teams tenant.</p>"""
    team_id: "capo_chatbot.types.uuid.UUID"
    """<p> The ID of the Microsoft Teams authorized with AWS Chatbot.</p> <p>To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more information, see <a href="https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup">Step 1: Configure a Microsoft Teams client</a> in the <i> AWS Chatbot Administrator Guide</i>. </p>"""
    team_name: NotRequired["capo_chatbot.types.uuid.UUID"]
    """<p>The name of the Microsoft Teams Team.</p>"""
    state: NotRequired["capo_chatbot.types.resource_state.ResourceState"]
    """<p>Either <code>ENABLED</code> or <code>DISABLED</code>. The resource returns <code>DISABLED</code> if the organization's AWS Chatbot policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.</p>"""
    state_reason: NotRequired["capo_chatbot.types.string.String"]
    """<p>Provided if State is <code>DISABLED</code>. Provides context as to why the resource is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTeam) -> dict:
    out: dict = {}
    out["TenantId"] = value["tenant_id"]
    out["TeamId"] = value["team_id"]
    if "team_name" in value:
        out["TeamName"] = value["team_name"]
    if "state" in value:
        out["State"] = value["state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> ConfiguredTeam:
    out: ConfiguredTeam = {}  # type: ignore[typeddict-item]
    if data.get("TenantId") is not None:
        out["tenant_id"] = data["TenantId"]
    else:
        raise DeserializationError("ConfiguredTeam.tenant_id required")
    if data.get("TeamId") is not None:
        out["team_id"] = data["TeamId"]
    else:
        raise DeserializationError("ConfiguredTeam.team_id required")
    if data.get("TeamName") is not None:
        out["team_name"] = data["TeamName"]
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    return out
