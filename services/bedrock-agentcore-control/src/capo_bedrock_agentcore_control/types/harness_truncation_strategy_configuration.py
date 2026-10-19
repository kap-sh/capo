"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTruncationStrategyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_sliding_window_configuration
    import capo_bedrock_agentcore_control.types.harness_summarization_configuration


class _HarnessTruncationStrategyConfiguration_slidingWindow(TypedDict, closed=True):
    slidingWindow: "capo_bedrock_agentcore_control.types.harness_sliding_window_configuration.HarnessSlidingWindowConfiguration"


class _HarnessTruncationStrategyConfiguration_summarization(TypedDict, closed=True):
    summarization: "capo_bedrock_agentcore_control.types.harness_summarization_configuration.HarnessSummarizationConfiguration"


HarnessTruncationStrategyConfiguration: TypeAlias = (
    _HarnessTruncationStrategyConfiguration_slidingWindow
    | _HarnessTruncationStrategyConfiguration_summarization
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTruncationStrategyConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HarnessTruncationStrategyConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "slidingWindow" in value:
        import capo_bedrock_agentcore_control.types.harness_sliding_window_configuration

        return {
            "slidingWindow": capo_bedrock_agentcore_control.types.harness_sliding_window_configuration.serialize_json(
                value["slidingWindow"]
            )
        }
    elif "summarization" in value:
        import capo_bedrock_agentcore_control.types.harness_summarization_configuration

        return {
            "summarization": capo_bedrock_agentcore_control.types.harness_summarization_configuration.serialize_json(
                value["summarization"]
            )
        }
    else:
        raise SerializationError(
            "HarnessTruncationStrategyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> HarnessTruncationStrategyConfiguration:
    if data.get("slidingWindow") is not None:
        import capo_bedrock_agentcore_control.types.harness_sliding_window_configuration

        return {
            "slidingWindow": capo_bedrock_agentcore_control.types.harness_sliding_window_configuration.deserialize_json(
                data["slidingWindow"]
            )
        }
    elif data.get("summarization") is not None:
        import capo_bedrock_agentcore_control.types.harness_summarization_configuration

        return {
            "summarization": capo_bedrock_agentcore_control.types.harness_summarization_configuration.deserialize_json(
                data["summarization"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "HarnessTruncationStrategyConfiguration: no recognized variant key"
        )
