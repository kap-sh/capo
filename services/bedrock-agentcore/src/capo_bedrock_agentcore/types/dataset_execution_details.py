"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DatasetExecutionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_invocation_details
    import capo_bedrock_agentcore.types.dataset_details


class DatasetExecutionDetails(TypedDict, closed=True):
    dataset: "capo_bedrock_agentcore.types.dataset_details.DatasetDetails"
    """<p>The dataset and the version of it that the batch evaluation ran.</p>"""
    agent_invocation: (
        "capo_bedrock_agentcore.types.agent_invocation_details.AgentInvocationDetails"
    )
    """<p>The agent that the batch evaluation invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetExecutionDetails) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.dataset_details

    out["dataset"] = capo_bedrock_agentcore.types.dataset_details.serialize_json(
        value["dataset"]
    )
    import capo_bedrock_agentcore.types.agent_invocation_details

    out["agentInvocation"] = (
        capo_bedrock_agentcore.types.agent_invocation_details.serialize_json(
            value["agent_invocation"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatasetExecutionDetails:
    out: DatasetExecutionDetails = {}  # type: ignore[typeddict-item]
    if data.get("dataset") is not None:
        import capo_bedrock_agentcore.types.dataset_details

        out["dataset"] = capo_bedrock_agentcore.types.dataset_details.deserialize_json(
            data["dataset"]
        )
    else:
        raise DeserializationError("DatasetExecutionDetails.dataset required")
    if data.get("agentInvocation") is not None:
        import capo_bedrock_agentcore.types.agent_invocation_details

        out["agent_invocation"] = (
            capo_bedrock_agentcore.types.agent_invocation_details.deserialize_json(
                data["agentInvocation"]
            )
        )
    else:
        out["agent_invocation"] = {"$unknown": {"name": ""}}
    return out
