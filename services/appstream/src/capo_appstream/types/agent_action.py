"""Generated from Smithy shape ``com.amazonaws.appstream#AgentAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of agent action.</p> <ul> <li> <p>COMPUTER_VISION - Allows agents to take screenshots of the desktop.</p> </li> <li> <p>COMPUTER_INPUT - Allows agents to click, type, and scroll on the desktop. Requires COMPUTER_VISION to also be enabled.</p> </li> <li> <p>FORWARD_MCP_TOOLS - Allows agents to interact with applications and the desktop operating system through direct MCP calls rather than using computer use tools. Forwards MCP tools configured on the WorkSpaces application session to the agent.</p> </li> </ul>"""
AgentAction: TypeAlias = Literal[
    "COMPUTER_VISION",
    "COMPUTER_INPUT",
    "FORWARD_MCP_TOOLS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AgentAction:
    return cast(AgentAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgentAction) -> str:
    return value


def deserialize_cbor(data: str) -> AgentAction:
    return cast(AgentAction, data)
