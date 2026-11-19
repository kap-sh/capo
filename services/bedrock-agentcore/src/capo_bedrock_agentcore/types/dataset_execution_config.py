"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetExecutionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_invocation_config
    import capo_bedrock_agentcore.types.dataset_source


class DatasetExecutionConfig(TypedDict, closed=True):
    dataset: "capo_bedrock_agentcore.types.dataset_source.DatasetSource"
    """<p>The dataset whose scenarios are sent to the agent. The dataset must use the predefined evaluation schema, and the version that runs must contain between 1 and 1,000 scenarios.</p>"""
    agent_invocation: (
        "capo_bedrock_agentcore.types.agent_invocation_config.AgentInvocationConfig"
    )
    """<p>Specifies the agent runtime endpoint and the request template that the batch evaluation uses to invoke the agent for each scenario in the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetExecutionConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.dataset_source

    out["dataset"] = capo_bedrock_agentcore.types.dataset_source.serialize_json(
        value["dataset"]
    )
    import capo_bedrock_agentcore.types.agent_invocation_config

    out["agentInvocation"] = (
        capo_bedrock_agentcore.types.agent_invocation_config.serialize_json(
            value["agent_invocation"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatasetExecutionConfig:
    out: DatasetExecutionConfig = {}  # type: ignore[typeddict-item]
    if data.get("dataset") is not None:
        import capo_bedrock_agentcore.types.dataset_source

        out["dataset"] = capo_bedrock_agentcore.types.dataset_source.deserialize_json(
            data["dataset"]
        )
    else:
        raise DeserializationError("DatasetExecutionConfig.dataset required")
    if data.get("agentInvocation") is not None:
        import capo_bedrock_agentcore.types.agent_invocation_config

        out["agent_invocation"] = (
            capo_bedrock_agentcore.types.agent_invocation_config.deserialize_json(
                data["agentInvocation"]
            )
        )
    else:
        out["agent_invocation"] = {"$unknown": {"name": ""}}
    return out
