"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DevOpsAgentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.dev_ops_agent_space_arn


class DevOpsAgentConfiguration(TypedDict, closed=True):
    agent_space_arn: NotRequired[
        "capo_resiliencehubv2.types.dev_ops_agent_space_arn.DevOpsAgentSpaceArn"
    ]
    """<p>The ARN of the DevOps Agent Agent Space to link to this service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevOpsAgentConfiguration) -> dict:
    out: dict = {}
    if "agent_space_arn" in value:
        out["agentSpaceArn"] = value["agent_space_arn"]
    return out


def deserialize_json(data: dict) -> DevOpsAgentConfiguration:
    out: DevOpsAgentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("agentSpaceArn") is not None:
        out["agent_space_arn"] = data["agentSpaceArn"]
    return out
