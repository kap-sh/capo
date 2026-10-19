"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HostingEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn


class HostingEnvironment(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
    """<p>The Amazon Resource Name (ARN) of the hosting environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HostingEnvironment) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> HostingEnvironment:
    out: HostingEnvironment = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out
