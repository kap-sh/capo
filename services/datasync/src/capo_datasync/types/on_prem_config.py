"""Generated from Smithy shape ``com.amazonaws.datasync#OnPremConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.agent_arn_list


class OnPremConfig(TypedDict, closed=True):
    agent_arns: "capo_datasync.types.agent_arn_list.AgentArnList"
    """<p>The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your NFS file server.</p> <p>You can specify more than one agent. For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html#multiple-agents">Using multiple DataSync agents</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnPremConfig) -> dict:
    out: dict = {}
    import capo_datasync.types.agent_arn_list

    out["AgentArns"] = capo_datasync.types.agent_arn_list.serialize_aws_json_1_1(
        value["agent_arns"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnPremConfig:
    out: OnPremConfig = {}  # type: ignore[typeddict-item]
    if data.get("AgentArns") is not None:
        import capo_datasync.types.agent_arn_list

        out["agent_arns"] = capo_datasync.types.agent_arn_list.deserialize_aws_json_1_1(
            data["AgentArns"]
        )
    else:
        raise DeserializationError("OnPremConfig.agent_arns required")
    return out
