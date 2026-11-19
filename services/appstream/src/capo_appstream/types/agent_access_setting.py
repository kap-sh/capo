"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAccessSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.agent_action
    import capo_appstream.types.permission


class AgentAccessSetting(TypedDict, closed=True):
    agent_action: NotRequired["capo_appstream.types.agent_action.AgentAction"]
    """<p>The agent action to configure. Valid values are COMPUTER_VISION, COMPUTER_INPUT, and FORWARD_MCP_TOOLS. If you enable COMPUTER_INPUT, you must also enable COMPUTER_VISION.</p>"""
    permission: NotRequired["capo_appstream.types.permission.Permission"]
    """<p>Whether the agent action is enabled or disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAccessSetting) -> dict:
    out: dict = {}
    if "agent_action" in value:
        import capo_appstream.types.agent_action

        out["AgentAction"] = capo_appstream.types.agent_action.serialize_aws_json_1_1(
            value["agent_action"]
        )
    if "permission" in value:
        import capo_appstream.types.permission

        out["Permission"] = capo_appstream.types.permission.serialize_aws_json_1_1(
            value["permission"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentAccessSetting:
    out: AgentAccessSetting = {}  # type: ignore[typeddict-item]
    if data.get("AgentAction") is not None:
        import capo_appstream.types.agent_action

        out["agent_action"] = (
            capo_appstream.types.agent_action.deserialize_aws_json_1_1(
                data["AgentAction"]
            )
        )
    if data.get("Permission") is not None:
        import capo_appstream.types.permission

        out["permission"] = capo_appstream.types.permission.deserialize_aws_json_1_1(
            data["Permission"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgentAccessSetting) -> dict:
    out: dict = {}
    if "agent_action" in value:
        import capo_appstream.types.agent_action

        out["AgentAction"] = capo_appstream.types.agent_action.serialize_cbor(
            value["agent_action"]
        )
    if "permission" in value:
        import capo_appstream.types.permission

        out["Permission"] = capo_appstream.types.permission.serialize_cbor(
            value["permission"]
        )
    return out


def deserialize_cbor(data: dict) -> AgentAccessSetting:
    out: AgentAccessSetting = {}  # type: ignore[typeddict-item]
    if data.get("AgentAction") is not None:
        import capo_appstream.types.agent_action

        out["agent_action"] = capo_appstream.types.agent_action.deserialize_cbor(
            data["AgentAction"]
        )
    if data.get("Permission") is not None:
        import capo_appstream.types.permission

        out["permission"] = capo_appstream.types.permission.deserialize_cbor(
            data["Permission"]
        )
    return out
