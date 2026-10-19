"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ProtocolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.server_protocol


class ProtocolConfiguration(TypedDict, closed=True):
    server_protocol: (
        "capo_bedrock_agentcore_control.types.server_protocol.ServerProtocol"
    )
    """<p>The server protocol for the agent runtime. This field specifies which protocol the agent runtime uses to communicate with clients.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.server_protocol

    out["serverProtocol"] = (
        capo_bedrock_agentcore_control.types.server_protocol.serialize_json(
            value["server_protocol"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtocolConfiguration:
    out: ProtocolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("serverProtocol") is not None:
        import capo_bedrock_agentcore_control.types.server_protocol

        out["server_protocol"] = (
            capo_bedrock_agentcore_control.types.server_protocol.deserialize_json(
                data["serverProtocol"]
            )
        )
    else:
        import typing

        out["server_protocol"] = typing.cast(
            "capo_bedrock_agentcore_control.types.server_protocol.ServerProtocol", ""
        )
    return out
